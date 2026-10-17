# ============================================================
# UPGRADED SVM REGRESSION: INDIAN STOCK PRICE PREDICTION
# Stock: Reliance Industries (NSE) | Stationary Return-Based SVR
# ============================================================
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.compose import TransformedTargetRegressor
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import TimeSeriesSplit, GridSearchCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# STEP 1: Download Indian stock market data
stock_code = "RELIANCE.NS"
print("Downloading stock data...")
df = yf.Ticker(stock_code).history(period="5y", interval="1d", auto_adjust=True)

if df.empty:
    raise RuntimeError("No stock data downloaded. Check connection and ticker.")

df = df[["Close", "Volume"]].dropna().copy()

# STEP 2: Stationary Feature Engineering (5 Trading Days)
# 1-day price diff and log volume change prevent RBF kernel saturation
df["Price_Diff"] = df["Close"].diff()
df["Log_Vol"] = np.log1p(df["Volume"])

feature_columns = []
for lag in range(1, 6):
    # Lagged price changes (stationary) and lagged close ratios
    df[f"Diff_lag_{lag}"] = df["Price_Diff"].shift(lag)
    df[f"Vol_lag_{lag}"] = df["Log_Vol"].shift(lag)
    feature_columns.extend([f"Diff_lag_{lag}", f"Vol_lag_{lag}"])

# Keep yesterday's close to reconstruct absolute price predictions
df["Close_lag_1"] = df["Close"].shift(1)

# Target: Today's price change (Close_t - Close_{t-1})
df["Target_Diff"] = df["Close"] - df["Close_lag_1"]
df = df.dropna()

X = df[feature_columns]
y_diff = df["Target_Diff"]
actual_close = df["Close"]
prev_close = df["Close_lag_1"]

# STEP 3: Chronological Train/Test Split (80/20)
split_index = int(len(df) * 0.80)

X_train, X_test = X.iloc[:split_index], X.iloc[split_index:]
y_train_diff, y_test_diff = y_diff.iloc[:split_index], y_diff.iloc[split_index:]
y_test_actual = actual_close.iloc[split_index:]
y_test_prev = prev_close.iloc[split_index:]

print(f"\nTraining records: {len(X_train)} | Testing records: {len(X_test)}")

# STEP 4: Scale Both X and y + Time-Series Cross-Validation
base_pipeline = make_pipeline(StandardScaler(), SVR(kernel="rbf"))
model = TransformedTargetRegressor(
    regressor=base_pipeline,
    transformer=StandardScaler()
)

param_grid = {
    "regressor__svr__C": [0.1, 1.0, 10.0],
    "regressor__svr__epsilon": [0.05, 0.1, 0.2],
    "regressor__svr__gamma": ["scale", 0.05, 0.1]
}

tscv = TimeSeriesSplit(n_splits=5)
grid_search = GridSearchCV(
    model, param_grid, cv=tscv, scoring="neg_root_mean_squared_error", n_jobs=-1
)

print("Tuning and training SVR model...")
grid_search.fit(X_train, y_train_diff)
best_model = grid_search.best_estimator_
print("Best Hyperparameters:", grid_search.best_params_)

# STEP 5: Predict Price Change & Reconstruct Closing Price
pred_diff = best_model.predict(X_test)
y_pred = y_test_prev + pred_diff

# STEP 6: Evaluate Against Naive Baseline (Yesterday's Close)
mae = mean_absolute_error(y_test_actual, y_pred)
rmse = np.sqrt(mean_squared_error(y_test_actual, y_pred))
r2 = r2_score(y_test_actual, y_pred)

naive_mae = mean_absolute_error(y_test_actual, y_test_prev)
naive_rmse = np.sqrt(mean_squared_error(y_test_actual, y_test_prev))

# Directional Accuracy: Did the model predict the sign of the move?
actual_direction = np.sign(y_test_actual - y_test_prev)
pred_direction = np.sign(pred_diff)
dir_accuracy = np.mean(actual_direction == pred_direction) * 100

print("\n========== MODEL PERFORMANCE vs. NAIVE BASELINE ==========")
print(f"SVR MAE            : {mae:.2f} INR  (Naive Baseline: {naive_mae:.2f} INR)")
print(f"SVR RMSE           : {rmse:.2f} INR  (Naive Baseline: {naive_rmse:.2f} INR)")
print(f"SVR R²             : {r2:.4f}")
print(f"Directional Acc.   : {dir_accuracy:.2f}%")

# STEP 7: Compare Last 10 Actual and Predicted Prices
results = pd.DataFrame({
    "Prev Close": y_test_prev,
    "Actual Price": y_test_actual,
    "Predicted Price": y_pred,
    "Predicted Move": pred_diff
}, index=y_test_actual.index)

print("\nLast 10 predictions:")
print(results.tail(10).round(2))

# STEP 8: Next-Day Forecast
latest_row = pd.DataFrame([[
    df["Price_Diff"].iloc[-1], df["Log_Vol"].iloc[-1],
    df["Price_Diff"].iloc[-2], df["Log_Vol"].iloc[-2],
    df["Price_Diff"].iloc[-3], df["Log_Vol"].iloc[-3],
    df["Price_Diff"].iloc[-4], df["Log_Vol"].iloc[-4],
    df["Price_Diff"].iloc[-5], df["Log_Vol"].iloc[-5],
]], columns=feature_columns)

next_diff = best_model.predict(latest_row)[0]
latest_close = df["Close"].iloc[-1]
next_price = latest_close + next_diff

print("\n========== NEXT-DAY FORECAST ==========")
print(f"Latest available closing price : {latest_close:.2f} INR")
print(f"Predicted next-day move        : {next_diff:+.2f} INR")
print(f"Predicted next trading-day close: {next_price:.2f} INR")

# STEP 9: Plot Actual vs Predicted Prices
plt.figure(figsize=(12, 6))
plt.plot(results.index, results["Actual Price"], label="Actual Closing Price", linewidth=1.5)
plt.plot(results.index, results["Predicted Price"], label="SVR Predicted Price", linestyle="--", alpha=0.85)
plt.title("Reliance Industries (RELIANCE.NS): Actual vs Stationary SVR Predicted Prices")
plt.xlabel("Date")
plt.ylabel("Price (INR)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()