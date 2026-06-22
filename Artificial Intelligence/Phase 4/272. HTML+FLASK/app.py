from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def home():

    return render_template(
        "home.html",
        name="Harshit",
        course="Flask Development",
        day=272
    )


@app.route("/profile")
def profile():

    skills = [
        "Python",
        "Flask",
        "HTML",
        "CSS",
        "Machine Learning"
    ]

    return render_template(
        "profile.html",
        username="Harshit",
        skills=skills
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )