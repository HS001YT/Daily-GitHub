# Running the Flask App (Day 266)
# 1. Make sure app.py, sentiment_model.joblib, and vectorizer.joblib are in the correct locations.
# 2. Open the terminal in the project folder.
# 3. Run:
#     python app.py
# 4. Open your browser and visit:
#     http://127.0.0.1:5000


from flask import Flask
from flask import render_template
from flask import request

import joblib
import re

app = Flask(__name__)

model = joblib.load(
    "sentiment_model.joblib"
)

vectorizer = joblib.load(
    "vectorizer.joblib"
)


def preprocess_text(text):

    text = text.lower()

    text = re.sub(
        r"\d+",
        "",
        text
    )

    text = re.sub(
        r"[^\w\s]",
        "",
        text
    )

    return text


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

    review = request.form[
        "review"
    ]

    review = preprocess_text(
        review
    )

    review_vector = (
        vectorizer.transform(
            [review]
        )
    )

    prediction = model.predict(
        review_vector
    )[0]

    return render_template(
        "index.html",
        prediction=prediction
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )