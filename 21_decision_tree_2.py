# develop model using decision tree for Health Insurance sector for Cross Sell Prediction .
#https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction?select=train.csv

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
    "anmolkumar/health-insurance-cross-sell-prediction"
)
# --------------------------------------------------
# 2. Load dataset
# --------------------------------------------------

df_train = pd.read_csv(path + "/train.csv")
df_test = pd.read_csv(path + "/test.csv")

df_train["Gender"] = df_train["Gender"].map({
    "Male": 1,
    "Female": 0
});

df_train["Vehicle_Damage"] = df_train["Vehicle_Damage"].map({
    "Yes": 1,
    "No": 0
});

df_train["Vehicle_Age"] = df_train["Vehicle_Age"].map({
    "1 Year": 0,
    "1-2 Year": 1,
    "> 2 Years": 2
});


df_test["Gender"] = df_test["Gender"].map({
    "Male": 1,
    "Female": 0
});

df_test["Vehicle_Damage"] = df_test["Vehicle_Damage"].map({
    "Yes": 1,
    "No": 0
});

df_test["Vehicle_Age"] = df_test["Vehicle_Age"].map({
    "1 Year": 0,
    "1-2 Year": 1,
    "> 2 Years": 2
});

X = df_train[
    [
    "Gender",
    "Age",	
    "Driving_License",	
    "Region_Code",
    "Previously_Insured",
    "Vehicle_Age",
    "Vehicle_Damage",
    "Annual_Premium",
    "Policy_Sales_Channel",
    "Vintage",
    ]
]

Y = df_train["Response"]
model = DecisionTreeClassifier(criterion="gini",random_state=42)
model.fit(X, Y)
X_test = df_test[
    [
    "Gender",
    "Age",	
    "Driving_License",	
    "Region_Code",
    "Previously_Insured",
    "Vehicle_Age",
    "Vehicle_Damage",
    "Annual_Premium",
    "Policy_Sales_Channel",
    "Vintage",
    ]
]
y_pred = model.predict(X_test)
print("Test data")
print(y_pred)
result = np.where(y_pred == 1, 'Yes', 'NO')
X_test['Response'] = result
with pd.ExcelWriter("output_2.xls", engine="openpyxl") as writer:
    X_test.to_excel(writer, sheet_name="Sheet1", index=False)
print('done....')
# print(df_train.head())
