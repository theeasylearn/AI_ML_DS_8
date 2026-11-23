
# ============================================================
# FAKE JOB POSTING DETECTION USING BERNOULLI NAIVE BAYES
# WITH FALSE POSITIVE REDUCTION
# NO PIPELINE - SAME ALGORITHM
# ============================================================

import os
import time
import kagglehub
import numpy as np
import pandas as pd

from scipy.sparse import hstack, csr_matrix

from sklearn.model_selection import (
    train_test_split,
    StratifiedKFold
)

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
    classification_report,
    roc_curve
)

# ============================================================
# 1. CONFIGURATION
# ============================================================
RANDOM_STATE = 42
TEST_SIZE = 0.20
VALIDATION_SIZE = 0.20
MAX_FEATURES = 5000
NGRAM_RANGE = (1, 2)
MIN_DF = 2
ALPHA = 1.0
# Minimum acceptable recall for fake jobs
MIN_RECALL = 0.85
DEFAULT_THRESHOLD = 0.50
TEXT_COLS = ["title","company_profile","description","requirements","benefits"]
BINARY_COLS = ["telecommuting","has_company_logo","has_questions","has_salary"]
start_time = time.time() #time when algorithm start
dataset_path = kagglehub.dataset_download("shivamb/real-or-fake-fake-jobposting-prediction")
file_path = os.path.join(dataset_path,"fake_job_postings.csv")
df = pd.read_csv(file_path)
print("Dataset loaded successfully:", df.shape)
# ============================================================
# 3. DATA PREPROCESSING
# ============================================================
# Fill missing text values
df[TEXT_COLS] = df[TEXT_COLS].fillna("")
#feature engineering
# Combine all text columns
df["full_text"] = (df["title"] + " " + df["company_profile"] + " " + df["description"] + " " + df["requirements"] + " " + df["benefits"])
# Salary availability flag
df["has_salary"] = (df["salary_range"].fillna("").astype(str).str.strip().ne("").astype(int))
X_text = df["full_text"]
X_meta = df[BINARY_COLS].values
# 0 = Real Job
# 1 = Fake Job
y = df["fraudulent"].astype(int)

# ============================================================
# 4. STRATIFIED TRAIN-VALIDATION-TEST SPLIT
# ============================================================

# First split:
# 80% train+validation, 20% test

X_text_trainval, X_text_test, X_meta_trainval, X_meta_test, y_trainval, y_test = train_test_split(X_text,X_meta,y,test_size=TEST_SIZE,random_state=RANDOM_STATE,stratify=y)

# Second split:
# 64% training, 16% validation, 20% testing

X_text_train, X_text_val, X_meta_train, X_meta_val, y_train, y_val = train_test_split( X_text_trainval, X_meta_trainval, y_trainval, test_size=VALIDATION_SIZE, random_state=RANDOM_STATE, stratify=y_trainval)

print("\nDATASET SPLIT")
print("=" * 60)
print("Training samples  :", len(y_train))
print("Validation samples:", len(y_val))
print("Testing samples   :", len(y_test))

# ============================================================
# 5. BINARY TEXT VECTORIZATION
# ============================================================
vectorizer = CountVectorizer(
    binary=True,
    stop_words="english",
    max_features=MAX_FEATURES,
    ngram_range=NGRAM_RANGE,
    min_df=MIN_DF
)

# Fit only on training data
X_text_train_bin = vectorizer.fit_transform(
    X_text_train
)

# Transform validation and test data
X_text_val_bin = vectorizer.transform(
    X_text_val
)

X_text_test_bin = vectorizer.transform(
    X_text_test
)

# Combine text features and metadata
X_train_final = hstack(
    [
        X_text_train_bin,
        csr_matrix(X_meta_train)
    ],
    format="csr"
)

X_val_final = hstack(
    [
        X_text_val_bin,
        csr_matrix(X_meta_val)
    ],
    format="csr"
)

X_test_final = hstack(
    [
        X_text_test_bin,
        csr_matrix(X_meta_test)
    ],
    format="csr"
)

print("\nFEATURE ENGINEERING")
print("=" * 60)

print("Text features:", len(vectorizer.vocabulary_))
print("Metadata features:", len(BINARY_COLS))
print("Total features:", X_train_final.shape[1])


# ============================================================
# 6. TRAIN BERNOULLI NAIVE BAYES
# ============================================================

print("\nTraining Bernoulli Naive Bayes...")

training_start = time.time()

model = BernoulliNB(
    alpha=ALPHA,
    binarize=0.0
)
model.fit(
    X_train_final,
    y_train
)
training_time = time.time() - training_start
print("Training completed.")
print(f"Training time: {training_time:.4f} seconds")


# ============================================================
# 7. AUTOMATIC THRESHOLD OPTIMIZATION
# ============================================================

print("\nOptimizing decision threshold...")

# Predict fake probabilities on validation data
y_val_prob = model.predict_proba(
    X_val_final
)[:, 1]

# ROC thresholds provide candidate decision boundaries.
# drop_intermediate=False checks all distinct boundaries.
fpr_values, tpr_values, thresholds = roc_curve(
    y_val,
    y_val_prob,
    drop_intermediate=False
)

total_real = int((y_val == 0).sum())
total_fake = int((y_val == 1).sum())

threshold_results = []

for i, threshold in enumerate(thresholds):

    recall = float(tpr_values[i])

    # Convert ROC rates into confusion matrix counts
    fp = int(round(fpr_values[i] * total_real))
    tp = int(round(recall * total_fake))

    tn = total_real - fp
    fn = total_fake - tp

    precision = (
        tp / (tp + fp)
        if (tp + fp) > 0
        else 0.0
    )

    f1 = (
        2 * precision * recall / (precision + recall)
        if (precision + recall) > 0
        else 0.0
    )

    threshold_results.append({
        "threshold": threshold,
        "tn": tn,
        "fp": fp,
        "fn": fn,
        "tp": tp,
        "precision": precision,
        "recall": recall,
        "f1": f1
    })

threshold_df = pd.DataFrame(threshold_results)

# Keep thresholds satisfying minimum fraud recall
valid_thresholds = threshold_df[
    threshold_df["recall"] >= MIN_RECALL
].copy()

if valid_thresholds.empty:
    raise ValueError(
        "No threshold satisfies the minimum recall."
    )

# Minimize FP.
# For equal FP values, prefer higher recall.
valid_thresholds = valid_thresholds.sort_values(
    by=["fp", "recall"],
    ascending=[True, False]
)

best_row = valid_thresholds.iloc[0]

best_threshold = float(best_row["threshold"])

print("\nOPTIMAL THRESHOLD REPORT")
print("=" * 60)

print(f"Default threshold     : {DEFAULT_THRESHOLD:.6f}")
print(f"Optimized threshold   : {best_threshold:.6f}")
print(f"Required minimum recall: {MIN_RECALL * 100:.2f}%")

print(f"Validation FP         : {int(best_row['fp'])}")
print(f"Validation FN         : {int(best_row['fn'])}")
print(f"Validation TP         : {int(best_row['tp'])}")
print(f"Validation Precision  : {best_row['precision'] * 100:.2f}%")
print(f"Validation Recall     : {best_row['recall'] * 100:.2f}%")
print(f"Validation F1         : {best_row['f1'] * 100:.2f}%")


# ============================================================
# 8. PREDICTIONS WITH BOTH THRESHOLDS
# ============================================================

y_train_prob = model.predict_proba(
    X_train_final
)[:, 1]

y_test_prob = model.predict_proba(
    X_test_final
)[:, 1]

# Default predictions
y_test_pred_default = (
    y_test_prob >= DEFAULT_THRESHOLD
).astype(int)

# Optimized predictions
y_test_pred = (
    y_test_prob >= best_threshold
).astype(int)

y_train_pred = (
    y_train_prob >= best_threshold
).astype(int)


# ============================================================
# 9. PERFORMANCE EVALUATION FUNCTION
# ============================================================

def evaluate_model(
    y_true,
    y_pred,
    y_prob,
    title
):

    tn, fp, fn, tp = confusion_matrix(
        y_true,
        y_pred,
        labels=[0, 1]
    ).ravel()

    accuracy = accuracy_score(y_true, y_pred)

    balanced_acc = balanced_accuracy_score(
        y_true,
        y_pred
    )

    precision = precision_score(
        y_true,
        y_pred,
        zero_division=0
    )

    recall = recall_score(
        y_true,
        y_pred,
        zero_division=0
    )

    f1 = f1_score(
        y_true,
        y_pred,
        zero_division=0
    )

    specificity = (
        tn / (tn + fp)
        if (tn + fp) > 0
        else 0
    )

    fpr = (
        fp / (fp + tn)
        if (fp + tn) > 0
        else 0
    )

    roc_auc = roc_auc_score(
        y_true,
        y_prob
    )

    pr_auc = average_precision_score(
        y_true,
        y_prob
    )

    print("\n" + "=" * 65)
    print(title)
    print("=" * 65)

    print("\nACCURACY METRICS")
    print(f"Accuracy             : {accuracy * 100:.2f}%")
    print(f"Balanced Accuracy    : {balanced_acc * 100:.2f}%")

    print("\nFRAUD DETECTION METRICS")
    print(f"Precision            : {precision * 100:.2f}%")
    print(f"Recall / Sensitivity : {recall * 100:.2f}%")
    print(f"Specificity          : {specificity * 100:.2f}%")
    print(f"F1 Score             : {f1 * 100:.2f}%")
    print(f"ROC-AUC              : {roc_auc:.4f}")
    print(f"Average Precision    : {pr_auc:.4f}")

    print("\nCONFUSION MATRIX")
    print(f"True Negatives       : {tn}")
    print(f"False Positives      : {fp}")
    print(f"False Negatives      : {fn}")
    print(f"True Positives       : {tp}")
    print(f"False Positive Rate  : {fpr * 100:.2f}%")

    print("\nCLASSIFICATION REPORT")
    print(
        classification_report(
            y_true,
            y_pred,
            labels=[0, 1],
            target_names=["Real (0)", "Fake (1)"],
            zero_division=0
        )
    )

    return {
        "accuracy": accuracy,
        "balanced_accuracy": balanced_acc,
        "precision": precision,
        "recall": recall,
        "specificity": specificity,
        "f1": f1,
        "roc_auc": roc_auc,
        "average_precision": pr_auc,
        "tn": int(tn),
        "fp": int(fp),
        "fn": int(fn),
        "tp": int(tp),
        "fpr": fpr
    }


# ============================================================
# 10. EVALUATE DEFAULT THRESHOLD
# ============================================================

default_results = evaluate_model(
    y_test,
    y_test_pred_default,
    y_test_prob,
    "BERNOULLI NB - DEFAULT THRESHOLD (0.50)"
)


# ============================================================
# 11. EVALUATE OPTIMIZED THRESHOLD
# ============================================================

optimized_results = evaluate_model(
    y_test,
    y_test_pred,
    y_test_prob,
    f"BERNOULLI NB - OPTIMIZED THRESHOLD ({best_threshold:.6f})"
)


# ============================================================
# 12. COMPARE BEFORE AND AFTER OPTIMIZATION
# ============================================================

print("\n" + "=" * 70)
print("DEFAULT VS OPTIMIZED THRESHOLD COMPARISON")
print("=" * 70)

comparison = pd.DataFrame({
    "Metric": [
        "Accuracy (%)",
        "Balanced Accuracy (%)",
        "Precision (%)",
        "Recall (%)",
        "Specificity (%)",
        "F1 Score (%)",
        "False Positives",
        "False Negatives",
        "True Positives",
        "True Negatives"
    ],

    "Default": [
        default_results["accuracy"] * 100,
        default_results["balanced_accuracy"] * 100,
        default_results["precision"] * 100,
        default_results["recall"] * 100,
        default_results["specificity"] * 100,
        default_results["f1"] * 100,
        default_results["fp"],
        default_results["fn"],
        default_results["tp"],
        default_results["tn"]
    ],

    "Optimized": [
        optimized_results["accuracy"] * 100,
        optimized_results["balanced_accuracy"] * 100,
        optimized_results["precision"] * 100,
        optimized_results["recall"] * 100,
        optimized_results["specificity"] * 100,
        optimized_results["f1"] * 100,
        optimized_results["fp"],
        optimized_results["fn"],
        optimized_results["tp"],
        optimized_results["tn"]
    ]
})

comparison["Difference"] = (
    comparison["Optimized"] -
    comparison["Default"]
)

print(
    comparison.to_string(
        index=False,
        float_format=lambda x: f"{x:.2f}"
    )
)

fp_reduction = (
    default_results["fp"] -
    optimized_results["fp"]
)

if default_results["fp"] > 0:
    fp_reduction_percentage = (
        fp_reduction /
        default_results["fp"] * 100
    )
else:
    fp_reduction_percentage = 0.0

print("\nFALSE POSITIVE REDUCTION SUMMARY")
print("=" * 60)

print("Before optimization:", default_results["fp"])
print("After optimization :", optimized_results["fp"])
print("FP reduction       :", fp_reduction)

print(
    f"FP reduction (%)   : "
    f"{fp_reduction_percentage:.2f}%"
)

print(
    "Change in missed scams:",
    optimized_results["fn"] - default_results["fn"]
)


# ============================================================
# 13. TRAINING ACCURACY & OVERFITTING CHECK
# ============================================================

train_acc = accuracy_score(
    y_train,
    y_train_pred
)

test_acc = optimized_results["accuracy"]

overfitting_gap = (
    train_acc - test_acc
) * 100

print("\n" + "=" * 60)
print("TRAINING VS TESTING ACCURACY")
print("=" * 60)

print(f"Training Accuracy  : {train_acc * 100:.2f}%")
print(f"Testing Accuracy   : {test_acc * 100:.2f}%")
print(f"Overfitting Gap    : {overfitting_gap:.2f}%")


# ============================================================
# 14. 5-FOLD CROSS-VALIDATION
# ============================================================

# Cross-validation is performed only on training data.
# Vectorization is fitted independently inside each fold.
#
# These CV scores use the default threshold of 0.50.
# They are baseline CV metrics, not optimized-threshold CV.

print("\nRunning 5-Fold Cross-Validation...")

skf = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=RANDOM_STATE
)

cv_accuracy_scores = []
cv_f1_scores = []
cv_precision_scores = []
cv_recall_scores = []

# Reset indexes for fold-based selection
cv_text = X_text_train.reset_index(drop=True)
cv_y = y_train.reset_index(drop=True)
cv_meta = np.asarray(X_meta_train)

for fold, (train_idx, test_idx) in enumerate(
    skf.split(cv_text, cv_y),
    start=1
):

    fold_vectorizer = CountVectorizer(
        binary=True,
        stop_words="english",
        max_features=MAX_FEATURES,
        ngram_range=NGRAM_RANGE,
        min_df=MIN_DF
    )

    fold_text_train = fold_vectorizer.fit_transform(
        cv_text.iloc[train_idx]
    )

    fold_text_test = fold_vectorizer.transform(
        cv_text.iloc[test_idx]
    )

    fold_X_train = hstack(
        [
            fold_text_train,
            csr_matrix(cv_meta[train_idx])
        ],
        format="csr"
    )

    fold_X_test = hstack(
        [
            fold_text_test,
            csr_matrix(cv_meta[test_idx])
        ],
        format="csr"
    )

    fold_y_train = cv_y.iloc[train_idx]
    fold_y_test = cv_y.iloc[test_idx]

    fold_model = BernoulliNB(
        alpha=ALPHA
    )

    fold_model.fit(
        fold_X_train,
        fold_y_train
    )

    fold_pred = fold_model.predict(
        fold_X_test
    )

    cv_accuracy_scores.append(
        accuracy_score(fold_y_test, fold_pred)
    )

    cv_precision_scores.append(
        precision_score(
            fold_y_test,
            fold_pred,
            zero_division=0
        )
    )

    cv_recall_scores.append(
        recall_score(
            fold_y_test,
            fold_pred,
            zero_division=0
        )
    )

    cv_f1_scores.append(
        f1_score(
            fold_y_test,
            fold_pred,
            zero_division=0
        )
    )

    print(
        f"Fold {fold}: "
        f"Accuracy={cv_accuracy_scores[-1] * 100:.2f}% | "
        f"F1={cv_f1_scores[-1] * 100:.2f}%"
    )

print("\n5-FOLD CV REPORT (DEFAULT THRESHOLD)")
print("=" * 60)

print(
    f"Mean CV Accuracy  : "
    f"{np.mean(cv_accuracy_scores) * 100:.2f}%"
)

print(
    f"Mean CV Precision : "
    f"{np.mean(cv_precision_scores) * 100:.2f}%"
)

print(
    f"Mean CV Recall    : "
    f"{np.mean(cv_recall_scores) * 100:.2f}%"
)

print(
    f"Mean CV F1 Score  : "
    f"{np.mean(cv_f1_scores) * 100:.2f}%"
)


# ============================================================
# 15. CUSTOM JOB POSTING PREDICTION
# ============================================================

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
    threshold: float = None
):

    # Use optimized threshold by default
    if threshold is None:
        threshold = best_threshold

    if not 0 <= threshold <= 1:
        raise ValueError(
            "Threshold must be between 0 and 1."
        )

    combined_text = (
        f"{title} "
        f"{company_profile} "
        f"{description} "
        f"{requirements} "
        f"{benefits}"
    )

    # Transform text into binary features
    text_features = vectorizer.transform(
        [combined_text]
    )

    # Metadata must remain binary
    meta_values = [
        telecommuting,
        has_company_logo,
        has_questions,
        has_salary
    ]

    if any(value not in (0, 1) for value in meta_values):
        raise ValueError(
            "All metadata flags must be 0 or 1."
        )

    meta_features = csr_matrix(
        [meta_values]
    )

    combined_features = hstack(
        [
            text_features,
            meta_features
        ],
        format="csr"
    )

    # Predict fake probability
    fake_prob = model.predict_proba(
        combined_features
    )[0, 1]

    predicted_class = int(
        fake_prob >= threshold
    )

    verdict = (
        "FAKE / SCAM"
        if predicted_class == 1
        else "PREDICTED REAL"
    )

    print("\n" + "-" * 60)
    print("CUSTOM JOB POSTING PREDICTION")
    print("-" * 60)

    print(f"Job Title        : {title}")

    print(
        f"Fraud Score      : "
        f"{fake_prob * 100:.2f}%"
    )

    print(
        f"Decision Threshold: "
        f"{threshold * 100:.2f}%"
    )

    print(f"Predicted Class  : {predicted_class}")
    print(f"Verdict          : {verdict}")

    print("-" * 60)

    return {
        "title": title,
        "fraud_score": float(fake_prob),
        "predicted_class": predicted_class,
        "verdict": verdict,
        "threshold": threshold
    }


# ============================================================
# 16. TEST WITH SAMPLE FAKE JOB POSTING
# ============================================================

print("\nTesting Fake Job Example...")

predict_job_posting(
    title=(
        "Urgent Work From Home Data Entry Clerk "
        "- Earn $3500/Week"
    ),

    description=(
        "Immediate start! No experience required. "
        "Earn daily cash payouts from home processing "
        "simple forms. Send bank details for direct "
        "wire transfer setup."
    ),

    requirements=(
        "Must have internet access and "
        "basic typing skills."
    ),

    benefits=(
        "Daily cash bonuses, flexible hours."
    ),

    telecommuting=1,
    has_company_logo=0,
    has_questions=0,
    has_salary=1
)


# ============================================================
# 17. TEST WITH SAMPLE REAL JOB POSTING
# ============================================================

print("\nTesting Real Job Example...")

predict_job_posting(
    title="Senior Python Backend Engineer",

    description=(
        "We are looking for an experienced backend "
        "engineer to design scalable REST APIs, "
        "optimize PostgreSQL queries, and maintain "
        "CI/CD pipelines."
    ),

    company_profile=(
        "Founded in 2016, CloudScale builds "
        "enterprise infrastructure monitoring tools."
    ),

    requirements=(
        "4+ years of experience with Python, "
        "Django or FastAPI, Docker, and AWS."
    ),

    benefits=(
        "Health insurance, 401(k) matching, "
        "annual learning stipend."
    ),

    telecommuting=0,
    has_company_logo=1,
    has_questions=1,
    has_salary=1
)


# ============================================================
# 18. FINAL EXECUTION SUMMARY
# ============================================================

total_time = time.time() - start_time

print("\n" + "=" * 70)
print("FINAL BERNOULLI NAIVE BAYES PERFORMANCE SUMMARY")
print("=" * 70)

print(f"Algorithm             : Bernoulli Naive Bayes")
print(f"Alpha                 : {ALPHA}")
print(f"Total Features        : {X_train_final.shape[1]}")

print(f"Default Threshold     : {DEFAULT_THRESHOLD:.6f}")
print(f"Optimized Threshold   : {best_threshold:.6f}")

print(
    f"Test Accuracy         : "
    f"{optimized_results['accuracy'] * 100:.2f}%"
)

print(
    f"Test Precision        : "
    f"{optimized_results['precision'] * 100:.2f}%"
)

print(
    f"Test Recall           : "
    f"{optimized_results['recall'] * 100:.2f}%"
)

print(
    f"Test F1 Score         : "
    f"{optimized_results['f1'] * 100:.2f}%"
)

print(
    f"Test Specificity      : "
    f"{optimized_results['specificity'] * 100:.2f}%"
)

print(
    f"ROC-AUC               : "
    f"{optimized_results['roc_auc']:.4f}"
)

print(
    f"Average Precision     : "
    f"{optimized_results['average_precision']:.4f}"
)

print(
    f"False Positives       : "
    f"{optimized_results['fp']}"
)

print(
    f"False Negatives       : "
    f"{optimized_results['fn']}"
)

print(
    f"FP Reduction          : "
    f"{fp_reduction_percentage:.2f}%"
)

print(f"Training Time         : {training_time:.4f} seconds")
print(f"Total Execution Time  : {total_time:.4f} seconds")

print("=" * 70)
