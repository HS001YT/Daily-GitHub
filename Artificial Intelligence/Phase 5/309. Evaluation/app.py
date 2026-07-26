import os

import joblib
import numpy as np

from flask import Flask
from flask import render_template
from flask import request

from tensorflow.keras.models import load_model


app = Flask(__name__)


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "other_files",
    "model.keras"
)

SCALER_PATH = os.path.join(
    BASE_DIR,
    "other_files",
    "scaler.pkl"
)


model = load_model(
    MODEL_PATH
)

scaler = joblib.load(
    SCALER_PATH
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

    try:

        longitude = float(
            request.form["longitude"]
        )

        latitude = float(
            request.form["latitude"]
        )

        housing_median_age = float(
            request.form["housing_median_age"]
        )

        total_rooms = float(
            request.form["total_rooms"]
        )

        total_bedrooms = float(
            request.form["total_bedrooms"]
        )

        population = float(
            request.form["population"]
        )

        households = float(
            request.form["households"]
        )

        median_income = float(
            request.form["median_income"]
        )

        values = np.array([
            [
                longitude,
                latitude,
                housing_median_age,
                total_rooms,
                total_bedrooms,
                population,
                households,
                median_income
            ]
        ])

        scaled_values = scaler.transform(
            values
        )

        prediction = model.predict(
            scaled_values,
            verbose=0
        )

        predicted_price = float(
            prediction[0][0]
        )

        return render_template(
            "index.html",
            prediction=f"${predicted_price:,.2f}"
        )

    except Exception as error:

        return render_template(
            "index.html",
            error=str(error)
        )


if __name__ == "__main__":

    app.run(
        debug=True
    )