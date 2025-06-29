from flask import Flask, render_template, request
import predictPhish

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/phishing",methods=['GET','POST'])
def url():
    if request.method == 'GET':
        url_request = request.args.get('url')

        y_pred, y_phishing, y_non_phishing = predictPhish.phishPrediction(url_request)
        
        return render_template("index.html",
                                phish=y_phishing,
                                non_phish=y_non_phishing,
                                url=url_request)
    return render_template("index.html",phish=0,non_phish=0,url=" ")

if __name__ == "__main__":
    app.run(debug=True)
