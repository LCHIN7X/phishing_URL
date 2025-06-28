from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/phishing", methods=["GET"])
def check_url():
    url = request.args.get("url")

    # Simulated phishing check (you can replace with actual model)
    phish_percent = 78  # Example value
    non_phish_percent = 22  # Example value

    return render_template(
        "index.html",
        phish=phish_percent,
        non_phish=non_phish_percent,
        url=url
    )

if __name__ == "__main__":
    app.run(debug=True)
