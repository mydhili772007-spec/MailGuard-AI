# 🛡 MailGuard AI

## AI-Powered Email Threat Detection & Risk Analysis Platform

### Description

MailGuard AI is a machine learning-based web application that detects and classifies emails as **Safe (Ham)**, **Spam**, or **Phishing**. The system analyzes email content using Natural Language Processing (NLP) and Machine Learning techniques to identify potential threats.

Users can paste email content into the application and receive an instant prediction along with a confidence score and risk level. The project helps improve email security awareness and demonstrates the use of Machine Learning in cybersecurity.

### Features

* Detects Safe, Spam, and Phishing emails
* Real-time email scanning
* Confidence score prediction
* Risk level assessment
* Dark-themed user interface
* Built using Machine Learning and Flask

### Technologies Used

* Python
* Flask
* Scikit-Learn
* Pandas
* NumPy
* HTML
* CSS

### How to Run

1. Install the required libraries.
2. Run `train.py` to train the model.
3. Run `app.py` to start the web application.
4. Open `http://127.0.0.1:5000` in your browser.

### Sample Output

**Input:**
Your bank account has been suspended. Verify immediately.

**Output:**

* Prediction: Phishing Email
* Confidence Score: 98%
* Risk Level: High Risk
