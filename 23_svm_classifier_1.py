
# SVM Classification: Email Spam Detection
# Dataset: Kaggle Spam Mails Dataset

# 1. Import libraries
import kagglehub
import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import (accuracy_score,classification_report,ConfusionMatrixDisplay)
# 2. Download the Kaggle dataset
print("Downloading dataset...")

path = kagglehub.dataset_download(
    "venky73/spam-mails-dataset"
)
print(path)
print("Dataset downloaded successfully!")


# 3. Find and load the CSV file
df = pd.read_csv(path + "/spam_ham_dataset.csv")


print("\nDataset shape:", df.shape)
print("\nColumns:", df.columns.tolist())

# exit(1)

# 4. Prepare the dataset
df.dropna(subset=["text", "label"]).copy()
print("\nFirst five rows:")
print(df.head())

df["text"] = df["text"].astype(str)
df["label"] = df["label"].astype(str).str.strip().str.lower()


df = df[df["label"].isin(["spam", "ham"])]

X = df["text"] #input feature
y = df["label"] #output label

print("\nEmail categories:")
print(y.value_counts())
# exit(1)


# 5. Split training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining emails:", len(X_train))
print("Testing emails:", len(X_test))

# 6. Create the SVM model
model = Pipeline([
    ("tfidf", TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2),
        max_features=20000
    )),
    ("svm", LinearSVC(random_state=42))
])



# 7. Train the model
print("\nTraining SVM model...")

model.fit(X_train, y_train)
print("Training completed!")

# 8. Evaluate the model
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# 9. Display confusion matrix
ConfusionMatrixDisplay.from_predictions(
    y_test,
    y_pred,
    labels=["ham", "spam"],
    display_labels=["Normal Email", "Spam Email"],
    cmap="Blues"
)

plt.title("SVM Email Spam Classification")
plt.tight_layout()
plt.show()
# exit(1)


# 10. Test new emails
new_emails = [
    "Congratulations! You won a free iPhone. Claim now!",
    "Please attend the project meeting tomorrow.",
    "URGENT! Claim your cash prize immediately.",
    "Your college examination timetable is published.",
    "Earn money fast from home. Click here now!",
    "Please review the attached project report.",
    "your salary has been credited",
    "your flight ticket has been booked successfully",
    "your bank account statement"
]

predictions = model.predict(new_emails)

print("\nNew Email Predictions:")

for email, prediction in zip(new_emails, predictions):
    print("\nEmail:", email)
    print("Prediction:", prediction.upper())

# exit(1)
# 11. Enter your own email
print("\nTest your own email")

while True:
    email = input(
        "\nEnter an email (or type exit to stop): "
    )

    if email.strip().lower() == "exit":
        break

    if not email.strip():
        print("Please enter an email.")
        continue

    prediction = model.predict([email])[0]

    print("Prediction:", prediction.upper())

    if prediction == "spam":
        print("This email is classified as SPAM.")
    else:
        print("This email is classified as NOT SPAM.")