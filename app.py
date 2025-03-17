from flask import Flask,request,jsonify,render_template
import numpy as np



app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)