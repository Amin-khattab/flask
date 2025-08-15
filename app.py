from flask import Flask,request,render_template,session,redirect
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return render_template("login.html")
    return redirect("/")

@app.route("/check", methods=["POST", "GET"])
def check():
    if request.method == "POST":
        name = request.form.get("name")
        session["name"] = name
        return render_template("check.html", name=name)
    else:
        return render_template("check.html", name=session.get("name"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
