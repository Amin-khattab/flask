from flask import Flask,request,render_template,session,redirect
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

GAME =["KCD2","DS2","Minecraft"]
GENDER = ["M","F","other"]
REGISTRANTS = {}
@app.route("/")
def index():
   return render_template("index.html")

@app.route("/login",methods = ["POST","GET"])
def login():
    if request.method =="POST":
        email = request.form.get("email")
        session["email"] = email
        return render_template("login.html",email =email)
    else:
        return render_template("login.html",email = session.get("email"))

@app.route("/logout")
def logout():
    session.clear()
    return render_template("index.html")


@app.route("/check",methods = ["POST"])
def check():
    return render_template("check.html")

@app.route("/register",methods = ["POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        gender = request.form.get("gender")
        game = request.form.get("game")

        if not name:
            return render_template("error.html", message="name is required for you to register")
        if not age.isdigit() or not 1 <= int(age) <= 100:
            return render_template("error.html", message="age is required and must be between 1-100")
        if gender not in GENDER:
            return render_template("error.html", message="gender must be M or F or other")
        if game not in GAME:
            return render_template("error.html", message="game must be between the games that are provided")
        else:
            REGISTRANTS[name] = {
                "age": age,
                "gender": gender,
                "game": game
            }
            return render_template("register.html",name = name,age=age,gender=gender,game=game)
    return render_template("check.html")

@app.route("/registrants",methods = ["POST"])
def registrants():
    return render_template("registrants.html",people = REGISTRANTS)
