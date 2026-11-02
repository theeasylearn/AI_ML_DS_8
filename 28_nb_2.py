'''
Retail Store Product Return Likelihood (CategoricalNB)
Scenario: An e-commerce apparel store evaluates purchase checkout carts using categorical tags: Product Category (Footwear, Formal Wear, Casuals), Payment Method (Cash on Delivery, UPI/Card, Store Credit), Customer Loyalty Tier (New, Silver, Platinum), and Discount Code Used (None, Clearance, Seasonal).
Target: Flag return likelihood: Keep vs. Likely Return.
Key Exercise Concept: Comparing class priors $P(C)$ against class-conditional likelihoods to understand how payment methods skew return rates.
'''

import matplotlib.pyplot as plt
import seaborn as sns
import kagglehub
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.decomposition import PCA
from sklearn.naive_bayes import GaussianNB, CategoricalNB
from sklearn.metrics import classification_report, accuracy_score
# https://www.kaggle.com/datasets/sergionefedov/will-this-order-come-back?select=fashion_returns_master.csv
# 1. Load dataset
path = kagglehub.dataset_download("sergionefedov/will-this-order-come-back")
df = pd.read_csv(f"{path}/fashion_returns_master.csv")

# print(path)


df['device'] = df['device'].map({'desktop':1,'mobile':0})
df.drop(columns=["order_id", "returned", "return_reason"])

print(df.head())
exit(1)
'''
price_usd, discount_pct, size_mismatch ($\vert{}\text{ordered} - \text{usual}\vert{}$), customer_prior_orders, customer_prior_return_rate, avg_review_rating, num_reviews,    days_to_delivery
'''
#this list contains only continuous numerical features
continuous_columns = [
    "price_usd", "discount_pct", "size_mismatch", "customer_prior_orders",
    "customer_prior_return_rate", "avg_review_rating", "num_reviews", "days_to_delivery"
]

Nominal_columns =  ['category','fabric','marketplace_region','device']
Categorical_Columns = ["fit_type", "size_ordered","size_usual"]

# X_cont contains only continuous numerical features
X_cont = df[continuous_columns]
# X_cat contains only categorical features
X_cat = OrdinalEncoder().fit_transform(df[Categorical_Columns])
y = df["Risk_Alert"]
# print(X_cat.shape)
# exit(1)
# Stratified split matching your exact seed
X_continous_training, X_continous_testing, X_categorical_training, X_categorical_testing, y_train, y_test = train_test_split(
    X_cont, X_cat, y, test_size=0.25, random_state=42, stratify=y
)

# 2. Orthogonalize continuous features with PCA so GaussianNB independence holds
pca = PCA(whiten=True, random_state=42)

X_continous_training_pca = pca.fit_transform(X_continous_training)
X_continous_testing_pca = pca.transform(X_continous_testing)

# 3. Fit GaussianNB on continuous + CategoricalNB on discrete features
gnb = GaussianNB().fit(X_continous_training_pca, y_train)

cnb = CategoricalNB().fit(X_categorical_training, y_train)

# 4. Combine log-posteriors: log P(y|X_cont) + log P(y|X_cat) - log P(y)
log_priors = np.log(gnb.class_prior_)
combined_log_prob = (gnb.predict_log_proba(X_continous_testing_pca)
    + cnb.predict_log_proba(X_categorical_testing)
    - log_priors
)
y_pred_hybrid = gnb.classes_[np.argmax(combined_log_prob, axis=1)]

score = accuracy_score(y_test, y_pred_hybrid)
print("=== Hybrid Naive Bayes (PCA-GaussianNB + CategoricalNB) ===")
print(f"Test Accuracy: {score * 100:.2f}%\n")
print(classification_report(y_test, y_pred_hybrid))
# exit(1)
