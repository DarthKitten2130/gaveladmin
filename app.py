from flask import Flask, templating, redirect, request, session 

app = Flask(__name__)
app.secret_key= 'root'

@app.route('/', methods=['GET', 'POST'])
def home():
    return templating.render_template("home.html")


@app.route('/iceeval', methods=['GET', 'POST'])
def evaluation_icebreaker():
    return templating.render_template("evaluation_icebreaker.html")


@app.route('/geneval', methods=['GET', 'POST'])
def evaluation_general():
    return templating.render_template("evaluation_general.html")


if __name__ == "__main__":
    app.run(debug=True)