from flask import Flask
from flask import render_template
from flask import request
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

UPLOAD_FOLDER = os.path.join(
    BASE_DIR,
    "uploads"
)

if not os.path.exists(
    UPLOAD_FOLDER
):
    os.makedirs(
        UPLOAD_FOLDER
    )


@app.route("/")
def home():

    return render_template(
        "home.html"
    )


@app.route(
    "/upload",
    methods=["POST"]
)
def upload():

    file = request.files.get(
        "file"
    )

    if not file:

        return "No File Selected"

    if file.filename == "":

        return "No File Selected"

    filename = file.filename

    save_path = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    file.save(save_path)

    return render_template(
        "success.html",
        filename=filename
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )