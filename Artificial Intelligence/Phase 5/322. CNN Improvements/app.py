import os
import pickle

import numpy as np

from PIL import Image

from flask import (
    Flask,
    render_template,
    request
)

from tensorflow.keras.models import load_model


# ==========================================================
# Flask Application
# ==========================================================

app = Flask(__name__)


# ==========================================================
# Project Paths
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
# Model Path
# ==========================================================

MODEL_PATH = os.path.join(
    OTHER_FILES,
    "fashion_mnist_augmented_model.keras"
)


# ==========================================================
# Class Names Path
# ==========================================================

CLASS_NAMES_PATH = os.path.join(
    OTHER_FILES,
    "class_names.pkl"
)


# ==========================================================
# Load Model
# ==========================================================

print("=" * 70)

print("DAY 322 - CNN + DATA AUGMENTATION")

print("=" * 70)

print()


if not os.path.exists(MODEL_PATH):

    raise FileNotFoundError(
        "Model not found. "
        "Run train_model.py first."
    )


model = load_model(
    MODEL_PATH
)


print(
    "Model loaded successfully."
)

print()


# ==========================================================
# Load Class Names
# ==========================================================

if not os.path.exists(CLASS_NAMES_PATH):

    raise FileNotFoundError(
        "class_names.pkl not found. "
        "Run train_model.py first."
    )


with open(
    CLASS_NAMES_PATH,
    "rb"
) as file:

    class_names = pickle.load(
        file
    )


print(
    "Class names loaded successfully."
)

print()


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

    # ------------------------------------------------------
    # Check File
    # ------------------------------------------------------

    if "image" not in request.files:

        return render_template(
            "index.html",
            error="Please select an image."
        )


    file = request.files["image"]


    # ------------------------------------------------------
    # Check Filename
    # ------------------------------------------------------

    if file.filename == "":

        return render_template(
            "index.html",
            error="No image selected."
        )


    # ------------------------------------------------------
    # Validate Extension
    # ------------------------------------------------------

    allowed_extensions = (
        ".jpg",
        ".jpeg",
        ".png",
        ".webp"
    )

    filename = file.filename.lower()


    if not filename.endswith(
        allowed_extensions
    ):

        return render_template(
            "index.html",
            error=(
                "Unsupported format. "
                "Use JPG, JPEG, PNG or WEBP."
            )
        )


    # ------------------------------------------------------
    # Save Uploaded Image
    # ------------------------------------------------------

    image_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(
        image_path
    )


    # ------------------------------------------------------
    # Open Image
    # ------------------------------------------------------

    try:

        image = Image.open(
            image_path
        )

    except Exception:

        return render_template(
            "index.html",
            error="Unable to read the image."
        )


    # ------------------------------------------------------
    # Convert to Grayscale
    # ------------------------------------------------------

    image = image.convert(
        "L"
    )


    # ------------------------------------------------------
    # Resize to Fashion-MNIST Size
    # ------------------------------------------------------

    image = image.resize(
        (28, 28)
    )


    # ------------------------------------------------------
    # Convert to NumPy Array
    # ------------------------------------------------------

    image_array = np.array(
        image,
        dtype="float32"
    )


    # ------------------------------------------------------
    # Normalize
    # ------------------------------------------------------

    image_array = (
        image_array / 255.0
    )


    # ------------------------------------------------------
    # Add Channel Dimension
    # ------------------------------------------------------

    image_array = np.expand_dims(
        image_array,
        axis=-1
    )


    # ------------------------------------------------------
    # Add Batch Dimension
    # ------------------------------------------------------

    image_array = np.expand_dims(
        image_array,
        axis=0
    )


    # ======================================================
    # Prediction
    # ======================================================

    predictions = model.predict(
        image_array,
        verbose=0
    )[0]


    # ======================================================
    # Predicted Class
    # ======================================================

    predicted_index = int(
        np.argmax(
            predictions
        )
    )


    predicted_class = class_names[
        predicted_index
    ]


    # ======================================================
    # Confidence
    # ======================================================

    confidence = float(
        predictions[
            predicted_index
        ] * 100
    )


    # ======================================================
    # Top 3 Predictions
    # ======================================================

    top_indices = np.argsort(
        predictions
    )[-3:][::-1]


    top_predictions = []


    for index in top_indices:

        top_predictions.append({

            "class": class_names[
                int(index)
            ],

            "confidence": round(
                float(
                    predictions[index] * 100
                ),
                2
            )

        })


    # ======================================================
    # Return Result
    # ======================================================

    return render_template(

        "index.html",

        prediction=predicted_class,

        confidence=round(
            confidence,
            2
        ),

        top_predictions=top_predictions,

        image=file.filename

    )


# ==========================================================
# Run Application
# ==========================================================

if __name__ == "__main__":

    print("=" * 70)

    print("Starting Flask Application")

    print("=" * 70)

    print()

    print(
        "Open: http://127.0.0.1:5000"
    )

    print()

    # Temporary debugging check
    print("Registered Routes:")

    print(app.url_map)

    print()

    app.run(
        debug=True
    )