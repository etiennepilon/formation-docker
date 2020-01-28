from flask import Flask, render_template, request
import json
import os

HOSTNAME = os.getenv("HOSTNAME", default="127.0.0.1")
JSON_PATH = os.getenv("JSON_PATH", default="data/members.json")

app = Flask(__name__)


with open(JSON_PATH, "r") as f:
    members = json.load(f)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/about")
def about():
    return render_template("about.html")
    
@app.route('/table')
def table():
    return render_template('table.html',
                            title='Active Members',
                            rows=members)
@app.route('/add_member', methods = ["POST", "GET"])
def add_member():
    if request.method == "GET":
        return render_template("form.html") 
    if request.method == "POST":
        name = request.form["answer"]
        members.append(dict(id=len(members), name=name))
        with open(JSON_PATH, "w+") as f:
            json.dump(members, f)
        return render_template('table.html',
                                title='Active Members',
                                rows=members)
                           

if __name__ == "__main__":
    app.run(host=HOSTNAME, port=5000)
