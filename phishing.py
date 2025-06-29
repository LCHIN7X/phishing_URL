import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


file_path = "C:/Users/night/Documents/CS/phishing_URL/phishing_site_urls.csv"
df = pd.read_csv(file_path, encoding="ISO-8859-1")

X = df["URL"]
y = df["Label"]  


vectorizer = CountVectorizer()
X_transformed = vectorizer.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=42)

model = MultinomialNB()
model.fit(X_train, y_train)

with open("phishing.pkl", "wb") as model_file:
    pickle.dump(model, model_file)

with open("vectorizer.pkl", "wb") as vec_file:
    pickle.dump(vectorizer, vec_file)

print("Model saved as phishing.pkl")
