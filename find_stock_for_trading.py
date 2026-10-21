"""
Screen many NSE stocks with the SAME walk-forward SVM swing strategy and rank them
by OUT-OF-SAMPLE results.  Put this file next to 25_svm_swing_strategy.py.

Why this instead of "pick the best stock": with ~30 stocks, the top one will look
good by luck alone.  So a stock only makes the shortlist if it passes ALL of:
  - enough trades (>= MIN_TRADES)
  - out-of-sample AUC above MIN_AUC
  - positive average net return per trade
  - beats the no-model baseline on the same stock
  - profitable in BOTH halves of its out-of-sample trades
Treat the shortlist as "worth paper-trading", not as a recommendation.
"""

import importlib.util
import pathlib
import warnings

import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score

warnings.filterwarnings("ignore")

# ---- load the strategy module (filename starts with a digit, so use importlib) ----
path = pathlib.Path(__file__).with_name("25_svm_regression_1.py")
spec = importlib.util.spec_from_file_location("strat", path)
strat = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strat)

UNIVERSE = [
    "RELIANCE", "TCS", "HDFCBANK", "ICICIBANK", "INFY", "SBIN", "BHARTIARTL", "ITC",
    "LT", "AXISBANK", "KOTAKBANK", "HINDUNILVR", "BAJFINANCE", "MARUTI", "M&M",
    "SUNPHARMA", "TATASTEEL", "NTPC", "POWERGRID", "ONGC", "COALINDIA", "ADANIPORTS",
    "TITAN", "ULTRACEMCO", "WIPRO", "HCLTECH", "TECHM", "JSWSTEEL", "HINDALCO",
    "BAJAJ-AUTO", "EICHERMOT", "CIPLA", "DRREDDY", "GRASIM", "INDUSINDBK",
]  # edit freely; a failed download is skipped

MIN_TRADES = 25
MIN_AUC = 0.52
C, GAMMA = 1.0, "scale"      # fixed (no per-stock tuning -> less overfitting, faster)
strat.PERIOD = "10y"


def evaluate(symbol):
    strat.STOCK = f"{symbol}.NS"
    df = strat.load_data()
    feats = strat.build_features(df)
    lab, _ = strat.build_dataset(df, feats)

    split = int(len(lab) * (1 - strat.TEST_FRACTION))
    test = lab.iloc[split:]
    probs, thr = strat.walk_forward(lab, test, C, GAMMA)

    sig = (probs >= thr) & test["trend_ok"].to_numpy()
    base = test["trend_ok"].to_numpy()
    tr_m, _, _ = strat.backtest(test, sig, df, "m")
    tr_b, _, _ = strat.backtest(test, base, df, "b")

    row = {
        "stock": symbol,
        "atr_%": round(float(feats["atr_pct"].iloc[-60:].mean() * 100), 2),
        "auc": round(roc_auc_score(test["label"], probs), 3),
        "trades": len(tr_m),
        "avg_net_%": round(tr_m["net_%"].mean(), 2) if len(tr_m) else np.nan,
        "base_avg_net_%": round(tr_b["net_%"].mean(), 2) if len(tr_b) else np.nan,
        "win_%": round((tr_m["net_%"] > 0).mean() * 100, 1) if len(tr_m) else np.nan,
    }
    if len(tr_m) >= 4:
        half = len(tr_m) // 2
        row["1st_half_%"] = round(tr_m["net_%"].iloc[:half].mean(), 2)
        row["2nd_half_%"] = round(tr_m["net_%"].iloc[half:].mean(), 2)
    return row


def main():
    rows = []
    for sym in UNIVERSE:
        try:
            print(f"\n=== {sym} ===")
            rows.append(evaluate(sym))
        except Exception as e:                      # keep going if one ticker fails
            print(f"  skipped {sym}: {e}")

    res = pd.DataFrame(rows)
    for col in ("1st_half_%", "2nd_half_%"):
        if col not in res:
            res[col] = np.nan
    res["uplift_%"] = res["avg_net_%"] - res["base_avg_net_%"]
    res["passes"] = (
        (res["trades"] >= MIN_TRADES) & (res["auc"] >= MIN_AUC)
        & (res["avg_net_%"] > 0) & (res["uplift_%"] > 0)
        & (res["1st_half_%"] > 0) & (res["2nd_half_%"] > 0)
    )
    res = res.sort_values(["passes", "avg_net_%"], ascending=False)

    pd.set_option("display.width", 200)
    print("\n================ SCREEN RESULTS (out-of-sample) ================")
    print(res.to_string(index=False))
    res.to_csv("screen_results.csv", index=False)

    short = res[res["passes"]]
    print("\n================ SHORTLIST ================")
    if short.empty:
        print("No stock passed every test. That is a valid, useful result: "
              "no reliable edge was found in this universe with these features.")
    else:
        print(short[["stock", "auc", "trades", "avg_net_%", "uplift_%"]].to_string(index=False))
        print(f"\nChance check: with {len(res)} stocks tested, a few can pass by luck. "
              "Paper-trade the shortlist before using real money.")


if __name__ == "__main__":
    main()