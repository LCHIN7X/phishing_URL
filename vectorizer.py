import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer


file_path = "C:/Users/night/Documents/CS/phishing_URL/phishing_site_urls.csv"
df = pd.read_csv(file_path, encoding="ISO-8859-1")


print(df.head())  # See column names


X_train = df["URL"].astype(str)


vectorizer = TfidfVectorizer()
X_train_transformed = vectorizer.fit_transform(X_train)  

pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print(" Vectorizer saved as 'vectorizer.pkl'!")
