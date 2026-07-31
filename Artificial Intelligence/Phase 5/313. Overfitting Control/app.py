import os

import numpy as np

from flask import Flask
from flask import render_template
from flask import request

from tensorflow.keras.models import load_model

from PIL import Image


app = Flask(__name__)


# ---------------------------------------
# Paths
# ---------------------------------------

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

UPLOAD_FOLDER = os.path.join(
    BASE_DIR,
    "uploads"
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "other_files",
    "digit_model.keras"
)


os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# ---------------------------------------
# Load Model
# ---------------------------------------

model = load_model(
    MODEL_PATH
)


# ---------------------------------------
# Image Preprocessing
# ---------------------------------------

def preprocess_image(image_path):

    image = Image.open(
        image_path
    )

    image = image.convert(
        "L"
    )

    image = np.array(
        image
    )


    # -----------------------------------
    # Auto Detect Background
    # -----------------------------------

    if np.mean(image) > 127:

        image = 255 - image


    # -----------------------------------
    # Threshold
    # -----------------------------------

    image = np.where(

        image > 50,

        255,

        0

    ).astype(np.uint8)


    # -----------------------------------
    # Find Bounding Box
    # -----------------------------------

    rows = np.any(

        image > 0,

        axis=1

    )

    cols = np.any(

        image > 0,

        axis=0

    )


    if rows.any() and cols.any():

        y_min, y_max = np.where(rows)[0][[0, -1]]

        x_min, x_max = np.where(cols)[0][[0, -1]]

        image = image[
            y_min:y_max + 1,
            x_min:x_max + 1
        ]


    image = Image.fromarray(
        image
    )


    # -----------------------------------
    # Preserve Aspect Ratio
    # -----------------------------------

    image.thumbnail(
        (20, 20),
        Image.Resampling.LANCZOS
    )


    # -----------------------------------
    # Center on 28x28 Canvas
    # -----------------------------------

    canvas = Image.new(
        "L",
        (28, 28),
        color=0
    )


    x = (28 - image.size[0]) // 2

    y = (28 - image.size[1]) // 2


    canvas.paste(

        image,

        (x, y)

    )


    image = np.array(
        canvas
    )


    image = image.astype(
        "float32"
    ) / 255.0


    image = image.reshape(

        1,

        28,

        28

    )


    return image


# ---------------------------------------
# Home
# ---------------------------------------

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# ---------------------------------------
# Prediction
# ---------------------------------------

@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    try:

        if "image" not in request.files:

            return render_template(

                "index.html",

                error="Please upload an image."

            )


        file = request.files["image"]


        if file.filename == "":

            return render_template(

                "index.html",

                error="No image selected."

            )


        filepath = os.path.join(

            app.config["UPLOAD_FOLDER"],

            file.filename

        )


        file.save(
            filepath
        )


        image = preprocess_image(
            filepath
        )
        probabilities = model.predict(

            image,

            verbose=0

        )[0]


        predicted_digit = int(

            np.argmax(

                probabilities

            )

        )


        confidence = float(

            np.max(

                probabilities

            ) * 100

        )


        return render_template(

            "index.html",

            prediction=predicted_digit,

            confidence=f"{confidence:.2f}%",

            image_name=file.filename

        )


    except Exception as error:

        return render_template(

            "index.html",

            error=str(error)

        )


# ---------------------------------------
# Run Application
# ---------------------------------------

if __name__ == "__main__":

    app.run(

        debug=True

    )