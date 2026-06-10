import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report



data = pd.read_csv("dataset/emails.csv")

print("Dataset Loaded Successfully")
print(data.head())



encoder = LabelEncoder()

data["label"] = encoder.fit_transform(data["label"])



vectorizer = TfidfVectorizer(
    stop_words='english',
    lowercase=True
)

X = vectorizer.fit_transform(data["text"])

y = data["label"]



X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)



model = MultinomialNB()

model.fit(X_train, y_train)



y_pred = model.predict(X_test)



accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))



joblib.dump(model, "model/spam_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")
joblib.dump(encoder, "model/encoder.pkl")

print("\nModel Saved Successfully!")



while True:

    email = input("\nEnter Email Text (or type exit): ")

    if email.lower() == "exit":
        break

    email_vector = vectorizer.transform([email])

    prediction = model.predict(email_vector)

    result = encoder.inverse_transform(prediction)

    print("Prediction:", result[0])