from flask import Flask, render_template, request
import joblib

app = Flask(__name__)


model = joblib.load("model/spam_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")
encoder = joblib.load("model/encoder.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    email_text = request.form["email"]

   
    email_vector = vectorizer.transform([email_text])

    
    prediction = model.predict(email_vector)[0]

    
    probabilities = model.predict_proba(email_vector)[0]

    confidence = round(max(probabilities) * 100, 2)

    
    result = encoder.inverse_transform([prediction])[0]

    
    if result == "ham":
        risk = "LOW RISK 🟢"

    elif result == "spam":
        risk = "MEDIUM RISK 🟡"

    else:
        risk = "HIGH RISK 🔴"

    return render_template(
        "index.html",
        prediction=result,
        confidence=confidence,
        risk=risk,
        email=email_text
    )


if __name__ == "__main__":
    app.run(debug=True)