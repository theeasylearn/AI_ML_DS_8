'''
Used Car Resale Value Prediction
Estimate the depreciation value and resale price of used vehicles.
Dataset : https://www.kaggle.com/datasets/jarupula/machine-hack?select=train.csv
'''
# STEP 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
import numpy as np
import kagglehub

# Download latest version
path = kagglehub.dataset_download("jarupula/machine-hack")
print("Path to dataset files:", path)
df = pd.read_csv(path + "/train.csv")
print("\nFirst five rows:")
df = df.dropna()
# print(df.head())
print("before cleaning",df.shape)
print(df.columns.to_list())
df = df.drop_duplicates()
df['Levy'] = df['Levy'].replace('-', np.nan).astype(float)

# Engine volume: Extract 'Turbo' binary feature FIRST, then clean string and replace 0 with NaN
#Feature Engineering
df['Turbo'] = df['Engine volume'].str.contains('Turbo', na=False).astype(int)
df['Engine volume'] = (
    df['Engine volume']
    .str.replace('Turbo','', regex=False)
    .str.strip()
    .astype(float)
    .replace(0.0, np.nan)
)

# Mileage: Strip ' km', convert to float, and replace 0 km with NaN
df['Mileage'] = (
    df['Mileage']
    .str.replace(' km', '', regex=False)
    .str.strip()
    .astype(float)
    .replace(0.0, np.nan)
)

# Apply dropna across the cleaned numeric columns
df = df.dropna(subset=['Levy', 'Engine volume', 'Mileage'])

df = df[(df['Price'] >= 500) & (df['Price'] <= 200000) & (df['Mileage'] <= 1000000)].copy()
df['Leather interior'] = df['Leather interior'].map({'Yes': 1, 'No': 0})
df['Wheel'] = df['Wheel'].map({'Left wheel': 0, 'Right-hand drive': 1})


print(f"After dropna on Levy, Engine volume, and Mileage: {df.shape}")
exit(1)
'''
    ['ID', 'Price', 'Levy', 'Manufacturer', 'Model', 'Prod. year', 'Category', 'Leather interior', 'Fuel type', 'Engine volume', 'Mileage', 'Cylinders', 'Gear box type', 'Drive wheels', 'Doors', 'Wheel', 'Color', 'Airbags']
'''
exit(1)

feature_columns = ['Levy', 'Manufacturer', 'Prod. year', 'Category', 'Leather interior', 'Fuel type', 'Engine volume', 'Mileage', 'Cylinders', 'Gear box type', 'Drive wheels', 'Wheel', 'Color', 'Airbags','Turbo']

X = df[feature_columns]
y = df["Price"]

# STEP 4: Split data chronologically
# Do not shuffle stock market time-series data

split_index = int(len(df) * 0.80)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]
y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

print("\nTraining records:", len(X_train))
print("Testing records:", len(X_test))


# STEP 5: Create and train the SVR model

# Scaling is important for SVR because its results
# depend on distances and feature magnitudes.

model = make_pipeline(
    StandardScaler(),
    SVR(kernel="rbf", C=100, epsilon=0.1)
)

print("\nTraining SVR model...")

model.fit(X_train, y_train)

print("Model trained successfully!")


# STEP 6: Predict test-set closing prices

y_pred = model.predict(X_test)


# STEP 7: Evaluate model performance

mae = mean_absolute_error(y_test, y_pred)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))

r2 = r2_score(y_test, y_pred)

print("\n========== MODEL PERFORMANCE ==========")

print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")


# STEP 8: Compare actual and predicted prices

results = pd.DataFrame({
    "Actual Price": y_test,
    "Predicted Price": y_pred
}, index=y_test.index)

print("\nLast 10 predictions:")
print(results.tail(10).round(2))


# STEP 9: Plot actual vs predicted prices

plt.figure(figsize=(12, 6))

plt.plot(
    results.index,
    results["Actual Price"],
    label="Actual Closing Price"
)

plt.plot(
    results.index,
    results["Predicted Price"],
    label="Predicted Closing Price"
)

plt.title("Reliance Industries: Actual vs SVR Predicted Prices")
plt.xlabel("Date")
plt.ylabel("Price (INR)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# STEP 10: Predict the next trading day's closing price

# The latest five observed trading days provide the features.
latest_features = pd.DataFrame(
    [[
        df["Close"].iloc[-1],
        df["Close"].iloc[-2],
        df["Close"].iloc[-3],
        df["Close"].iloc[-4],
        df["Close"].iloc[-5],
        df["Volume"].iloc[-1],
        df["Volume"].iloc[-2],
        df["Volume"].iloc[-3],
        df["Volume"].iloc[-4],
        df["Volume"].iloc[-5]
    ]],
    columns=feature_columns
)

next_price = model.predict(latest_features)[0]

print("\n========== NEXT-DAY FORECAST ==========")

print("Latest available closing price:",
      round(df["Close"].iloc[-1], 2))

print("Predicted next trading-day close:",
      round(next_price, 2))
