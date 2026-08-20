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

CLASS_NAMES = {
    0: "Cat",
    1: "Dog"
}


app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


print("Loading image classification model...")

model = tf.keras.models.load_model(
    MODEL_PATH
)

print("Model loaded successfully.")


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

    image = image / 255.0

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

@app.route("/uploads/<filename>")
def uploaded_file(filename):

    return send_from_directory(
        UPLOAD_FOLDER,
        filename
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


    extension = os.path.splitext(
        file.filename
    )[1].lower()


    allowed_extensions = [
        ".jpg",
        ".jpeg",
        ".png",
        ".webp"
    ]


    if extension not in allowed_extensions:

        return render_template(
            "index.html",
            error="Please upload JPG, JPEG, PNG or WEBP."
        )


    filename = (
        f"{uuid.uuid4().hex}"
        f"{extension}"
    )


    image_path = os.path.join(
        UPLOAD_FOLDER,
        filename
    )


    file.save(
        image_path
    )


    try:

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

            confidence = (1 - prediction) * 100


        image_url = (
            f"/uploads/{filename}"
        )


        return render_template(
            "index.html",
            prediction=predicted_class,
            confidence=round(
                confidence,
                2
            ),
            image_url=image_url
        )


    except Exception as error:

        if os.path.exists(
            image_path
        ):

            os.remove(
                image_path
            )


        return render_template(
            "index.html",
            error=f"Prediction failed: {error}"
        )


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