from flask import Flask
from flask import render_template
from flask import request

import os
import joblib

app = Flask(__name__)

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

OTHER_FILES_DIR = os.path.join(
    BASE_DIR,
    "other_files"
)

models = {

    "Logistic Regression":
    joblib.load(
        os.path.join(
            OTHER_FILES_DIR,
            "logistic_regression.pkl"
        )
    ),

    "Decision Tree":
    joblib.load(
        os.path.join(
            OTHER_FILES_DIR,
            "decision_tree.pkl"
        )
    ),

    "Random Forest":
    joblib.load(
        os.path.join(
            OTHER_FILES_DIR,
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

    results = {}

    for name, model in models.items():

        prediction = model.predict(
            [values]
        )[0]

        if prediction == 1:

            results[name] = (
                "Heart Disease Detected"
            )

        else:

            results[name] = (
                "No Heart Disease Detected"
            )

    return render_template(
        "result.html",
        results=results
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )