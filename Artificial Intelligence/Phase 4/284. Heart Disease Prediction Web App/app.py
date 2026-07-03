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
    "heart_model.pkl"
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

    values = []

    field_names = [
        "age",
        "sex",
        "cp",
        "trestbps",
        "chol",
        "fbs",
        "restecg",
        "thalach",
        "exang",
        "oldpeak",
        "slope",
        "ca",
        "thal"
    ]

    for field in field_names:

        values.append(
            float(
                request.form.get(
                    field
                )
            )
        )

    prediction = model.predict(
        [values]
    )[0]

    if prediction == 1:

        result = "Heart Disease Risk Detected"

    else:

        result = "No Heart Disease Risk Detected"

    return render_template(
        "result.html",
        result=result
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )