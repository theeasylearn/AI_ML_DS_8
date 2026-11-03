import kagglehub
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, accuracy_score, roc_auc_score

# 1. Load dataset
path = kagglehub.dataset_download("sergionefedov/will-this-order-come-back")
df = pd.read_csv(f"{path}/fashion_returns_master.csv")

# 2. Separate X and y — Also drop 'size_ordered' & 'size_usual' 
# because 'size_mismatch' already captures the exact size difference!
X = df.drop(columns=["order_id", "returned", "return_reason", "size_ordered", "size_usual"])
y = df["returned"]

# 3. Define column groups
continuous_columns = [
    "price_usd", "discount_pct", "size_mismatch", "customer_prior_orders",
    "customer_prior_return_rate", "avg_review_rating", "num_reviews", "days_to_delivery"
]

nominal_columns = ["category", "fabric", "marketplace_region", "device", "fit_type"]

binary_columns = [
    "ordered_multiple_sizes", "reviews_read", "size_chart_viewed",
    "model_shown", "return_shipping_free", "is_gift"
]

X[binary_columns] = X[binary_columns].astype(int)

# 4. Preprocessor: StandardScaler on continuous + OneHot on nominal + passthrough binary
preprocessor = ColumnTransformer(
    transformers=[
        ("ohe", OneHotEncoder(drop="first", sparse_output=False, handle_unknown="ignore"), nominal_columns),
        ("scaler", StandardScaler(), continuous_columns),
        ("binary", "passthrough", binary_columns)
    ]
)

# 5. Train / Test Split
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Scaling ALL columns to unit variance prevents low-variance 0/1 columns from distorting GaussianNB
model_max_acc = Pipeline([
    ("preprocessor", preprocessor),
    ("all_scaler", StandardScaler()), 
    ("nb", GaussianNB(var_smoothing=0.05)) # Uses true priors [0.719, 0.281] for max accuracy
])

model_max_acc.fit(x_train, y_train)
y_pred_acc = model_max_acc.predict(x_test)
y_prob_acc = model_max_acc.predict_proba(x_test)[:, 1]

print(f"Max-Accuracy Mode: {accuracy_score(y_test, y_pred_acc) * 100:.2f}%")
print(classification_report(y_test, y_pred_acc))