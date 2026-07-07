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
    "spam_model.pkl"
)

VECTORIZER_PATH = os.path.join(
    BASE_DIR,
    "other_files",
    "vectorizer.pkl"
)

model = joblib.load(
    MODEL_PATH
)

vectorizer = joblib.load(
    VECTORIZER_PATH
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

        message = request.form.get(
            "message"
        )

        if not message:

            raise ValueError(
                "Please enter a message."
            )

        transformed_message = vectorizer.transform(
            [message]
        )

        prediction = model.predict(
            transformed_message
        )[0]

        return render_template(
            "result.html",
            prediction=prediction
        )

    except Exception as error:

        return render_template(
            "result.html",
            error=str(error)
        )


if __name__ == "__main__":

    app.run(
        debug=True
    )