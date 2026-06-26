from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def home():

    username = "Harshit"

    return render_template(
        "home.html",
        username=username
    )


@app.route("/students")
def students():

    student_data = [

        {
            "name": "Harshit",
            "age": 19,
            "status": "Pass"
        },

        {
            "name": "Rahul",
            "age": 20,
            "status": "Fail"
        },

        {
            "name": "Priya",
            "age": 18,
            "status": "Pass"
        }

    ]

    return render_template(
        "students.html",
        students=student_data
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )