# Filter extreme data-entry outliers in Price ($500 to $200,000) and Mileage (<= 1,000,000 km)
print(f"After outlier removal: {df.shape}") # (9235, 16)

# ==========================================
# 3. Binary Mapping (2-Class Features -> 0/1)
# ==========================================
# Note: 'Turbo' is already mapped to 0/1 in Step 2
df['Leather interior'] = df['Leather interior'].map({'Yes': 1, 'No': 0})
df['Wheel'] = df['Wheel'].map({'Left wheel': 0, 'Right-hand drive': 1})

# ==========================================
# 4. Base-2 Binary Encoding (High-Cardinality)
# ==========================================
# Option A: Native NumPy bitwise implementation (No external library required)
# Compresses the 45 remaining unique Manufacturers into 6 binary columns
manufacturers = {val: idx + 1 for idx, val in enumerate(df['Manufacturer'].unique())}
m_codes = df['Manufacturer'].map(manufacturers).to_numpy(dtype=int)
n_bits = int(np.ceil(np.log2(len(manufacturers) + 1)))

for bit in range(n_bits):
    df[f'Manufacturer_bin_{bit}'] = (m_codes >> bit) & 1

df = df.drop(columns=['Manufacturer'])

# Option B: If you prefer using the `category_encoders` library (pip install category_encoders):
# import category_encoders as ce
# bin_encoder = ce.BinaryEncoder(cols=['Manufacturer'])
# df = bin_encoder.fit_transform(df)

# ==========================================
# 5. One-Hot Encoding (Nominal Categories) string
# ==========================================
ohe_cols = ['Gear box type', 'Drive wheels', 'Fuel type', 'Category', 'Color']
df = pd.get_dummies(df, columns=ohe_cols, drop_first=True, dtype=int)
print(f"Final preprocessed shape ready for SVR: {df.shape}") # (9235, 50)

# ==========================================
# 6. Train-Test Split, Scaling & SVR Training
# ==========================================
X = df.drop(columns=['Price'])
# Log-transform target to prevent high-price cars from dominating SVR loss
y = np.log1p(df['Price'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale only the continuous numerical features (leave binary/OHE columns as 0/1)
num_cols = ['Levy', 'Prod. year', 'Engine volume', 'Mileage', 'Cylinders', 'Airbags']
scaler = StandardScaler()

X_train[num_cols] = scaler.fit_transform(X_train[num_cols])
X_test[num_cols] = scaler.transform(X_test[num_cols])

# Fit Support Vector Regression (RBF Kernel)
svr = SVR(kernel='rbf', C=5.0, epsilon=0.1)
svr.fit(X_train, y_train)

# ==========================================
# 7. Predictions & Evaluation
# ==========================================
y_pred_log = svr.predict(X_test)

# Inverse log transformation to evaluate in actual Dollar ($) terms
y_pred_actual = np.expm1(y_pred_log)
y_test_actual = np.expm1(y_test)

print("\n--- SVR Model Performance ---")
print(f"R² Score (Log Price):    {r2_score(y_test, y_pred_log):.4f}")
print(f"RMSE (Log Price):        {np.sqrt(mean_squared_error(y_test, y_pred_log)):.4f}")
print(f"R² Score (Actual Price): {r2_score(y_test_actual, y_pred_actual):.4f}")
print(f"MAE (Actual Price):      ${mean_absolute_error(y_test_actual, y_pred_actual):,.2f}")
print(f"RMSE (Actual Price):     ${np.sqrt(mean_squared_error(y_test_actual, y_pred_act