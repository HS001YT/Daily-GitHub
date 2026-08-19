# ==========================================================
# Day 327 - Sentiment Analysis using Deep Learning
# ==========================================================

import os
import json
import numpy as np
import tensorflow as tf

from flask import (
    Flask,
    render_template,
    request
)

from tensorflow.keras.preprocessing.sequence import pad_sequences


# ==========================================================
# Configuration
# ==========================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

OTHER_FILES = os.path.join(
    BASE_DIR,
    "other_files"
)

MODEL_PATH = os.path.join(
    OTHER_FILES,
    "sentiment_model.keras"
)

WORD_INDEX_PATH = os.path.join(
    OTHER_FILES,
    "word_index.json"
)

MAX_LENGTH = 200
VOCAB_SIZE = 10000


# ==========================================================
# Flask
# ==========================================================

app = Flask(__name__)


# ==========================================================
# Load Model
# ==========================================================

print("Loading sentiment model...")

model = tf.keras.models.load_model(
    MODEL_PATH
)

print("Model loaded successfully.")


# ==========================================================
# Load Word Index
# ==========================================================

with open(
    WORD_INDEX_PATH,
    "r",
    encoding="utf-8"
) as file:

    word_index = json.load(file)


# ==========================================================
# Text Preprocessing
# ==========================================================

def preprocess_text(text):

    words = text.lower().split()

    sequence = []

    for word in words:

        index = word_index.get(
            word,
            2
        )

        if index >= VOCAB_SIZE:

            index = 2

        sequence.append(
            index
        )

    sequence = pad_sequences(
        [sequence],
        maxlen=MAX_LENGTH,
        padding="post",
        truncating="post"
    )

    return sequence


# ==========================================================
# Home
# ==========================================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# ==========================================================
# Predict
# ==========================================================

@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    text = request.form.get(
        "text",
        ""
    ).strip()


    if not text:

        return render_template(
            "index.html",
            error="Please enter a review."
        )


    sequence = preprocess_text(
        text
    )


    prediction = model.predict(
        sequence,
        verbose=0
    )[0][0]


    prediction = float(
        prediction
    )


    if prediction >= 0.5:

        sentiment = "Positive"

        confidence = prediction * 100

    else:

        sentiment = "Negative"

        confidence = (1 - prediction) * 100


    return render_template(
        "index.html",
        text=text,
        sentiment=sentiment,
        confidence=round(
            confidence,
            2
        )
    )


# ==========================================================
# Run
# ==========================================================

if __name__ == "__main__":

    print()
    print("=" * 60)
    print("Sentiment Analysis Application")
    print("=" * 60)
    print()
    print("Open: http://127.0.0.1:5000")
    print()

    app.run(
        debug=True
    )