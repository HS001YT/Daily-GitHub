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

    "cifar10_model.keras"

)


# ==========================================================
# Class Names Path
# ==========================================================

CLASS_NAMES_PATH = os.path.join(

    OTHER_FILES,

    "class_names.pkl"

)


# ==========================================================
# Load CNN Model
# ==========================================================

print()

print("=" * 70)

print("LOADING CIFAR-10 MODEL")

print("=" * 70)

print()


if not os.path.exists(MODEL_PATH):

    raise FileNotFoundError(

        "Model file not found. "

        "Run train_model.py first."

    )


model = load_model(

    MODEL_PATH

)


print("CNN model loaded successfully.")

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


print("Class names loaded successfully.")

print()

print("Classes:")

for index, class_name in enumerate(

    class_names

):

    print(

        f"{index} : {class_name}"

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
# Image Prediction Route
# ==========================================================

@app.route(

    "/predict",

    methods=["POST"]

)

def predict():

    # ------------------------------------------------------
    # Check whether image was uploaded
    # ------------------------------------------------------

    if "image" not in request.files:

        return render_template(

            "index.html",

            error="Please select an image."

        )


    file = request.files["image"]


    # ------------------------------------------------------
    # Check filename
    # ------------------------------------------------------

    if file.filename == "":

        return render_template(

            "index.html",

            error="No image selected."

        )


    # ------------------------------------------------------
    # Check file extension
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

                "Unsupported image format. "

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

            error="Unable to read the uploaded image."

        )


    # ------------------------------------------------------
    # Convert to RGB
    # ------------------------------------------------------

    image = image.convert(

        "L"

    )


    # ------------------------------------------------------
    # Resize to CIFAR-10 Size
    # ------------------------------------------------------

    image = image.resize(

        (

            28,

            28

        )

    )


    # ------------------------------------------------------
    # Convert Image to NumPy Array
    # ------------------------------------------------------

    image_array = np.array(

        image,

        dtype="float32"

    )


    # ------------------------------------------------------
    # Normalize Pixel Values
    # ------------------------------------------------------

    image_array = image_array / 255.0


    # ------------------------------------------------------
    # Add Batch Dimension
    # ------------------------------------------------------

    image_array = np.expand_dims(

        image_array,

        axis=0

    )


    # ------------------------------------------------------
    # Make Prediction
    # ------------------------------------------------------

    predictions = model.predict(

        image_array,

        verbose=0

    )[0]


    # ------------------------------------------------------
    # Get Predicted Class
    # ------------------------------------------------------

    predicted_index = int(

        np.argmax(

            predictions

        )

    )


    predicted_class = class_names[

        predicted_index

    ]


    # ------------------------------------------------------
    # Get Confidence
    # ------------------------------------------------------

    confidence = float(

        predictions[predicted_index] * 100

    )


    # ------------------------------------------------------
    # Get Top 3 Predictions
    # ------------------------------------------------------

    top_indices = np.argsort(

        predictions

    )[-3:][::-1]


    top_predictions = []


    for index in top_indices:

        top_predictions.append(

            {

                "class": class_names[int(index)],

                "confidence": round(

                    float(

                        predictions[index] * 100

                    ),

                    2

                )

            }

        )


    # ------------------------------------------------------
    # Return Result
    # ------------------------------------------------------

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
# Run Flask Application
# ==========================================================

if __name__ == "__main__":

    print("=" * 70)

    print("STARTING CIFAR-10 IMAGE CLASSIFIER")

    print("=" * 70)

    print()

    print(

        "Open this address in your browser:"

    )

    print()

    print(

        "http://127.0.0.1:5000"

    )

    print()

    app.run(

        debug=True

    )