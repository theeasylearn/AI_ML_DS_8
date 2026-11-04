import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix

# ==========================================
# STEP 1: Create Realistic UPI SMS Dataset
# ==========================================
data = [
    # Food & Dining
    ("Rs. 245 debited from A/c XX1234 to VPA zomato@hdfcbank for food order", "Food"),
    ("INR 180.00 paid to swiggy@icici via UPI Ref 41258963", "Food"),
    ("Debited Rs 540 to dominos pizza online order via UPI", "Food"),
    ("Rs 120 paid to burgerking@axisbank from A/c XX8899", "Food"),
    ("UPI payment of Rs 95 to tea post cafe snack bill", "Food"),
    ("Rs 310 debited to mcdonalds@yesbank for dinner", "Food"),

    # Travel & Commute
    ("Rs. 1450 debited to irctc@sbi for railway ticket booking", "Travel"),
    ("INR 210 paid to uber@axisbank for cab ride trip", "Travel"),
    ("Rs 85 debited to olacabs@icici auto ride commute", "Travel"),
    ("Paid Rs 650 to redbus@hdfcbank for bus ticket booking", "Travel"),
    ("Rs 500 debited at hpcl petrol pump fuel station via UPI", "Travel"),
    ("INR 1200 paid to makemytrip@icici for flight booking", "Travel"),

    # Utilities & Bills
    ("Rs 299 debited to jio@paytm for mobile prepaid recharge", "Utilities"),
    ("INR 1850 paid to torrent power electricity bill payment", "Utilities"),
    ("Rs 799 debited to airtel@axisbank broadband wifi bill", "Utilities"),
    ("Paid Rs 950 to indane gas cylinder booking utility bill", "Utilities"),
    ("Rs 499 debited to tataplay dth television recharge", "Utilities"),
    ("INR 650 paid to vodafone idea postpaid mobile bill", "Utilities"),

    # Shopping & E-Commerce
    ("Rs 1299 debited to amazon@apl for online shopping order", "Shopping"),
    ("INR 899 paid to flipkart@axisbank electronics delivery", "Shopping"),
    ("Rs 1599 debited to myntra@icici for clothes fashion shopping", "Shopping"),
    ("Paid Rs 2450 to dmart@hdfcbank supermarket grocery shopping", "Shopping"),
    ("Rs 450 debited to meesho@sbi online apparel order", "Shopping"),
    ("INR 3200 paid to nykaa@icici beauty and retail shopping", "Shopping")

]
#create dataframe from list
df = pd.DataFrame(data, columns=["sms_text", "category"])
# print(f"Total SMS Records:", df.shape)
# print(df)
# exit(1)

# ==========================================
# STEP 2: Peek Inside CountVectorizer (For Students)
# ==========================================
# Custom stop words so important banking words like "bill" aren't deleted
# (sklearn's default stop_words="english" removes "bill", "amount", "due", etc.)
custom_stops = ["from", "to", "for", "via", "and", "at", "on", "of", "the", "in"]

sample_vectorizer = CountVectorizer(stop_words=custom_stops)
X_counts = sample_vectorizer.fit_transform(df["sms_text"])
print(X_counts)
# exit(1)
count_df = pd.DataFrame(
    X_counts.toarray(), 
    columns=sample_vectorizer.get_feature_names_out()
)

print("--- Sample Word Count Matrix (First 5 SMS, Selected Columns) ---")
selected_words = ["debited", "zomato", "irctc", "recharge", "bill", "shopping"]
print(count_df[selected_words].head(5), "\n")

# ==========================================
# STEP 3: Train-Test Split & Pipeline Setup
# ==========================================
X_train, X_test, y_train, y_test = train_test_split(
    df["sms_text"], 
    df["category"], 
    test_size=0.25, 
    random_state=42, 
    stratify=df["category"]
)

# Pipeline combines tokenization + Multinomial Naive Bayes
# alpha=1.0 applies Laplace Smoothing for unseen words
model_pipeline = Pipeline([
    ("vectorizer", CountVectorizer(stop_words=custom_stops, ngram_range=(1, 2))),
    ("nb_classifier", MultinomialNB(alpha=1.0))
])

model_pipeline.fit(X_train, y_train)

# ==========================================
# STEP 4: Evaluate on Test Set
# ==========================================
y_pred = model_pipeline.predict(X_test)
print("--- Classification Report on Test Set ---")
print(classification_report(y_test, y_pred))

print("--- Confusion Matrix ---")
print(pd.DataFrame(
    confusion_matrix(y_test, y_pred),
    index=[f"Actual_{c}" for c in model_pipeline.classes_],
    columns=[f"Pred_{c}" for c in model_pipeline.classes_]
), "\n")

# ==========================================
# STEP 5: Inspect Top Keywords per Category
# ==========================================
print("--- Top 4 Most Influential Tokens per Category ---")
vect = model_pipeline.named_steps["vectorizer"]
clf = model_pipeline.named_steps["nb_classifier"]
feature_names = vect.get_feature_names_out()

for i, category in enumerate(clf.classes_):
    top_indices = np.argsort(clf.feature_log_prob_[i])[-4:][::-1]
    top_words = [feature_names[idx] for idx in top_indices]
    print(f"Category [{category:10s}] -> {top_words}")
print()

# ==========================================
# STEP 6: Test on Brand-New Real-World SMS
# ==========================================
new_sms_alerts = [
    "Rs 320 debited from A/c XX4510 to swiggy@axisbank for late night dinner",
    "INR 1120 paid to pgvcl electricity bill payment via UPI",
    "Paid Rs 430 to uber@hdfcbank for airport cab ride",
    "Rs 1999 debited to flipkart@icici for shoes shopping",
    # Tricky unseen merchant ("honest_restaurant") + known context word ("food")
    "Rs 260 paid to honest_restaurant@sbi for family food order"
]

predictions = model_pipeline.predict(new_sms_alerts)
probabilities = model_pipeline.predict_proba(new_sms_alerts)
classes = model_pipeline.classes_

print("--- Predictions on Unseen UPI SMS Messages ---")
for sms, pred, probs in zip(new_sms_alerts, predictions, probabilities):
    max_prob = np.max(probs) * 100
    print(f"\nSMS: '{sms}'")
    print(f" -> Predicted Category: {pred} (Confidence: {max_prob:.1f}%)")
    prob_str = ", ".join([f"{c}: {p*100:.1f}%" for c, p in zip(classes, probs)])
    print(f" -> Class Breakdown: [{prob_str}]")