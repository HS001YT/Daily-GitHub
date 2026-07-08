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
    "resume_model.pkl"
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

        resume_text = request.form.get(
            "resume"
        )

        if not resume_text:

            raise ValueError(
                "Please enter resume text."
            )

        transformed_text = vectorizer.transform(
            [resume_text]
        )

        prediction = model.predict(
            transformed_text
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