from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    req = requests.get("https://data.kodeplat.manoe.my.id/")
    data = req.json()

    return render_template("home.html", data=data)

if __name__ == "__main__":
    app.run()
