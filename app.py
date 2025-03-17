from flask import Flask,request,jsonify,render_template
import numpy as np
import pickle


app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)