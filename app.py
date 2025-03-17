from flask import Flask,request,jsonify,render_template
import numpy as np
import pickle


app = Flask(__name__)

file_path = "C:/Users/night/Documents/CS/phishing_URL/phishing_site_urls.csv"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predicta():

    


if __name__ == "__main__":
    app.run(debug=True)