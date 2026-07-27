import os
import joblib
import numpy as np

from flask import Flask
from flask import render_template
from flask import request

from tensorflow.keras.models import load_model


app = Flask(__name__)


# ---------------------------------------
# Paths
# ---------------------------------------

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "other_files",
    "diabetes_model.keras"
)

SCALER_PATH = os.path.join(
    BASE_DIR,
    "other_files",
    "scaler.pkl"
)


# ---------------------------------------
# Load Model
# ---------------------------------------

model = load_model(
    MODEL_PATH
)

scaler = joblib.load(
    SCALER_PATH
)


# ---------------------------------------
# Home
# ---------------------------------------

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# ---------------------------------------
# Prediction
# ---------------------------------------

@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    try:

        pregnancies = float(
            request.form["pregnancies"]
        )

        glucose = float(
            request.form["glucose"]
        )

        blood_pressure = float(
            request.form["blood_pressure"]
        )

        skin_thickness = float(
            request.form["skin_thickness"]
        )

        insulin = float(
            request.form["insulin"]
        )

        bmi = float(
            request.form["bmi"]
        )

        diabetes_pedigree = float(
            request.form["diabetes_pedigree"]
        )

        age = float(
            request.form["age"]
        )

        values = np.array([
            [
                pregnancies,
                glucose,
                blood_pressure,
                skin_thickness,
                insulin,
                bmi,
                diabetes_pedigree,
                age
            ]
        ])

        values = scaler.transform(
            values
        )

        probability = model.predict(
            values,
            verbose=0
        )[0][0]

        confidence = probability * 100

        if probability >= 0.5:

            prediction = "Diabetes Detected"

        else:

            prediction = "No Diabetes"

            confidence = (1 - probability) * 100

        return render_template(

            "index.html",

            prediction=prediction,

            confidence=f"{confidence:.2f}%"

        )

    except Exception as error:

        return render_template(

            "index.html",

            error=str(error)

        )


# ---------------------------------------
# Run
# ---------------------------------------

if __name__ == "__main__":

    app.run(
        debug=True
    )
    