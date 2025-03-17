from flask import Flask,request,jsonify,render_template
import numpy as np
import pickle
import pandas as pd


app = Flask(__name__)

file_path = "C:/Users/night/Documents/CS/phishing_URL/phishing_site_urls.csv"
df = pd.read_csv(file_path,encoding="ISO-8859-1")



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predicta():

    


if __name__ == "__main__":
    app.run(debug=True)