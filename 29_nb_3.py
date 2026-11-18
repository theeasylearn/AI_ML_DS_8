import re
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix

# ==========================================
# STEP 1: Realistic UPI SMS Dataset (expanded)
# ==========================================
# Fix #1: MORE DATA. Naive Bayes can only use words it has seen in training.
# With 4-5 training rows per class, most test SMS had no known words at all.
data = [
    # Food & Dining
    ("Rs. 245 debited from A/c XX1234 to VPA zomato@hdfcbank for food order", "Food"),
    ("INR 180.00 paid to swiggy@icici via UPI Ref 41258963", "Food"),
    ("Debited Rs 540 to dominos pizza online order via UPI", "Food"),
    ("Rs 120 paid to burgerking@axisbank from A/c XX8899", "Food"),
    ("UPI payment of Rs 95 to tea post cafe snack bill", "Food"),
    ("Rs 310 debited to mcdonalds@yesbank for dinner", "Food"),
    ("Rs 420 paid to zomato@icici for lunch food delivery", "Food"),
    ("INR 260 debited to swiggy@axisbank for dinner food delivery", "Food"),
    ("Rs 650 paid to pizzahut@hdfcbank for pizza dinner", "Food"),
    ("Rs 150 debited to chai cafe for tea and snacks", "Food"),
    ("INR 899 paid to barbeque nation restaurant dinner bill", "Food"),
    ("Rs 230 debited to kfc@icici for burger meal", "Food"),
    ("Rs 75 paid to local tea stall snack via UPI", "Food"),
    ("INR 1150 paid to restaurant for family lunch meal", "Food"),
    ("Rs 340 debited to swiggy instamart food snacks", "Food"),

    # Travel & Commute
    ("Rs. 1450 debited to irctc@sbi for railway ticket booking", "Travel"),
    ("INR 210 paid to uber@axisbank for cab ride trip", "Travel"),
    ("Rs 85 debited to olacabs@icici auto ride commute", "Travel"),
    ("Paid Rs 650 to redbus@hdfcbank for bus ticket booking", "Travel"),
    ("Rs 500 debited at hpcl petrol pump fuel station via UPI", "Travel"),
    ("INR 1200 paid to makemytrip@icici for flight booking", "Travel"),
    ("Rs 2000 debited at indian oil petrol pump fuel", "Travel"),
    ("INR 800 paid to bpcl fuel station petrol", "Travel"),
    ("Rs 350 debited to uber@icici cab ride to airport", "Travel"),
    ("Rs 60 paid to rapido@axisbank bike taxi ride", "Travel"),
    ("INR 4500 paid to indigo airlines flight ticket", "Travel"),
    ("Rs 120 debited to ahmedabad metro train ticket commute", "Travel"),
    ("Rs 980 paid to irctc@hdfcbank train ticket booking", "Travel"),
    ("INR 150 paid to fastag toll plaza highway trip", "Travel"),
    ("Rs 2300 debited to goibibo@icici hotel booking trip", "Travel"),

    # Utilities & Bills
    ("Rs 299 debited to jio@paytm for mobile prepaid recharge", "Utilities"),
    ("INR 1850 paid to torrent power electricity bill payment", "Utilities"),
    ("Rs 799 debited to airtel@axisbank broadband wifi bill", "Utilities"),
    ("Paid Rs 950 to indane gas cylinder booking utility bill", "Utilities"),
    ("Rs 499 debited to tataplay dth television recharge", "Utilities"),
    ("INR 650 paid to vodafone idea postpaid mobile bill", "Utilities"),
    ("Rs 1340 paid to pgvcl electricity bill payment", "Utilities"),
    ("INR 2100 debited to mgvcl electricity power bill", "Utilities"),
    ("Rs 239 paid to airtel prepaid mobile recharge", "Utilities"),
    ("Rs 420 debited to municipal water bill payment", "Utilities"),
    ("INR 780 paid to adani gas png bill", "Utilities"),
    ("Rs 599 debited to jiofiber broadband internet bill", "Utilities"),
    ("Rs 349 paid to dish tv dth recharge", "Utilities"),
    ("INR 1100 paid to bsnl landline telephone bill", "Utilities"),
    ("Rs 999 debited to act fibernet wifi internet bill", "Utilities"),

    # Shopping & E-Commerce
    ("Rs 1299 debited to amazon@apl for online shopping order", "Shopping"),
    ("INR 899 paid to flipkart@axisbank electronics delivery", "Shopping"),
    ("Rs 1599 debited to myntra@icici for clothes fashion shopping", "Shopping"),
    ("Paid Rs 2450 to dmart@hdfcbank supermarket grocery shopping", "Shopping"),
    ("Rs 450 debited to meesho@sbi online apparel order", "Shopping"),
    ("INR 3200 paid to nykaa@icici beauty and retail shopping", "Shopping"),
    ("Rs 2499 paid to amazon@icici for shoes shopping", "Shopping"),
    ("INR 1799 debited to flipkart@hdfcbank mobile accessories shopping", "Shopping"),
    ("Rs 999 paid to ajio@axisbank clothes apparel", "Shopping"),
    ("Rs 1650 debited to reliance smart grocery supermarket", "Shopping"),
    ("INR 3499 paid to croma electronics store", "Shopping"),
    ("Rs 2199 debited to decathlon sports shoes store", "Shopping"),
    ("Rs 799 paid to bigbasket@icici grocery delivery", "Shopping"),
    ("INR 1250 paid to westside fashion clothes store", "Shopping"),
    ("Rs 560 debited to blinkit grocery household items", "Shopping"),
]

df = pd.DataFrame(data, columns=["sms_text", "category"])
print(f"Total SMS Records: {len(df)}")
print(df["category"].value_counts(), "\n")
# ==========================================
# STEP 2: Text Cleaning (Fix #2)
# ==========================================
# Every SMS contains words like "rs", "debited", "paid", "upi", bank handles
# (hdfcbank, icici, axisbank) and numbers. These appear in ALL categories, so they
# carry no signal, but Naive Bayes still counts them and gets confused.
def clean_sms(text): 
    # text = Rs. 245 debited from A/c XX1234 to VPA zomato@hdfcbank for food order
    text = text.lower()
    text = re.sub(r"@\w+", " ", text)         # zomato@hdfcbank -> zomato hdfcbank
    text = re.sub(r"\bxx\d+\b", " ", text)    # account numbers like xx1234
    text = re.sub(r"\d+(\.\d+)?", " ", text)  # amounts and reference numbers
    return text
    # text debited from  to VPA zomato hdfcbank for food order

custom_stops = [
    # grammar words
    "from", "to", "for", "via", "and", "at", "on", "of", "the", "in",
    # banking words common to every SMS (no category signal)
    "rs", "inr", "debited", "paid", "payment", "upi", "ref", "vpa", "ac",
    "online", "order",
]

sample_vectorizer = CountVectorizer(preprocessor=clean_sms,stop_words=custom_stops)
X_counts = sample_vectorizer.fit_transform(df["sms_text"])
print("Vocabulary size after cleaning:", len(sample_vectorizer.vocabulary_))
print("Example tokens:", sample_vectorizer.build_analyzer()(df["sms_text"][0]), "\n")

# ==========================================
# STEP 3: Train-Test Split & Pipeline Setup
# ==========================================
X_train, X_test, y_train, y_test = train_test_split(
    df["sms_text"], df["category"],
    test_size=0.25, random_state=42, stratify=df["category"]
)
# exit(1)

# Fix #3: unigrams only. ngram_range=(1,3) created hundreds of 2-3 word
#         phrases that each appear only once - pure noise on a small dataset.
# Fix #4: alpha=0.1 (lighter smoothing). alpha=1.0 is heavy for few examples and
#         lets unseen/noise words pull the probabilities toward the wrong class.
clean_data = []
model_pipeline = Pipeline([
    ("vectorizer", CountVectorizer(preprocessor=clean_sms, stop_words=custom_stops,
                                   ngram_range=(1, 1))),
    ("nb_classifier", MultinomialNB(alpha=0.1)),
])
model_pipeline.fit(X_train, y_train)

# ==========================================
# STEP 4: Evaluate on Test Set
# ==========================================
y_pred = model_pipeline.predict(X_test)
print("--- Classification Report on Test Set ---")
print(classification_report(y_test, y_pred, zero_division=0))
print("--- Confusion Matrix ---")
print(pd.DataFrame(
    confusion_matrix(y_test, y_pred, labels=model_pipeline.classes_),
    index=[f"Actual_{c}" for c in model_pipeline.classes_],
    columns=[f"Pred_{c}" for c in model_pipeline.classes_]
), "\n")

# Fix #5: a single small test split is luck-dependent. Cross-validation averages
# accuracy over 5 different splits, which gives a more trustworthy number.
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(model_pipeline, df["sms_text"], df["category"], cv=cv)
print(f"5-Fold Cross-Validation Accuracy: {cv_scores.mean()*100:.1f}% "
      f"(per fold: {[round(s*100) for s in cv_scores]})\n")

# ==========================================
# STEP 5: Inspect Top Keywords per Category
# ==========================================
print("--- Top 5 Most Influential Tokens per Category ---")
vect = model_pipeline.named_steps["vectorizer"]
clf = model_pipeline.named_steps["nb_classifier"]
feature_names = vect.get_feature_names_out()
for i, category in enumerate(clf.classes_):
    top_indices = np.argsort(clf.feature_log_prob_[i])[-5:][::-1]
    print(f"Category [{category:10s}] -> {[feature_names[idx] for idx in top_indices]}")
print()

# ==========================================
# STEP 6: Test on Brand-New Real-World SMS
# ==========================================
# Retrain on ALL data before predicting truly new messages
model_pipeline.fit(df["sms_text"], df["category"])

new_sms_alerts = [
    "Rs 320 debited from A/c XX4510 to swiggy@axisbank for late night dinner",
    "INR 1120 paid to pgvcl electricity bill payment via UPI",
    "Paid Rs 430 to uber@hdfcbank for airport cab ride",
    "Rs 1999 debited to flipkart@icici for shoes shopping",
    "Rs 260 paid to honest_restaurant@sbi for family food order",
]
predictions = model_pipeline.predict(new_sms_alerts)
probabilities = model_pipeline.predict_proba(new_sms_alerts)
classes = model_pipeline.classes_

print("--- Predictions on Unseen UPI SMS Messages ---")
for sms, pred, probs in zip(new_sms_alerts, predictions, probabilities):
    print(f"\nSMS: '{sms}'")
    print(f" -> Predicted Category: {pred} (Confidence: {np.max(probs)*100:.1f}%)")