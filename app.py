from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html  ")


@app.route("/shire")
def shire():
    return '<h1>Hello, Shire!</h1>'


if __name__ == "__main__":
    app.run(debug=True)
