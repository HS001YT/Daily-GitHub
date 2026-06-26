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
    "model.pkl"
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

    sepal_length = float(
        request.form.get(
            "sepal_length"
        )
    )

    sepal_width = float(
        request.form.get(
            "sepal_width"
        )
    )

    petal_length = float(
        request.form.get(
            "petal_length"
        )
    )

    petal_width = float(
        request.form.get(
            "petal_width"
        )
    )

    prediction = model.predict(
        [[
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        ]]
    )[0]

    classes = {
        0: "Setosa",
        1: "Versicolor",
        2: "Virginica"
    }

    result = classes[
        prediction
    ]

    return render_template(
        "result.html",
        result=result
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )