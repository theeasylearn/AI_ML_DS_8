import pandas as pd
import matplotlib.pyplot as plt
#dataset 
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
    roc_curve,
    roc_auc_score
)

# ============================================================
# 1. Load Dataset
# ============================================================
patient = load_breast_cancer()

#define x (data) and y (target)
X  = pd.DataFrame(patient.data,columns=patient.feature_names)
# print(X.shape)
# print(X)
Y = pd.Series(patient.target,name="target")
# print(Y)
# exit(1)
#split data into training and testing
list = train_test_split(X,Y,train_size=0.80,test_size=0.20,random_state=42,stratify=Y)
x_train = list[0] # list has train data for at 0th position
x_test = list[1]  # list has test data for at 1st position
y_train = list[2] # list has y train target for at 2nd position
y_test = list[3] # list has y test target for at 3rd position

#use scaler 
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.fit_transform(x_test)

#create model 
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train,y_train)
y_predict = knn.predict(x_test)

accuracy = accuracy_score(y_test,y_predict)

# Original:
# 0 = malignant
# 1 = benign

# Medical interpretation:
# 1 = malignant
# 0 = benign

y_test_medical  = (y_test == 0).astype(int)
y_pred_medical = (y_predict == 0).astype(int)


# ============================================================
# 8. Confusion Matrix
# ============================================================
cm = confusion_matrix(
    y_test_medical,
    y_pred_medical
)
TN, FP, FN, TP = cm.ravel()
# ============================================================
# 9. Precision
# ============================================================
precision = precision_score(
    y_test_medical,
    y_pred_medical
)
# ============================================================
# 10. Recall
# ============================================================

recall = recall_score(
    y_test_medical,
    y_pred_medical
)


# ============================================================
# 11. F1 Score
# ============================================================

f1 = f1_score(
    y_test_medical,
    y_pred_medical
)


# ============================================================
# 12. Specificity
# ============================================================

specificity = TN / (TN + FP)


# ============================================================
# 13. ROC and AUC
# ============================================================

# Probability of malignant class
y_probability = knn.predict_proba(x_test_scaled)[:, 0]

fpr, tpr, thresholds = roc_curve(
    y_test_medical,
    y_probability
)

auc = roc_auc_score(
    y_test_medical,
    y_probability
)
# ============================================================
# 14. Print Results
# ============================================================
print("\n========================================")
print("   BREAST CANCER KNN MODEL RESULTS")
print("========================================")
print(f"Accuracy    : {accuracy:.4f}")
print(f"Precision   : {precision:.4f}")
print(f"Recall      : {recall:.4f}")
print(f"F1 Score    : {f1:.4f}")
print(f"Specificity : {specificity:.4f}")
print(f"AUC         : {auc:.4f}")

print("\nConfusion Matrix:")
print(cm)

print("\nConfusion Matrix Values:")
print("True Negative :", TN)
print("False Positive:", FP)
print("False Negative:", FN)
print("True Positive :", TP)


# ============================================================
# 15. Plot ROC Curve
# ============================================================

plt.figure(figsize=(8, 6))

plt.plot(
    fpr,
    tpr,
    label=f"KNN (AUC = {auc:.3f})"
)

plt.plot(
    [0, 1],
    [0, 1],
    linestyle="--",
    label="Random Classifier"
)

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title(
    "ROC Curve - Breast Cancer Diagnosis using KNN"
)
plt.legend()
plt.grid()
plt.show()