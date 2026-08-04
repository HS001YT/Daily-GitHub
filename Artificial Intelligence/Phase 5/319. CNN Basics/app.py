import os

import numpy as np

from PIL import Image

from flask import Flask
from flask import render_template
from flask import request

from tensorflow.keras.models import load_model


# ==========================================================
# Flask App
# ==========================================================

app = Flask(__name__)


# ==========================================================
# Folder Paths
# ==========================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

OTHER_FILES = os.path.join(
    BASE_DIR,
    "other_files"
)

UPLOAD_FOLDER = os.path.join(
    BASE_DIR,
    "static",
    "uploads"
)

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# ==========================================================
# Load CNN Model
# ==========================================================

MODEL_PATH = os.path.join(
    OTHER_FILES,
    "cnn_digit_model.keras"
)

model = load_model(
    MODEL_PATH
)

print()

print("CNN Model Loaded Successfully")

print()


# ==========================================================
# Home Page
# ==========================================================

@app.route("/")

def home():

    return render_template(
        "index.html"
    )

# ==========================================================
# Predict Digit
# ==========================================================

@app.route(

    "/predict",

    methods=["POST"]

)

def predict():

    if "image" not in request.files:

        return render_template(

            "index.html",

            error="Please upload an image."

        )

    file = request.files["image"]

    if file.filename == "":

        return render_template(

            "index.html",

            error="No file selected."

        )

    image_path = os.path.join(

        app.config["UPLOAD_FOLDER"],

        file.filename

    )

    file.save(

        image_path

    )

    image = Image.open(

        image_path

    )

    image = image.convert(

        "L"

    )

    image = image.resize(

        (

            28,

            28

        )

    )

    image_array = np.array(

        image

    )

    image_array = 255 - image_array

    image_array = image_array.astype(

        "float32"

    ) / 255.0

    image_array = image_array.reshape(

        1,

        28,

        28,

        1

    )

    prediction = model.predict(

        image_array,

        verbose=0

    )

    predicted_digit = int(

        np.argmax(

            prediction

        )

    )

    confidence = float(

        np.max(

            prediction

        ) * 100

    )

    return render_template(

        "index.html",

        prediction=predicted_digit,

        confidence=round(

            confidence,

            2

        ),

        image=file.filename

    )

if __name__ == "__main__":

    app.run(

        debug=True

    )