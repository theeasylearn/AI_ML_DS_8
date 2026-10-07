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

path = kagglehub.dataset_download("harlfoxem/housesalesprediction")

print("Dataset downloaded successfully!")
print("Dataset location:")
print(path)
# ------------------------------------------------------------
# STEP 4: Load the dataset
# ------------------------------------------------------------
df = pd.read_csv(path + "/kc_house_data.csv")
# ------------------------------------------------------------
# STEP 5: Display the dataset
# ------------------------------------------------------------
# print("\nFirst 5 rows:")
# print(df.head(10))
# ------------------------------------------------------------
# STEP 6: Display dataset information
# ------------------------------------------------------------

print("\nDataset Shape (row column):")
print(df.shape) 
print("\nColumn Names:")
print(df.columns)
# print("\nDataset Information:")
# df.info()
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

X = df.drop(['id', 'date', 'price'], axis=1)
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
# exit(1)

# ------------------------------------------------------------
# STEP 11: Create Decision Tree Regressor
# ------------------------------------------------------------
model = DecisionTreeRegressor(criterion="squared_error",max_depth=9,random_state=42)
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

path = kagglehub.dataset_download("harlfoxem/housesalesprediction")

print("Dataset downloaded successfully!")
print("Dataset location:")
print(path)
# ------------------------------------------------------------
# STEP 4: Load the dataset
# ------------------------------------------------------------
df = pd.read_csv(path + "/kc_house_data.csv")
# ------------------------------------------------------------
# STEP 5: Display the dataset
# ------------------------------------------------------------
# print("\nFirst 5 rows:")
# print(df.head(10))
# ------------------------------------------------------------
# STEP 6: Display dataset information
# ------------------------------------------------------------

print("\nDataset Shape (row column):")
print(df.shape) 
print("\nColumn Names:")
print(df.columns)
# print("\nDataset Information:")
# df.info()
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

X = df.drop(['id', 'date', 'price'], axis=1)
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
# exit(1)

# ------------------------------------------------------------
# STEP 11: Create Decision Tree Regressor
# ------------------------------------------------------------
model = DecisionTreeRegressor(criterion="squared_error",max_depth=9,random_state=42)
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
r2_test = r2_score(y_test, y_pred)

# Predict on training data to check for overfitting
y_train_pred = model.predict(X_train)
r2_train = r2_score(y_train, y_train_pred)

print("\nR² Scores:")
print(f"Training R² : {r2_train:.4f}")
print(f"Testing R²  : {r2_test:.4f}")
