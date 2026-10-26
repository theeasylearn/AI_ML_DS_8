'''
Used Car Resale Value Prediction
Estimate the depreciation value and resale price of used vehicles.
Dataset : https://www.kaggle.com/datasets/jarupula/machine-hack?select=train.csv
'''
# STEP 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import kagglehub
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler, TargetEncoder
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# STEP 2: Download and load dataset
path = kagglehub.dataset_download("jarupula/machine-hack")
print("Path to dataset files:", path)
df = pd.read_csv(path + "/train.csv")
df = df.dropna()

print(f"Shape before cleaning: {df.shape}")
df = df.drop_duplicates()

# STEP 3: Data Cleaning & Feature Engineering
df['Levy'] = df['Levy'].replace('-', np.nan).astype(float)

# Engine volume: Extract 'Turbo' binary feature FIRST, then clean string
df['Turbo'] = df['Engine volume'].str.contains('Turbo', na=False).astype(int)
df['Engine volume'] = (
    df['Engine volume']
    .str.replace('Turbo', '', regex=False)
    .str.strip()
    .astype(float)
    .replace(0.0, np.nan)
)

# Mileage: Strip ' km', convert to float
df['Mileage'] = (
    df['Mileage']
    .str.replace(' km', '', regex=False)
    .str.strip()
    .astype(float)
    .replace(0.0, np.nan)
)

# Apply dropna across the cleaned numeric columns
df = df.dropna(subset=['Levy', 'Engine volume', 'Mileage'])

# Filter out extreme outliers (salvage cars and ultra-exotics)
df = df[(df['Price'] >= 1500) & (df['Price'] <= 200000) & (df['Mileage'] <= 4000000)].copy()

# Binary mapping
df['Leather interior'] = df['Leather interior'].map({'Yes': 1, 'No': 0})
df['Wheel'] = df['Wheel'].map({'Left wheel': 0, 'Right-hand drive': 1})

# Manufacturer Bitwise Encoding
manufacturers = {val: idx + 1 for idx, val in enumerate(df['Manufacturer'].unique())}
m_codes = df['Manufacturer'].map(manufacturers).to_numpy(dtype=int)
n_bits = int(np.ceil(np.log2(len(manufacturers) + 1)))

for bit in range(n_bits):
    df[f'Manufacturer_bin_{bit}'] = (m_codes >> bit) & 1
df = df.drop(columns=['Manufacturer'])

# One-Hot Encoding for remaining categorical columns
ohe_cols = ['Gear box type', 'Drive wheels', 'Fuel type', 'Category', 'Color']
df = pd.get_dummies(df, columns=ohe_cols, drop_first=True, dtype=int)

print(f"Shape after cleaning & OHE: {df.shape}")

# STEP 4: Feature Selection & Target Transformation
# Keep 'Model' for Target Encoding, drop unhandled 'Doors', 'ID', and 'Price'
X = df.drop(columns=['ID', 'Price', 'Doors'])

# Log-transform target to prevent high-price cars from dominating SVR loss
y = np.log1p(df['Price'])

# STEP 5: Train/Test Split (Must happen before Target Encoding to prevent leakage)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# STEP 6: Target Encoding for 'Model'
encoder = TargetEncoder(target_type="continuous")
X_train['Model_encoded'] = encoder.fit_transform(X_train[['Model']], y_train)
X_test['Model_encoded'] = encoder.transform(X_test[['Model']])

# Drop the original string column
X_train = X_train.drop(columns=['Model'])
X_test = X_test.drop(columns=['Model'])

# STEP 7: Feature Scaling
num_cols = ['Levy', 'Prod. year', 'Engine volume', 'Mileage', 'Cylinders', 'Airbags', 'Model_encoded']
scaler = StandardScaler()

X_train[num_cols] = scaler.fit_transform(X_train[num_cols])
X_test[num_cols] = scaler.transform(X_test[num_cols])

# STEP 8: Model Training
svr = SVR(kernel='rbf', C=5.0, epsilon=0.1)
print("\nTraining SVR model (this may take a moment)...")
svr.fit(X_train, y_train)

# STEP 9: Predictions & Evaluation
y_pred = svr.predict(X_test)

# Inverse the log transformation for readable dollar metrics
y_test_inv = np.expm1(y_test)
y_pred_inv = np.expm1(y_pred)

mae = mean_absolute_error(y_test_inv, y_pred_inv)
rmse = np.sqrt(mean_squared_error(y_test_inv, y_pred_inv))
r2 = r2_score(y_test_inv, y_pred_inv)

print("\n========== MODEL PERFORMANCE ==========")
print(f"MAE  : ${mae:,.2f}")
print(f"RMSE : ${rmse:,.2f}")
print(f"R²   : {r2:.4f}")

# Compare actual and predicted prices
results = pd.DataFrame({
    "Actual Price": y_test_inv,
    "Predicted Price": y_pred_inv
}, index=y_test.index)

print("\nLast 10 predictions:")
print(results.tail(10).round(2))

# STEP 10: Visualization
plt.figure(figsize=(12, 6))
plt.plot(results["Actual Price"].values[:100], label="Actual Price", alpha=0.7)
plt.plot(results["Predicted Price"].values[:100], label="Predicted Price", alpha=0.7)
plt.title("Used Car Prices: Actual vs SVR Predicted (Sample of 100)")
plt.xlabel("Sample Index")
plt.ylabel("Price ($)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()