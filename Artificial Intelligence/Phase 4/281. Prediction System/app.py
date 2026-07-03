from flask import Flask
from flask import render_template
from flask import request

import joblib
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "other_files",
    "house_price_model.pkl"
)

model = joblib.load(
    MODEL_PATH
)


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    area = float(
        request.form.get(
            "area"
        )
    )

    bedrooms = int(
        request.form.get(
            "bedrooms"
        )
    )

    age = int(
        request.form.get(
            "age"
        )
    )

    prediction = model.predict(
        [[
            area,
            bedrooms,
            age
        ]]
    )[0]

    return render_template(
        "result.html",
        price=round(
            prediction,
            2
        )
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )