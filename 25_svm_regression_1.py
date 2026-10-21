"""
RELIANCE.NS swing-trading research framework (SVM classifier + honest backtest)

What changed vs. the SVR price-prediction version
-------------------------------------------------
1. Predicts a TRADE OUTCOME, not tomorrow's return.
   Label = "does a trade entered at tomorrow's open hit +TAKE_PROFIT before
   -STOP_LOSS within HOLD_DAYS?"  (triple-barrier label).  This matches the
   2-5% per-trade goal directly and has far better signal-to-noise than a
   1-day return (your R^2 was ~0.000 and direction accuracy ~50%).
2. No look-ahead: features use data up to the close of day T, the trade enters
   at the OPEN of day T+1.  No .shift(1) tricks needed.
3. Purged walk-forward: a model is only trained on trades that had already
   finished before the prediction date (labels overlap in time otherwise).
4. Realistic backtest: one position at a time, stop/target checked on daily
   High/Low (stop wins if both hit the same day), gap-through-stop fills at the
   open, brokerage/STT/slippage as a cost per side.
5. Honest benchmarks: buy & hold, and "same trade rules, no model".
   If the model does not beat the no-model baseline, it has no edge.

NOTE: research tool, not investment advice.  Past results do not guarantee
future returns, and a "2-5%" target cannot be guaranteed by any model.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

from sklearn.svm import SVC
from sklearn.preprocessing import RobustScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import TimeSeriesSplit, GridSearchCV
from sklearn.metrics import roc_auc_score

# ============================================================
# CONFIG  (change these, re-run, compare)
# ============================================================
# STOCK = "RELIANCE.NS"
STOCK = "M&M.NS"
INDEX = "^NSEI"
PERIOD = "10y"            # more history = more trades to learn from

HOLD_DAYS = 7             # max trading days a trade is kept
TAKE_PROFIT = 0.03        # +3% target  (inside your 2-5% band)
STOP_LOSS = 0.015         # -1.5% stop  (reward:risk = 2:1)

# Round-trip cost = 2 * COST_PER_SIDE. 0.12% per side ~ delivery trade incl.
# STT, stamp duty, exchange fees, GST and a little slippage. Check your broker.
COST_PER_SIDE = 0.0012

EDGE_MARGIN = 0.05        # trade only if P(target) > base rate + this margin
USE_TREND_FILTER = True   # only long when Close > 50-day SMA
POSITION_FRACTION = 1.0   # share of capital used per trade (1.0 = all-in)
START_CAPITAL = 100_000

TEST_FRACTION = 0.30      # last 30% of labelled history = out-of-sample
REFIT_STEP = 20           # refit model every 20 trading days in the test
GOAL_LOW, GOAL_HIGH = 0.02, 0.05   # 2-5% net return per trade

FEATURES = [
    "ret_1d", "ret_5d", "ret_10d", "ret_20d",
    "rel_5d", "rel_20d",
    "dist_sma20", "dist_sma50", "dist_sma200",
    "atr_pct", "vol_ratio", "rsi", "rel_vol",
    "clv", "intraday", "off_high_60", "nifty_trend",
]


# ============================================================
# STEP 1: Data
# ============================================================
def load_data():
    print(f"Downloading {STOCK} and {INDEX} ({PERIOD})...")
    stock = yf.Ticker(STOCK).history(period=PERIOD, interval="1d", auto_adjust=True)
    index = yf.Ticker(INDEX).history(period=PERIOD, interval="1d", auto_adjust=True)
    if stock.empty or index.empty:
        raise RuntimeError("No data downloaded. Check connection and tickers.")
    df = stock[["Open", "High", "Low", "Close", "Volume"]].dropna().copy()
    df["Nifty"] = index["Close"].reindex(df.index).ffill()
    return df.dropna()
# ============================================================
# STEP 2: Features (all use data up to the close of day T only)
# ============================================================
def build_features(df):
    o, h, l, c, v, nifty = (df[k] for k in ["Open", "High", "Low", "Close", "Volume", "Nifty"])
    r = c.pct_change()
    f = pd.DataFrame(index=df.index)

    for k in (1, 5, 10, 20):
        f[f"ret_{k}d"] = c.pct_change(k)
    for k in (5, 20):                                   # relative strength vs NIFTY
        f[f"rel_{k}d"] = c.pct_change(k) - nifty.pct_change(k)
    for k in (20, 50, 200):                             # trend position
        f[f"dist_sma{k}"] = c / c.rolling(k).mean() - 1

    prev_c = c.shift(1)
    tr = pd.concat([h - l, (h - prev_c).abs(), (l - prev_c).abs()], axis=1).max(axis=1)
    f["atr_pct"] = tr.rolling(14).mean() / c            # volatility level
    f["vol_ratio"] = r.rolling(5).std() / r.rolling(20).std()

    delta = c.diff()
    gain = delta.clip(lower=0).rolling(14).mean()
    loss = (-delta.clip(upper=0)).rolling(14).mean()
    rsi = 100 - 100 / (1 + gain / loss.replace(0, np.nan))
    f["rsi"] = (rsi.fillna(50.0) - 50.0) / 50.0

    f["rel_vol"] = v / v.rolling(20).mean()
    span = (h - l).replace(0, np.nan)
    f["clv"] = (((c - l) - (h - c)) / span).fillna(0.0)
    f["intraday"] = c / o - 1
    f["off_high_60"] = c / c.rolling(60).max() - 1       # pullback depth
    f["nifty_trend"] = nifty / nifty.rolling(50).mean() - 1
    return f.replace([np.inf, -np.inf], np.nan)


# ============================================================
# STEP 3: Trade simulation + triple-barrier labels
# ============================================================
def simulate_trade(o, h, l, c, i, hold, tp, sl):
    """
    Signal at close of day i -> buy at OPEN of day i+1.
    Returns (exit_pos, gross_return, reason) or None if the window is incomplete.
    """
    e = i + 1
    if e + hold - 1 > len(o) - 1:
        return None
    entry = o[e]
    tp_px, sl_px = entry * (1 + tp), entry * (1 - sl)
    for j in range(e, e + hold):
        if j > e:                                        # overnight gaps
            if o[j] <= sl_px:
                return j, o[j] / entry - 1, "STOP"
            if o[j] >= tp_px:
                return j, o[j] / entry - 1, "TARGET"
        if l[j] <= sl_px:                                # stop assumed first
            return j, -sl, "STOP"
        if h[j] >= tp_px:
            return j, tp, "TARGET"
    return e + hold - 1, c[e + hold - 1] / entry - 1, "TIME"


def build_dataset(df, feats):
    o, h, l, c = (df[k].to_numpy() for k in ["Open", "High", "Low", "Close"])
    n = len(df)
    exit_pos = np.full(n, -1)
    gross = np.full(n, np.nan)
    reason = np.array([""] * n, dtype=object)
    for i in range(n - 1):
        res = simulate_trade(o, h, l, c, i, HOLD_DAYS, TAKE_PROFIT, STOP_LOSS)
        if res is not None:
            exit_pos[i], gross[i], reason[i] = res

    data = feats.copy()
    data["pos"] = np.arange(n)
    data["exit_pos"] = exit_pos
    data["gross_ret"] = gross
    data["reason"] = reason
    data["label"] = (reason == "TARGET").astype(int)
    data["trend_ok"] = (feats["dist_sma50"] > 0) if USE_TREND_FILTER else True
    data = data.dropna(subset=FEATURES)
    labelled = data[data["exit_pos"] >= 0].copy()
    latest = data.iloc[[-1]]          # newest bar: features only, trade not finished
    return labelled, latest


# ============================================================
# STEP 4: Model, tuning, purged walk-forward
# ============================================================
def make_model(C=1.0, gamma="scale"):
    return make_pipeline(
        RobustScaler(),
        SVC(kernel="rbf", C=C, gamma=gamma, class_weight="balanced",
            probability=True, random_state=42),
    )


def tune(train):
    print("Tuning SVC on the initial training block (time-series CV with gap)...")
    pipe = make_model()
    grid = {
        "svc__C": [0.1, 0.5, 1.0, 3.0],
        "svc__gamma": ["scale", 0.01, 0.05],
    }
    gs = GridSearchCV(
        pipe, grid, scoring="roc_auc",
        cv=TimeSeriesSplit(n_splits=5, gap=HOLD_DAYS), n_jobs=-1,
    )
    gs.fit(train[FEATURES], train["label"])
    print("Best params:", gs.best_params_, f"| CV AUC: {gs.best_score_:.3f}")
    return gs.best_params_["svc__C"], gs.best_params_["svc__gamma"]


def walk_forward(lab, test, C, gamma):
    probs = np.zeros(len(test))
    thresholds = np.zeros(len(test))
    print(f"Walk-forward: refit every {REFIT_STEP} days, purged training labels...")
    for s in range(0, len(test), REFIT_STEP):
        chunk = test.iloc[s:s + REFIT_STEP]
        cutoff = chunk["pos"].iloc[0]
        hist = lab[lab["exit_pos"] <= cutoff]            # only trades already finished
        model = make_model(C, gamma).fit(hist[FEATURES], hist["label"])
        probs[s:s + len(chunk)] = model.predict_proba(chunk[FEATURES])[:, 1]
        thresholds[s:s + len(chunk)] = hist["label"].mean() + EDGE_MARGIN
    return probs, thresholds


# ============================================================
# STEP 5: Backtest (one position at a time, compounding)
# ============================================================
def backtest(test, signal, df, label):
    o, c = df["Open"].to_numpy(), df["Close"].to_numpy()
    n = len(df)
    p0 = int(test["pos"].iloc[0]) + 1
    equity = np.full(n - p0, float(START_CAPITAL))       # daily mark-to-market
    cap, busy_until, trades = float(START_CAPITAL), -1, []
    cost = COST_PER_SIDE

    for k, (_, row) in enumerate(test.iterrows()):
        if not signal[k] or row["pos"] < busy_until:
            continue
        pos, xpos = int(row["pos"]), int(row["exit_pos"])
        entry_px = o[pos + 1]
        stake = cap * POSITION_FRACTION
        net = POSITION_FRACTION * ((1 + row["gross_ret"]) * (1 - cost) ** 2 - 1)

        for j in range(pos + 1, xpos + 1):               # daily path of this trade
            if j == xpos:
                val = cap + stake * ((1 + row["gross_ret"]) * (1 - cost) ** 2 - 1)
            else:
                val = cap + stake * (c[j] / entry_px * (1 - cost) - 1)
            equity[j - p0] = val
        new_cap = cap * (1 + net)
        equity[xpos - p0 + 1:] = new_cap
        trades.append({
            "signal_date": df.index[pos], "entry_date": df.index[pos + 1],
            "exit_date": df.index[xpos], "reason": row["reason"],
            "gross_%": row["gross_ret"] * 100, "net_%": net * 100,
            "capital": new_cap,
        })
        cap, busy_until = new_cap, xpos

    return pd.DataFrame(trades), pd.Series(equity, index=df.index[p0:]), label


def summarize(name, trades, equity, years):
    if trades.empty:
        print(f"\n[{name}] no trades")
        return
    net = trades["net_%"] / 100
    wins, losses = net[net > 0], net[net <= 0]
    pf = wins.sum() / abs(losses.sum()) if losses.sum() != 0 else np.inf
    total = equity.iloc[-1] / START_CAPITAL - 1
    cagr = (1 + total) ** (1 / years) - 1 if years > 0 else np.nan
    mdd = (equity / equity.cummax() - 1).min()
    print(f"\n------ {name} ------")
    print(f"Trades                     : {len(trades)}  (~{len(trades) / years:.1f}/yr)")
    print(f"Win rate                   : {(net > 0).mean() * 100:.1f}%")
    print(f"Avg net return / trade     : {net.mean() * 100:+.2f}%")
    print(f"Trades netting >= {GOAL_LOW*100:.0f}%        : {(net >= GOAL_LOW).mean() * 100:.1f}%")
    print(f"Trades netting {GOAL_LOW*100:.0f}-{GOAL_HIGH*100:.0f}%        : "
          f"{((net >= GOAL_LOW) & (net <= GOAL_HIGH)).mean() * 100:.1f}%")
    print(f"Exit reasons               : {trades['reason'].value_counts().to_dict()}")
    print(f"Profit factor              : {pf:.2f}")
    print(f"Total return (out-of-sample): {total * 100:+.1f}%   | CAGR: {cagr * 100:+.1f}%")
    print(f"Max drawdown               : {mdd * 100:.1f}%")


# ============================================================
# STEP 6: Run everything
# ============================================================
def main():
    df = load_data()
    feats = build_features(df)
    lab, latest = build_dataset(df, feats)

    base_rate = lab["label"].mean()
    breakeven = (STOP_LOSS + 2 * COST_PER_SIDE) / (TAKE_PROFIT + STOP_LOSS)
    print(f"\nLabelled trade setups: {len(lab)} | target-hit base rate: {base_rate:.1%}")
    print(f"Approx. break-even hit rate for TP {TAKE_PROFIT:.1%} / SL {STOP_LOSS:.1%} "
          f"after costs (ignoring time exits): {breakeven:.1%}")

    split = int(len(lab) * (1 - TEST_FRACTION))
    train, test = lab.iloc[:split], lab.iloc[split:]
    print(f"Initial train: {len(train)} | Out-of-sample test: {len(test)} "
          f"({test.index[0].date()} -> {test.index[-1].date()})")

    C, gamma = tune(train)
    probs, thresholds = walk_forward(lab, test, C, gamma)

    auc = roc_auc_score(test["label"], probs)
    print(f"\nOut-of-sample AUC: {auc:.3f}   (0.50 = coin flip; >0.55 is a real, rare edge)")

    model_signal = (probs >= thresholds) & test["trend_ok"].to_numpy()
    trend_only = test["trend_ok"].to_numpy()
    years = (test.index[-1] - test.index[0]).days / 365.25

    tr_m, eq_m, _ = backtest(test, model_signal, df, "model")
    tr_b, eq_b, _ = backtest(test, trend_only, df, "baseline")
    p0 = int(test["pos"].iloc[0]) + 1
    bh = START_CAPITAL * df["Close"].iloc[p0:] / df["Open"].iloc[p0]

    summarize("SVM STRATEGY (out-of-sample)", tr_m, eq_m, years)
    summarize("BASELINE: same rules, no model", tr_b, eq_b, years)
    bh_total = bh.iloc[-1] / START_CAPITAL - 1
    print(f"\n------ BUY & HOLD ------\nTotal return: {bh_total*100:+.1f}% | "
          f"Max drawdown: {(bh / bh.cummax() - 1).min() * 100:.1f}%")

    # Honest verdict against the goal
    print("\n========== GOAL CHECK (2-5% net per trade) ==========")
    if tr_m.empty:
        print("No trades taken - lower EDGE_MARGIN or loosen the filter.")
    else:
        avg = tr_m["net_%"].mean()
        edge_vs_base = avg - (tr_b["net_%"].mean() if not tr_b.empty else 0)
        print(f"Average net return per trade: {avg:+.2f}%  (goal: {GOAL_LOW*100:.0f}-{GOAL_HIGH*100:.0f}%)")
        print(f"Improvement over no-model baseline: {edge_vs_base:+.2f}% per trade")
        if avg >= GOAL_LOW * 100 and auc > 0.53:
            print("Verdict: goal met in this test. Now stress-test it (other stocks, other periods).")
        else:
            print("Verdict: goal NOT met on a per-trade average. Don't trade this live yet.")

    # Next-day plan
    X_all = lab[FEATURES]
    final = make_model(C, gamma).fit(X_all, lab["label"])
    p_next = final.predict_proba(latest[FEATURES])[0, 1]
    thr_next = base_rate + EDGE_MARGIN
    trend_ok = bool(latest["trend_ok"].iloc[0])
    go = (p_next >= thr_next) and trend_ok
    last_close = df["Close"].iloc[-1]
    print("\n========== NEXT-SESSION PLAN ==========")
    print(f"As of close {df.index[-1].date()}: {last_close:.2f} INR")
    print(f"P(target before stop): {p_next:.1%} (needs >= {thr_next:.1%}) | trend filter ok: {trend_ok}")
    if go:
        print("Signal: BUY at next open")
        print(f"  Stop  : open x {1 - STOP_LOSS:.3f}  (~{last_close * (1 - STOP_LOSS):.2f})")
        print(f"  Target: open x {1 + TAKE_PROFIT:.3f}  (~{last_close * (1 + TAKE_PROFIT):.2f})")
        print(f"  Exit at close of day {HOLD_DAYS} if neither is hit")
    else:
        print("Signal: NO TRADE (stay in cash)")

    # Plots
    fig, ax = plt.subplots(1, 2, figsize=(15, 5))
    ax[0].plot(eq_m, label="SVM strategy", linewidth=1.6)
    ax[0].plot(eq_b, label="Same rules, no model", alpha=0.7)
    ax[0].plot(bh, label="Buy & hold", alpha=0.7)
    ax[0].set_title(f"{STOCK}: out-of-sample equity (after costs)")
    ax[0].legend(); ax[0].grid(alpha=0.3)
    if not tr_m.empty:
        ax[1].hist(tr_m["net_%"], bins=25, color="steelblue", edgecolor="white")
        ax[1].axvspan(GOAL_LOW * 100, GOAL_HIGH * 100, color="green", alpha=0.2, label="2-5% goal band")
        ax[1].axvline(0, color="black", linewidth=0.8)
        ax[1].set_title("Net return per trade (%)")
        ax[1].legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()