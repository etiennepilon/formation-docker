from flask import Flask, render_template
import os

HOSTNAME = os.getenv("HOSTNAME", default="127.0.0.1")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/about")
def about():
    return render_template("about.html")
    
if __name__ == "__main__":
    app.run(host=HOSTNAME, port=5000)
