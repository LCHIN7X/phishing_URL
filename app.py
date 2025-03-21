import numpy as np
from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load dataset
file_path = "C:/Users/night/Documents/CS/phishing_URL/phishing_site_urls.csv"
df = pd.read_csv(file_path, encoding="ISO-8859-1")

# Load trained model & vectorizer
model = pickle.load(open('phishing.pkl', 'rb'))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))  # Load vectorizer

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    Check if the input URL is phishing based on dataset & model prediction.
    """
    user_url = request.form["z1"]  # Get input URL
    
    # Check if URL exists in dataset
    if user_url in df.values:
        return render_template('index.html', prediction_text="🚨 THIS IS A DANGEROUS LINK (found in dataset) 🚨")
    
    # Transform URL using vectorizer
    transformed_url = vectorizer.transform([user_url])  # Convert text into numeric form
    
    # Predict with model
    result = model.predict(transformed_url)
    
    # Return result
    if result[0] == "bad":
        return render_template('index.html', prediction_text="🚨 THIS IS A DANGEROUS LINK (predicted by model) 🚨")
    else:
        return render_template('index.html', prediction_text="✅ THIS IS A SAFE LINK ✅")

if __name__ == "__main__":
    app.run(debug=True)
