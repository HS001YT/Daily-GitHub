from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def home():

    return render_template(
        "home.html"
    )


@app.route(
    "/submit",
    methods=["POST"]
)
def submit():

    name = request.form.get(
        "name"
    )

    age = request.form.get(
        "age"
    )

    return render_template(
        "result.html",
        name=name,
        age=age
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )