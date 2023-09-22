from flask import Flask, templating, redirect, request, session 

app = Flask(__name__)
app.secret_key= 'root'

@app.route('/', methods=['GET', 'POST'])
def home():
    return templating.render_template("home.html")


@app.route('/iceeval', methods=['GET', 'POST'])
def evaluation_icebrekaer():
    return templating.render_template("evaluation_icebreaker.html")


if __name__ == "__main__":
    app.run(debug=True)