# SVM Classification: Mobile Money Fraud Detection (Corrected Pipeline)
# Dataset: Kaggle PaySim1

import kagglehub
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt

from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import (
    confusion_matrix, 
    precision_score, 
    recall_score, 
    f1_score, 
    average_precision_score,
    ConfusionMatrixDisplay
)

# 1. Download the Kaggle dataset
print("Downloading dataset...")
path = kagglehub.dataset_download("ealaxi/paysim1")
print("Dataset downloaded successfully!")

# 2. Load the CSV file
df = pd.read_csv(path + "/PS_20174392719_1491204439457_log.csv")
print(f"\nOriginal Dataset shape: {df.shape}")

# 3. FILTER NOISE: Keep only transaction types where fraud actually occurs
# Using .copy() prevents Pandas SettingWithCopyWarning during feature engineering
df = df.loc[(df['type'] == 'TRANSFER') | (df['type'] == 'CASH_OUT')].copy()
print(f"Filtered Dataset shape: {df.shape}")

# 4. LABEL ENCODING
encoder = LabelEncoder()
df['type_encoded'] = encoder.fit_transform(df['type'])

# 5. NON-LINEAR FEATURE ENGINEERING (Designed for LinearSVC)
print("\nEngineering non-linear fraud indicator features...")

# Feature 1: Exact account liquidation (1 if transaction empties the exact positive balance)
df['is_account_drained'] = (
    (df['amount'] == df['oldbalanceOrg']) & 
    (df['newbalanceOrig'] == 0) & 
    (df['amount'] > 0)
).astype(int)

# Feature 2: Zero-balance mule account anomaly (destination stays 0 despite a transfer)
df['is_dest_zero_anomaly'] = (
    (df['oldbalanceDest'] == 0) & 
    (df['newbalanceDest'] == 0) & 
    (df['amount'] > 0)
).astype(int)

# Feature 3: Ratio of transaction amount to starting balance
# Clipped at 10.0 so zero-balance accounts do not create million-scale outliers that distort StandardScaler
df['amount_to_balance_ratio'] = np.clip(
    df['amount'] / (df['oldbalanceOrg'] + 1.0), 0.0, 10.0
)

# 6. PREPARE X and y
X = df.drop(['isFraud', 'isFlaggedFraud', 'nameOrig', 'nameDest', 'type'], axis=1)
y = df["isFraud"]
feature_names = X.columns.tolist()

print("\nFirst five rows of feature matrix X:")
print(X.head())

# 7. SPLIT DATA FIRST (Prevents Test Set Data Leakage)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# 8. SCALE FEATURES (Fit strictly on X_train, then transform both)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 9. CREATE AND TRAIN MODEL
# A moderate penalty weight (1:10) works well once strong non-linear indicators are present
model = LinearSVC(class_weight={0: 1, 1: 10}, random_state=42)

print("\nTraining SVM model...")
start_time = dt.now()
model.fit(X_train, y_train)
print(f"Training completed in {dt.now() - start_time}!")

# 10. EVALUATE METRICS
y_pred = model.predict(X_test)
y_scores = model.decision_function(X_test)

precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
pr_auc = average_precision_score(y_test, y_scores)

cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm.ravel()

# 11. PRINT RESULTS
print("\n=== Non-Linear Feature SVM Performance on PaySim1 ===")
print(f"Precision: {precision:.4f} (When it flags fraud, it is correct {precision*100:.2f}% of the time)")
print(f"Recall:    {recall:.4f} (It caught {recall*100:.2f}% of all actual fraud)")
print(f"F1-Score:  {f1:.4f}")
print(f"PR-AUC:    {pr_auc:.4f}")
print("-" * 53)
print("Confusion Matrix Breakdown:")
print(f"True Negatives (Legitimate, Allowed): {tn}")
print(f"False Positives (Legitimate, Blocked): {fp} <- Customer Friction")
print(f"False Negatives (Fraud, Missed):      {fn} <- Financial Loss")
print(f"True Positives (Fraud, Caught):       {tp}")

# 12. VISUALIZE CONFUSION MATRIX & FEATURE WEIGHTS
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Confusion Matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Normal", "Fraud"])
disp.plot(cmap="Blues", values_format="d", ax=axes[0], colorbar=False)
axes[0].set_title("Fraud Detection Confusion Matrix")

# Plot 2: Signed SVM Coefficients
weights = model.coef_[0]
feature_importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Weight': weights,
    'Abs_Weight': np.abs(weights)
}).sort_values(by='Abs_Weight', ascending=True)

axes[1].barh(feature_importance_df['Feature'], feature_importance_df['Weight'], color='steelblue')
axes[1].axvline(0, color='black', linewidth=0.8, linestyle='--')
axes[1].set_xlabel('Signed Coefficient Weight (Standardized)')
axes[1].set_title('LinearSVC Feature Weights')
axes[1].grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()