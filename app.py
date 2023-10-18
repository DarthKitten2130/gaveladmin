from flask import Flask, templating, redirect, request, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://darthkitten2228:Bi4E8vlSCodf@ep-twilight-mud-18405172.ap-southeast-1.aws.neon.tech/2023-2024"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'root'

db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(7),primary_key = True)
    rollno = db.Column(db.Integer())
    name = db.Column(db.String(255))
    role = db.Column(db.String(7))
    email = db.Column(db.String(255), unique = True)
    psswd = db.Column(db.String(255))
    grade = db.Column(db.Integer())
    section = db.Column(db.String(1))
    phone = db.Column(db.String(255))


@app.route('/', methods=['GET', 'POST'])
def home():
    return templating.render_template("home.html")


@app.route('/evalice', methods=['GET', 'POST'])
def evaluation_icebreaker():
    return templating.render_template("evaluation_icebreaker.html")


@app.route('/evalgen', methods=['GET', 'POST'])
def evaluation_general():
    return templating.render_template("evaluation_general.html")


@app.route('/geneval', methods=['GET', 'POST'])
def general_evaluator():
    return templating.render_template("general_evaluator.html")


@app.route('/ahcounter', methods=['GET', 'POST'])
def ahcounter():
    return templating.render_template("ahcounter.html")


@app.route('/timer', methods=['GET', 'POST'])
def timer():
    return templating.render_template("timer1.html")


@app.route('/wmg', methods=['GET', 'POST'])
def wmg():
    return templating.render_template("wmg1.html")


@app.route('/oc', methods=['GET', 'POST'])
def oc():
    return templating.render_template("oc1.html")


if __name__ == "__main__":
    app.run(debug=True)
