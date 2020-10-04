# General imports for this project
import os
from flask import ( Flask, render_template, url_for )
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# Import my env.py that's ignored by git
if os.path.exists("env.py"):
    import env


# App instance
app = Flask(__name__)
SECRET_KEY = os.environ.get("SECRET_KEY")
app.secret_key = SECRET_KEY


# MongoDB configuration
MONGO_URI = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = 'jobboard_milestone3'
app.config["MONGO_URI"] = MONGO_URI
mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


# Login page for candidates and admin to login
@app.route('/login')
def login():
    return render_template('login.html')


# Registration page for new users
@app.route('/register')
def register():
    return render_template('register.html')


# Contact page in case of any problems
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Vacancies page for overview of open vacancies
@app.route('/vacancies')
def vacancies():
    vacancies_open = mongo.db.vacancies.find({'vacancy_status': 'open'})

    return render_template("vacancies.html", 
        vacancies_open=vacancies_open )


# To run the app
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)                     #debug uitzetten aan het eind