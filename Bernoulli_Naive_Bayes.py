# Bernoulli Naive Bayes
import os
import time
import kagglehub
import numpy as np
import pandas as pd
from scipy.sparse import hstack, csr_matrix
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    average_precision_score,
    confusion_matrix,
    classification_report
)

# ==========================================
# 1. AUTOMATICALLY DOWNLOAD DATASET
# ==========================================
print("Downloading dataset via kagglehub...")
dataset_path = kagglehub.dataset_download("shivamb/real-or-fake-fake-jobposting-prediction")
csv_file = os.path.join(dataset_path, "fake_job_postings.csv")

df = pd.read_csv(csv_file)
print(f"Dataset loaded successfully: {df.shape[0]} rows, {df.shape[1]} columns\n")

# ==========================================
# 2. FEATURE ENGINEERING (TEXT + BINARY FLAGS)
# ==========================================
text_cols = ["title", "company_profile", "description", "requirements", "benefits"]
df[text_cols] = df[text_cols].fillna("")

df["full_text"] = (
    df["title"] + " " +
    df["company_profile"] + " " +
    df["description"] + " " +
    df["requirements"] + " " +
    df["benefits"]
)

# Native binary (0/1) metadata flags
df["has_salary"] = df["salary_range"].notnull().astype(int)
binary_cols = ["telecommuting", "has_company_logo", "has_questions", "has_salary"]

X_text = df["full_text"]
X_meta = df[binary_cols].values
y = df["fraudulent"]  # 0 = Real, 1 = Fake

# ==========================================
# 3. STRATIFIED TRAIN-TEST SPLIT
# ==========================================
X_text_train, X_text_test, X_meta_train, X_meta_test, y_train, y_test = train_test_split(
    X_text, X_meta, y, test_size=0.2, random_state=42, stratify=y
)

# ==========================================
# 4. BINARY TEXT VECTORIZATION (0/1 PRESENCE)
# ==========================================
vectorizer = CountVectorizer(
    binary=True,         # Strict 0/1 presence/absence required for BernoulliNB
    stop_words="english",
    max_features=5000,
    ngram_range=(1, 2)
)

X_text_train_bin = vectorizer.fit_transform(X_text_train)
X_text_test_bin = vectorizer.transform(X_text_test)

# Combine sparse binary text matrix with binary metadata columns
X_train_final = hstack([X_text_train_bin, csr_matrix(X_meta_train)])
X_test_final = hstack([X_text_test_bin, csr_matrix(X_meta_test)])

# ==========================================
# 5. TRAIN BERNOULLI NAIVE BAYES (WITH TIMING)
# ==========================================
model = BernoulliNB(alpha=1.0)

train_start = time.perf_counter()
model.fit(X_train_final, y_train)
train_time = time.perf_counter() - train_start

# ==========================================
# 6. ALGORITHM EFFICIENCY & ACCURACY CHECKS
# ==========================================
# Time the prediction speed on the test set
pred_start = time.perf_counter()
y_test_pred = model.predict(X_test_final)
pred_time = time.perf_counter() - pred_start

y_train_pred = model.predict(X_train_final)
y_test_prob = model.predict_proba(X_test_final)[:, 1]

# Calculate Core Accuracy & Error Metrics
train_acc = accuracy_score(y_train, y_train_pred)
test_acc = accuracy_score(y_test, y_test_pred)
bal_acc = balanced_accuracy_score(y_test, y_test_pred)
precision = precision_score(y_test, y_test_pred)
recall = recall_score(y_test, y_test_pred)
f1 = f1_score(y_test, y_test_pred)
roc_auc = roc_auc_score(y_test, y_test_prob)
pr_auc = average_precision_score(y_test, y_test_prob)

# Extract Confusion Matrix components: TN, FP, FN, TP
tn, fp, fn, tp = confusion_matrix(y_test, y_test_pred).ravel()
specificity = tn / (tn + fp)  # True Negative Rate (Real jobs correctly identified)
fpr = fp / (fp + tn)          # False Positive Rate (False alarm rate)

# 5-Fold Cross-Validation Accuracy & F1
cv_acc = cross_val_score(model, X_train_final, y_train, cv=5, scoring="accuracy").mean()
cv_f1 = cross_val_score(model, X_train_final, y_train, cv=5, scoring="f1").mean()

print("=" * 60)
print("       ALGORITHM EFFICIENCY & ACCURACY REPORT")
print("=" * 60)
print("1. COMPUTATIONAL SPEED (EFFICIENCY):")
print(f"   - Training Time (14,304 samples) : {train_time * 1000:.2f} ms")
print(f"   - Inference Time (3,576 samples) : {pred_time * 1000:.2f} ms")
print(f"   - Prediction Throughput          : {len(y_test) / pred_time:,.0f} postings/sec\n")

print("2. ACCURACY & OVERFITTING CHECK:")
print(f"   - Training Accuracy              : {train_acc * 100:.2f}%")
print(f"   - Testing Accuracy               : {test_acc * 100:.2f}%")
print(f"   - 5-Fold Cross-Val Accuracy      : {cv_acc * 100:.2f}%")
print(f"   - Balanced Accuracy (Imbalance)  : {bal_acc * 100:.2f}%")
print(f"   - Overfitting Gap (Train - Test) : {(train_acc - test_acc) * 100:.2f}%\n")

print("3. FRAUD DETECTION EFFECTIVENESS (CLASS 1 METRICS):")
print(f"   - Precision (Flagged truly fake) : {precision * 100:.2f}%")
print(f"   - Recall / Sensitivity (Caught)  : {recall * 100:.2f}%")
print(f"   - Specificity (Real jobs passed) : {specificity * 100:.2f}%")
print(f"   - F1-Score (Harmonic Mean)       : {f1 * 100:.2f}% (5-Fold CV: {cv_f1 * 100:.2f}%)")
print(f"   - ROC-AUC Score                  : {roc_auc:.4f}")
print(f"   - Precision-Recall AUC (PR-AUC)  : {pr_auc:.4f}\n")

print("4. CONFUSION MATRIX BREAKDOWN:")
print(f"   - True Negatives (Real -> Real)  : {tn}")
print(f"   - False Positives (False Alarms) : {fp} (FPR: {fpr * 100:.2f}%)")
print(f"   - False Negatives (Missed Scams) : {fn}")
print(f"   - True Positives (Caught Scams)  : {tp}")
print("=" * 60)

print("\n--- Detailed Sklearn Classification Report ---")
print(classification_report(y_test, y_test_pred, target_names=["Real (0)", "Fake (1)"]))

# ==========================================
# 7. CUSTOM JOB POSTING PREDICTION FUNCTION
# ==========================================
def predict_job_posting(
    title: str,
    description: str,
    company_profile: str = "",
    requirements: str = "",
    benefits: str = "",
    telecommuting: int = 0,
    has_company_logo: int = 0,
    has_questions: int = 0,
    has_salary: int = 0,
    threshold: float = 0.5
):
    combined_text = f"{title} {company_profile} {description} {requirements} {benefits}"
    text_features = vectorizer.transform([combined_text])
    meta_features = csr_matrix([[telecommuting, has_company_logo, has_questions, has_salary]])
    combined_features = hstack([text_features, meta_features])
    
    fake_prob = model.predict_proba(combined_features)[0][1]
    verdict = "FAKE / SCAM" if fake_prob >= threshold else "REAL / LEGITIMATE"
    
    print("-" * 55)
    print(f"Job Title        : {title}")
    print(f"Fraud Probability: {fake_prob * 100:.2f}% (Threshold: {threshold * 100:.0f}%)")
    print(f"Verdict          : {verdict}")
    print("-" * 55)
    return fake_prob

# ==========================================
# 8. TEST WITH SAMPLE REAL & FAKE POSTINGS
# ==========================================
print("\nTesting Custom Job Postings:")

predict_job_posting(
    title="Urgent Work From Home Data Entry Clerk - Earn $3500/Week",
    description="Immediate start! No experience required. Earn daily cash payouts from home processing simple forms. Send bank details for direct wire transfer setup.",
    requirements="Must have internet access and basic typing skills.",
    benefits="Daily cash bonuses, flexible hours.",
    telecommuting=1,
    has_company_logo=0,
    has_questions=0,
    has_salary=1
)

predict_job_posting(
    title="Senior Python Backend Engineer",
    description="We are looking for an experienced backend engineer to design scalable REST APIs, optimize PostgreSQL queries, and maintain CI/CD pipelines.",
    company_profile="Founded in 2016, CloudScale builds enterprise infrastructure monitoring tools.",
    requirements="4+ years of experience with Python, Django or FastAPI, Docker, and AWS.",
    benefits="Health insurance, 401(k) matching, annual learning stipend.",
    telecommuting=0,
    has_company_logo=1,
    has_questions=1,
    has_salary=1
)