# ==========================================================
# Day 325 - MobileNetV2 Image Classifier
# ==========================================================

import os

from flask import (
    Flask,
    render_template,
    request
)

import numpy as np

import tensorflow as tf

from tensorflow.keras.applications import MobileNetV2

from tensorflow.keras.applications.mobilenet_v2 import (
    preprocess_input,
    decode_predictions
)


# ==========================================================
# Flask Configuration
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

MODEL_PATH = os.path.join(
    OTHER_FILES,
    "mobilenetv2_feature_extractor.keras"
)


os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


app = Flask(__name__)

app.config[
    "UPLOAD_FOLDER"
] = UPLOAD_FOLDER


# ==========================================================
# Load Model
# ==========================================================

print("Loading MobileNetV2 model...")

model = tf.keras.models.load_model(
    MODEL_PATH
)

print("Model loaded successfully.")


# ==========================================================
# Home Route
# ==========================================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# ==========================================================
# Prediction Route
# ==========================================================

@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    if "image" not in request.files:

        return render_template(
            "index.html",
            error="Please select an image."
        )


    file = request.files["image"]


    if file.filename == "":

        return render_template(
            "index.html",
            error="Please select an image."
        )


    filename = file.filename

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    file.save(filepath)


    # ======================================================
    # Load Image
    # ======================================================

    image = tf.keras.utils.load_img(
        filepath,
        target_size=(224, 224)
    )


    image_array = tf.keras.utils.img_to_array(
        image
    )


    image_array = np.expand_dims(
        image_array,
        axis=0
    )


    image_array = preprocess_input(
        image_array
    )


    # ======================================================
    # Prediction
    # ======================================================

    predictions = model.predict(
        image_array,
        verbose=0
    )


    decoded_predictions = decode_predictions(
        predictions,
        top=5
    )[0]


    results = []


    for _, class_name, probability in decoded_predictions:

        results.append({
            "name": class_name.replace(
                "_",
                " "
            ).title(),

            "confidence": round(
                float(probability) * 100,
                2
            )
        })


    # ======================================================
    # Best Prediction
    # ======================================================

    best_prediction = results[0]


    return render_template(
        "index.html",
        prediction=best_prediction,
        results=results,
        image_path=(
            "uploads/" + filename
        )
    )


# ==========================================================
# Run Application
# ==========================================================

if __name__ == "__main__":

    print()
    print("=" * 60)
    print("MobileNetV2 Image Classifier")
    print("=" * 60)
    print()
    print("Open: http://127.0.0.1:5000")
    print()

    app.run(
        debug=True
    )