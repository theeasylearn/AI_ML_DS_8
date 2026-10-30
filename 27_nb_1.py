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

# 1. Load dataset
path = kagglehub.dataset_download("aljarah/xapi-edu-data")
df = pd.read_csv(f"{path}/xAPI-Edu-Data.csv")

status_mapping = {"L": "At Risk", "M": "Moderate", "H": "On Track"}
df["Risk_Alert"] = df["Class"].map(status_mapping)

#this list contains only continuous numerical features
continuous_features = [
    "raisedhands", "VisITedResources", "AnnouncementsView", "Discussion"
]

categorical_features = [
    "StudentAbsenceDays", "ParentAnsweringSurvey",
    "ParentschoolSatisfaction", "Relation", "gender", "StageID", "Semester"
]

# X_cont contains only continuous numerical features
X_cont = df[continuous_features]
# X_cat contains only categorical features
X_cat = OrdinalEncoder().fit_transform(df[categorical_features])
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
exit(1)
