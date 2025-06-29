import pickle
import numpy as np

# Load trained model
with open("phishing.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Load trained CountVectorizer
with open("vectorizer.pkl", "rb") as vec_file:
    vectorizer = pickle.load(vec_file)

def phishPrediction(url):
    # Transform input URL using the saved vectorizer
    url_vectorized = vectorizer.transform([url])  # must be a list

    # Predict label and probabilities
    y_pred = model.predict(url_vectorized)[0]
    y_proba = model.predict_proba(url_vectorized)[0]  # [phishing_prob, non_phishing_prob]

    y_phishing = y_proba[0]  # Assuming label 'bad' corresponds to index 0
    y_non_phishing = y_proba[1]

    print(f"Predicted label: {y_pred}")
    print(f"Phishing probability: {y_phishing}")
    print(f"Non-Phishing probability: {y_non_phishing}")

    return y_pred, round(y_phishing * 100, 2), round(y_non_phishing * 100, 2)
