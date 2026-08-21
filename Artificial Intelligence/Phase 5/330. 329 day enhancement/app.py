import os
import uuid

import numpy as np
import tensorflow as tf

from PIL import Image
from flask import (
    Flask,
    render_template,
    request,
    send_from_directory
)
from werkzeug.utils import secure_filename


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "other_files",
    "image_classifier.keras"
)

UPLOAD_FOLDER = os.path.join(
    BASE_DIR,
    "uploads"
)

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


IMAGE_SIZE = (128, 128)

ALLOWED_EXTENSIONS = {
    "jpg",
    "jpeg",
    "png",
    "webp"
}

MAX_FILE_SIZE = 5 * 1024 * 1024


print("Loading model...")

model = tf.keras.models.load_model(
    MODEL_PATH
)

print("Model loaded successfully.")


app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = MAX_FILE_SIZE


def allowed_file(filename):

    return (
        "." in filename
        and filename.rsplit(
            ".",
            1
        )[1].lower()
        in ALLOWED_EXTENSIONS
    )


def preprocess_image(image_path):

    image = Image.open(
        image_path
    ).convert("RGB")

    image = image.resize(
        IMAGE_SIZE
    )

    image = np.array(
        image,
        dtype="float32"
    )

    image /= 255.0

    image = np.expand_dims(
        image,
        axis=0
    )

    return image


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


    if not allowed_file(
        file.filename
    ):

        return render_template(
            "index.html",
            error="Only JPG, JPEG, PNG and WEBP files are allowed."
        )


    extension = os.path.splitext(
        file.filename
    )[1].lower()


    filename = (
        f"{uuid.uuid4().hex}"
        f"{extension}"
    )


    filename = secure_filename(
        filename
    )


    image_path = os.path.join(
        UPLOAD_FOLDER,
        filename
    )


    try:

        file.save(
            image_path
        )


        image = preprocess_image(
            image_path
        )


        prediction = model.predict(
            image,
            verbose=0
        )[0][0]


        prediction = float(
            prediction
        )


        if prediction >= 0.5:

            predicted_class = "Dog"

            confidence = prediction * 100

        else:

            predicted_class = "Cat"

            confidence = (
                1 - prediction
            ) * 100


        return render_template(
            "index.html",
            prediction=predicted_class,
            confidence=round(
                confidence,
                2
            ),
            image_url=(
                f"/uploads/{filename}"
            )
        )


    except Exception as error:

        print(
            f"Prediction error: {error}"
        )


        if os.path.exists(
            image_path
        ):

            os.remove(
                image_path
            )


        return render_template(
            "index.html",
            error="Unable to process this image."
        )


@app.route(
    "/uploads/<filename>"
)
def uploaded_file(filename):

    return send_from_directory(
        UPLOAD_FOLDER,
        filename
    )


@app.errorhandler(413)
def file_too_large(error):

    return render_template(
        "index.html",
        error="Image size must be less than 5 MB."
    ), 413


if __name__ == "__main__":

    print()
    print("=" * 55)
    print("AI Image Classification Web App")
    print("=" * 55)
    print("Open: http://127.0.0.1:5000")
    print()

    app.run(
        debug=True
    )