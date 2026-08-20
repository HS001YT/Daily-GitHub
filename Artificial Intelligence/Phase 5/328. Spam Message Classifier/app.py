import os
import pickle
import tensorflow as tf

from flask import Flask, render_template, request
from tensorflow.keras.preprocessing.sequence import pad_sequences


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "other_files",
    "spam_model.keras"
)

TOKENIZER_PATH = os.path.join(
    BASE_DIR,
    "other_files",
    "tokenizer.pkl"
)

MAX_LENGTH = 100


app = Flask(__name__)


print("Loading spam detection model...")

model = tf.keras.models.load_model(
    MODEL_PATH
)

with open(
    TOKENIZER_PATH,
    "rb"
) as file:

    tokenizer = pickle.load(file)

print("Model loaded successfully.")


def preprocess_message(message):

    sequence = tokenizer.texts_to_sequences(
        [message]
    )

    sequence = pad_sequences(
        sequence,
        maxlen=MAX_LENGTH,
        padding="post",
        truncating="post"
    )

    return sequence


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

    message = request.form.get(
        "message",
        ""
    ).strip()

    if not message:

        return render_template(
            "index.html",
            error="Please enter a message."
        )

    sequence = preprocess_message(
        message
    )

    prediction = model.predict(
        sequence,
        verbose=0
    )[0][0]

    prediction = float(
        prediction
    )

    if prediction >= 0.5:

        result = "Spam"

        confidence = prediction * 100

    else:

        result = "Not Spam"

        confidence = (1 - prediction) * 100

    return render_template(
        "index.html",
        message=message,
        result=result,
        confidence=round(
            confidence,
            2
        )
    )


if __name__ == "__main__":

    print()
    print("=" * 50)
    print("SMS Spam Classification")
    print("=" * 50)
    print("Open: http://127.0.0.1:5000")
    print()

    app.run(
        debug=True
    )