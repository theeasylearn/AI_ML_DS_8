# ============================================================
# DECISION TREE REGRESSION
# House Price Prediction
# ============================================================


# ------------------------------------------------------------
# STEP 1: Install KaggleHub
# ------------------------------------------------------------

# Run this only once in Google Colab / Jupyter
# !pip install kagglehub


# ------------------------------------------------------------
# STEP 2: Import libraries
# ------------------------------------------------------------

# Used to download dataset from Kaggle
import kagglehub

# Used to work with datasets
import pandas as pd

# Used for mathematical calculations
import numpy as np

# Used to split data into training and testing data
from sklearn.model_selection import train_test_split

# Decision Tree Regression algorithm
from sklearn.tree import DecisionTreeRegressor

# Evaluation metrics
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


# ------------------------------------------------------------
# STEP 3: Download dataset from Kaggle
# ------------------------------------------------------------

path = kagglehub.dataset_download(
    "yasserh/housing-prices-dataset"
)
print("Dataset downloaded successfully!")
print("Dataset location:")
print(path)
# ------------------------------------------------------------
# STEP 4: Load the dataset
# ------------------------------------------------------------
df = pd.read_csv(path + "/Housing.csv")
# ------------------------------------------------------------
# STEP 5: Display the dataset
# ------------------------------------------------------------
print("\nFirst 5 rows:")
# print(df.head(10))
# ------------------------------------------------------------
# STEP 6: Display dataset information
# ------------------------------------------------------------

print("\nDataset Shape (row column):")
print(df.shape) 
print("\nColumn Names:")
print(df.columns)
print("\nDataset Information:")
# df.info()
# exit(1)
# ------------------------------------------------------------
# STEP 7: Check missing values
# ------------------------------------------------------------
print("\nMissing Values:")
print(df.isnull().sum())
# ------------------------------------------------------------
# STEP 8: Select input features
# ------------------------------------------------------------
# exit(1)
# We are using the following information
# to predict the house price.

X = df[
    [
        "area",
        "bedrooms",
        "bathrooms",
        "stories",
        "parking"
    ]
]
#---------------------------------------
# STEP 9: Select target/output
# ------------------------------------------------------------
# price is the value we want to predict.
y = df["price"]
# ------------------------------------------------------------
# STEP 10: Split dataset
# ------------------------------------------------------------
# 80% → Training data
# 20% → Testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)
print("\nTraining records:", len(X_train))
print("Testing records:", len(X_test))
# ------------------------------------------------------------
# STEP 11: Create Decision Tree Regressor
# ------------------------------------------------------------
model = DecisionTreeRegressor(criterion="squared_error",max_depth=11,random_state=42)
# ------------------------------------------------------------
# STEP 12: Train the model
# ------------------------------------------------------------
model.fit(X_train,y_train)
print("\nModel training completed!")
# ------------------------------------------------------------
# STEP 13: Make predictions
# ------------------------------------------------------------
y_pred = model.predict(X_test)
# ------------------------------------------------------------
# STEP 14: Display Actual vs Predicted prices
# ------------------------------------------------------------
result = pd.DataFrame({"Actual Price": y_test.values,"Predicted Price": y_pred})

# Format prices with commas
# Example:
# 6250000 → 6,250,000

result["Actual Price"] = result["Actual Price"].apply(lambda x: f"₹{x:,.0f}")
result["Predicted Price"] = result["Predicted Price"].apply(lambda x: f"₹{x:,.0f}")


print("\nActual vs Predicted Prices:")
print(result.head(20).to_string(index=False))
# exit(1)
# ------------------------------------------------------------
# STEP 15: Calculate MAE
# ------------------------------------------------------------
mae = mean_absolute_error(
    y_test,
    y_pred
)

print("\nMean Absolute Error (MAE):")
print(f"₹{mae:,.2f}")


# ------------------------------------------------------------
# STEP 16: Calculate MSE
# ------------------------------------------------------------

mse = mean_squared_error(
    y_test,
    y_pred
)

print("\nMean Squared Error (MSE):")
print(f"{mse:,.2f}")


# ------------------------------------------------------------
# STEP 17: Calculate RMSE
# ------------------------------------------------------------

rmse = np.sqrt(mse)

print("\nRoot Mean Squared Error (RMSE):")
print(f"₹{rmse:,.2f}")


# ------------------------------------------------------------
# STEP 18: Calculate R² Score
# ------------------------------------------------------------
r2 = r2_score(
    y_test,
    y_pred
)

print("\nR² Score:")
print(f"{r2:.4f}")

exit(1)
# ------------------------------------------------------------
# STEP 19: Predict price of a new house
# ------------------------------------------------------------

# New house information:
#
# Area       = 1500 sq.ft
# Bedrooms   = 3
# Bathrooms  = 2
# Stories    = 2
# Parking    = 1

new_house = [[
    1500,
    3,
    2,
    2,
    1
]]


# Make prediction
new_prediction = model.predict(
    new_house
)


# Display prediction
print("\n-----------------------------------")
print("NEW HOUSE PRICE PREDICTION")
print("-----------------------------------")

print(
    f"Predicted House Price: ₹{new_prediction[0]:,.0f}"
)