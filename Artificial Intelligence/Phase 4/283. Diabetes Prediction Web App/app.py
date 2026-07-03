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
    "diabetes_model.pkl"
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

    pregnancies = float(
        request.form.get("pregnancies")
    )

    glucose = float(
        request.form.get("glucose")
    )

    blood_pressure = float(
        request.form.get("blood_pressure")
    )

    skin_thickness = float(
        request.form.get("skin_thickness")
    )

    insulin = float(
        request.form.get("insulin")
    )

    bmi = float(
        request.form.get("bmi")
    )

    pedigree = float(
        request.form.get("pedigree")
    )

    age = float(
        request.form.get("age")
    )

    prediction = model.predict(
        [[
            pregnancies,
            glucose,
            blood_pressure,
            skin_thickness,
            insulin,
            bmi,
            pedigree,
            age
        ]]
    )[0]

    if prediction == 1:
        result = "Diabetes Detected"
    else:
        result = "No Diabetes Detected"

    return render_template(
        "result.html",
        result=result
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )