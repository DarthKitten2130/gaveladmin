from flask import Flask, templating
from sql import *

app = Flask(__name__)
app.secret_key = 'root'


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


@app.route('/attendance', methods=['GET', 'POST'])
def attendance():
    results = fetch_attendance()
    return templating.render_template("attendance.html",results=results)

if __name__ == "__main__":
    app.run(debug=True)
