import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load phishing dataset
file_path = "C:/Users/night/Documents/CS/phishing_URL/phishing_site_urls.csv"
df = pd.read_csv(file_path, encoding="ISO-8859-1")

# Check column names (modify based on your dataset)
print(df.head())  # See column names

# If your dataset has a column like "url", use it:
X_train = df["URL"].astype(str)  # Convert URLs to string

# Initialize and fit TF-IDF vectorizer
vectorizer = TfidfVectorizer()
X_train_transformed = vectorizer.fit_transform(X_train)  # Transform training data

# Save vectorizer for later use in Flask app
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print(" Vectorizer saved as 'vectorizer.pkl'!")
