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


@app.route("/education_unemployed")
def education_unemployed():
    return render_template("education_unemployed.html")


@app.route("/edu_unemployed_d3")
def edu_unemployed_d3():
    return render_template("edu_unemployed_d3.html")


@app.route("/age_employed")
def age_employed():
    return render_template("age_employed.html")


@app.route("/age_employed_d3")
def age_employed_d3():
    return render_template("age_employed_d3.html")


@app.route("/age_unemployed")
def age_unemployed():
    return render_template("age_unemployed.html")


@app.route("/age_unemployed_d3")
def age_unemployed_d3():
    return render_template("age_unemployed_d3.html")


@app.route("/data")
def data():
    return render_template("data.html")


@app.route("/comparison")
def comparison():
    return render_template("comparison.html")


@app.route("/form")
def game():
    return render_template("form.html")


@app.route("/data_age_emp")
def data_age_emp():
    return render_template("data_age_emp.html")
    

@app.route("/data_age_unemp")
def data_age_unemp():
    return render_template("data_age_unemp.html")


@app.route("/data_edu_emp")
def data_edu_emp():
    return render_template("data_edu_emp.html")


@app.route("/data_edu_unemp")
def data_edu_unemp():
    return render_template("data_edu_unemp.html")


if __name__ == "__main__":
    app.run(debug=True)
