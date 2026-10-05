# develop model using decision tree to decide whether loan will be approval or rejected.

import kagglehub
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np
# --------------------------------------------------
# 1. Download dataset from Kaggle
# --------------------------------------------------
path = kagglehub.dataset_download(
    "architsharma01/loan-approval-prediction-dataset"
)
# --------------------------------------------------
# 2. Load dataset
# --------------------------------------------------

df = pd.read_csv(path + "/loan_approval_dataset.csv")
# --------------------------------------------------
# 3. Clean column names
# --------------------------------------------------
df.columns = df.columns.str.strip()
# --------------------------------------------------
# 4. Convert categorical values into numbers
# --------------------------------------------------
# print("Before Categorical Encoding")
# print(df.head(10))
# input("Press any to continue")
df["education"] = df["education"].str.strip().map({
    "Graduate": 1,
    "Not Graduate": 0
})

df["self_employed"] = df["self_employed"].str.strip().map({
    "Yes": 1,
    "No": 0
})

df["loan_status"] = df["loan_status"].str.strip().map({
    "Approved": 1,
    "Rejected": 0
})
print("After Categorical Encoding")
# print(df.head(10))
# exit(1)
# --------------------------------------------------
# 5. Select input features
# --------------------------------------------------
X = df[
    [
        "no_of_dependents",
        "education",
        "self_employed",
        "income_annum",
        "loan_amount",
        "loan_term",
        "cibil_score",
        "residential_assets_value",
        "commercial_assets_value",
        "luxury_assets_value",
        "bank_asset_value"
    ]
]

# --------------------------------------------------
# 6. Select target
# --------------------------------------------------
y = df["loan_status"]
# --------------------------------------------------
# 7. Split data
# --------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)
# --------------------------------------------------
# 8. Create Decision Tree
# --------------------------------------------------
model = DecisionTreeClassifier(criterion="gini",random_state=42)
# --------------------------------------------------
# 9. Train model
# --------------------------------------------------
model.fit(X_train, y_train)
# --------------------------------------------------
# 10. Make prediction
# --------------------------------------------------
y_pred = model.predict(X_test)
# --------------------------------------------------
# 11. Check accuracy
# --------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Test data")
print(y_pred)
result = np.where(y_pred == 1, 'Approved', 'reject')
X_test['loan_status'] = result
with pd.ExcelWriter("output.xls", engine="openpyxl") as writer:
    X_test.to_excel(writer, sheet_name="Sheet1", index=False)
print('done....')