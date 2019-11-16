# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/education_employed")
def education_employed():
    return render_template("education_employed.html")


@app.route("/edu_employed_d3")
def edu_employed_d3():
    return render_template("edu_employed_d3.html")


if __name__ == "__main__":
    app.run(debug=True)
