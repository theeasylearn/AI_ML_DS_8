import os
import kagglehub
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# =====================================================================
# 1. DOWNLOAD & LOAD KAGGLE DATASET
# =====================================================================
# Kaggle: aljarah/xapi-edu-data (Students' Academic Performance Dataset)
path = kagglehub.dataset_download("aljarah/xapi-edu-data")
print(path)
# exit(1)

#data set 
df = pd.read_csv(path + "/xAPI-Edu-Data.csv")

# =====================================================================
# 2. FEATURE SELECTION & TARGET MAPPING
# =====================================================================
# Map academic class tiers to early-alert status:
# 'L' (Low-Level: 0-69)   -> 'At Risk'
# 'M' (Middle-Level: 70-89) -> 'Moderate'
# 'H' (High-Level: 90-100) -> 'On Track'
status_mapping = {
    "L": "At Risk",
    "M": "Moderate",
    "H": "On Track"
}
df["Risk_Alert"] = df["Class"].map(status_mapping)

# Continuous behavioral and LMS engagement metrics
continuous_features = [
    "raisedhands",        # Classroom questions / hand raises (0-100)
    "VisITedResources",   # LMS course content visits (0-100)
    "AnnouncementsView",  # Course announcement checks (0-100)
    "Discussion"          # Discussion forum participation (0-100)
]

X = df[continuous_features]
y = df["Risk_Alert"]

# Split 75% training, 25% testing with stratification to preserve class balance
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

# =====================================================================
# 3. TRAIN GAUSSIAN NAIVE BAYES
# =====================================================================
gnb = GaussianNB()
gnb.fit(X_train, y_train)

# =====================================================================
# 4. EVALUATION & METRICS
# =====================================================================
y_pred = gnb.predict(X_test)
score = accuracy_score(y_test, y_pred)

print("=== Model Performance ===")
print(f"Test Accuracy: {score * 100:.2f}%\n")
print("Classification Report:")
print(classification_report(y_test, y_pred))

# exit(1)
# =====================================================================
# 5. INSPECT LEARNED GAUSSIAN PARAMETERS (mu & sigma^2)
# =====================================================================
classes = gnb.classes_

means_df = pd.DataFrame(gnb.theta_, index=classes, columns=continuous_features)
vars_df = pd.DataFrame(gnb.var_, index=classes, columns=continuous_features)

print("=== Learned Means (mu) per Risk Category ===")
print(means_df.round(2))
print("\n=== Learned Variances (sigma^2) per Risk Category ===")
print(vars_df.round(2))

# =====================================================================
# 6. VISUALIZATION 1: CONFUSION MATRIX
# =====================================================================
cm = confusion_matrix(y_test, y_pred, labels=classes)

plt.figure(figsize=(7, 5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Purples",
            xticklabels=classes, yticklabels=classes)
plt.title("Study Risk Alert: Confusion Matrix", fontsize=12, fontweight="bold")
plt.xlabel("Predicted Status")
plt.ylabel("Actual Status")
plt.tight_layout()
plt.show()

# =====================================================================
# 7. VISUALIZATION 2: GAUSSIAN BELL CURVES (VisITedResources)
# =====================================================================
# Demonstrates how the model calculates P(x | Risk Level)
feature_to_plot = "VisITedResources"
feature_idx = continuous_features.index(feature_to_plot)

plt.figure(figsize=(9, 5))
x_vals = np.linspace(0, 100, 500)
colors = {"At Risk": "#d9534f", "Moderate": "#f0ad4e", "On Track": "#5cb85c"}

for i, class_label in enumerate(classes):
    mu = gnb.theta_[i, feature_idx]
    sigma = np.sqrt(gnb.var_[i, feature_idx])
    
    # Gaussian Probability Density Function
    pdf = norm.pdf(x_vals, loc=mu, scale=sigma)
    
    color = colors.get(class_label, "blue")
    plt.plot(x_vals, pdf, label=f"{class_label} (μ={mu:.1f}, σ={sigma:.1f})", 
             color=color, linewidth=2.2)
    plt.fill_between(x_vals, 0, pdf, color=color, alpha=0.15)

plt.title(f"Learned Gaussian Distribution: '{feature_to_plot}' Across Risk Levels", 
          fontsize=12, fontweight="bold")
plt.xlabel("LMS Resource Visits (Count / Index)")
plt.ylabel("Probability Density P(x | Class)")
plt.legend(frameon=True)
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

# =====================================================================
# 8. EARLY ALERT INFERENCE ENGINE (REAL-TIME RISK CHECK)
# =====================================================================
# Simulated incoming week-4 telemetry for two distinct students:
sample_students = pd.DataFrame([
    {
        "Student": "Student A (Low Activity)",
        "raisedhands": 10,
        "VisITedResources": 12,
        "AnnouncementsView": 5,
        "Discussion": 8
    },
    {
        "Student": "Student B (High Activity)",
        "raisedhands": 75,
        "VisITedResources": 82,
        "AnnouncementsView": 60,
        "Discussion": 70
    }
])

features_only = sample_students[continuous_features]
predictions = gnb.predict(features_only)
probabilities = gnb.predict_proba(features_only)

print("\n=== Early Alert Decision Engine Output ===")
for i, row in sample_students.iterrows():
    print(f"\nProfile: {row['Student']}")
    print(f"Predicted Early-Alert Category: >>> {predictions[i]} <<<")
    print("Posterior Probabilities:")
    for class_name, prob in zip(classes, probabilities[i]):
        print(f"  - P({class_name:8s} | Activity): {prob * 100:.2f}%")