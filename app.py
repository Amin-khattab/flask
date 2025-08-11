#so this is the flask behind those html files so when things get done lets say you have provided name/age/gender/sport here you get
#redirected to like register.html, 


from flask import Flask,render_template,request

app = Flask(__name__)

SPORT =[
    "basketball",
    "football",
    "tennis"
]

@app.route("/")
def index():
    return render_template("index.html",sports=SPORT)

@app.route("/register", methods=["POST"])
def register():
    sport = request.form.get("sport", "not provided")
    sex = request.form.get("sex", "Not provided")
    age = request.form.get("age", "Not provided")
    name = request.form.get("name", "whoever you are")


    if not name:

        return render_template("error.html",message="missing name")

    elif not age.isdigit() or not 1 < int(age) < 120:

        return render_template("error.html", message = "age must be a number and between 1-120")

    elif sex not in ["male","female","other"]:

        return render_template("error.html",message = "gender must be between male,female,other")

    elif sport not in SPORT:

        return render_template("error.html",message = "sport must be between these that have been provided")

    else:

        return render_template("register.html",name=name,age=age,sex=sex,sport=sport)
