from flask import Flask, render_template, request
import predictPhish
import sql
import firewallRule

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/phishing', methods=['GET', 'POST'])
def url():
    if request.method == 'GET':
        url_requested = request.args.get('url')

        # Run phishing prediction
        y_pred, y_phishing, y_non_phishing = predictPhish.phishPrediction(url_requested)

        # If phishing, log and block
        if y_phishing >= 0.5:
            sql.phishing(url_requested)
            domain = firewallRule.getDomain(url_requested)
            BLOCK = f"127.0.0.1 {domain}"
            firewallRule.BlockURL(BLOCK)

        return render_template(
            "index.html",
            phish=round(y_phishing * 100, 2),
            non_phish=round(y_non_phishing * 100, 2),
            url=url_requested
        )

  
    return render_template("index.html", phish=0, non_phish=0, url="")

if __name__ == "__main__":
    app.run(debug=True)
