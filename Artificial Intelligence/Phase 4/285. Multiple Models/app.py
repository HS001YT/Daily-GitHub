from flask import Flask
from flask import render_template
from flask import request

import joblib
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

MODELS = {

    "Logistic Regression":
    joblib.load(
        os.path.join(
            BASE_DIR,
            "other_files",
            "logistic_regression.pkl"
        )
    ),

    "Decision Tree":
    joblib.load(
        os.path.join(
            BASE_DIR,
            "other_files",
            "decision_tree.pkl"
        )
    ),

    "Random Forest":
    joblib.load(
        os.path.join(
            BASE_DIR,
            "other_files",
            "random_forest.pkl"
        )
    )
}


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

    selected_model = request.form.get(
        "model"
    )

    values = []

    fields = [
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

    for field in fields:

        values.append(
            float(
                request.form.get(
                    field
                )
            )
        )

    prediction = MODELS[
        selected_model
    ].predict(
        [values]
    )[0]

    if prediction == 1:

        result = "Heart Disease Detected"

    else:

        result = "No Heart Disease Detected"

    return render_template(
        "result.html",
        result=result,
        model_name=selected_model
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )