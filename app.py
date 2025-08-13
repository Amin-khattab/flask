#so this is the flask behind those html files so when things get done lets say you have provided name/age/gender/sport here you get
#redirected to like register.html, 


from flask import Flask,render_template,request

app = Flask(__name__)

SPORT =[
    "basketball",
    "football",
    "tennis"
]

REGISTRANTS = {} #to store users information

@app.route("/") # this is how flask knows to first show index.html and when its filled
                # with the required info it gets redirected to bellow(register.html)
def index():
    return render_template("index.html",sports=SPORT)

@app.route("/register", methods=["POST"]) # this is the register.html that it will be redirected to using POST method
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

        REGISTRANTS[name] = { #here the users info is registered for later use in /registrants
            "sport":sport,
            "age":age,
            "sex":sex
        }
    
        return render_template("register.html",name=name,age=age,sex=sex,sport=sport)

@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTRANTS)
