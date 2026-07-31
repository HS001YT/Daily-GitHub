import os
import pickle
import numpy as np

from tensorflow.keras.models import load_model


# ==========================================================
# Paths
# ==========================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

OTHER_FILES = os.path.join(
    BASE_DIR,
    "other_files"
)


# ==========================================================
# Load Model
# ==========================================================

MODEL_PATH = os.path.join(
    OTHER_FILES,
    "cancer_model.keras"
)

model = load_model(
    MODEL_PATH
)

print("Deep Learning Model Loaded Successfully")


# ==========================================================
# Load Scaler
# ==========================================================

SCALER_PATH = os.path.join(
    OTHER_FILES,
    "scaler.pkl"
)

with open(
    SCALER_PATH,
    "rb"
) as file:

    scaler = pickle.load(file)

print("Scaler Loaded Successfully")


# ==========================================================
# Feature Names
# ==========================================================

feature_names = [

    "mean_radius",
    "mean_texture",
    "mean_perimeter",
    "mean_area",
    "mean_smoothness",
    "mean_compactness",
    "mean_concavity",
    "mean_concave_points",
    "mean_symmetry",
    "mean_fractal_dimension",

    "radius_error",
    "texture_error",
    "perimeter_error",
    "area_error",
    "smoothness_error",
    "compactness_error",
    "concavity_error",
    "concave_points_error",
    "symmetry_error",
    "fractal_dimension_error",

    "worst_radius",
    "worst_texture",
    "worst_perimeter",
    "worst_area",
    "worst_smoothness",
    "worst_compactness",
    "worst_concavity",
    "worst_concave_points",
    "worst_symmetry",
    "worst_fractal_dimension"

]


# ==========================================================
# Take Input
# ==========================================================

print()

print("=" * 60)

print("BREAST CANCER PREDICTION")

print("=" * 60)

print()

values = []

for feature in feature_names:

    value = float(

        input(

            f"{feature} : "

        )

    )

    values.append(
        value
    )


# ==========================================================
# Prepare Data
# ==========================================================

values = np.array(

    values

).reshape(

    1,

    -1

)

values = scaler.transform(

    values

)


# ==========================================================
# Prediction
# ==========================================================

probability = model.predict(

    values,

    verbose=0

)[0][0]


if probability >= 0.5:

    prediction = "Benign (No Cancer)"

    confidence = probability * 100

else:

    prediction = "Malignant (Cancer)"

    confidence = (1 - probability) * 100


# ==========================================================
# Result
# ==========================================================

print()

print("=" * 60)

print("PREDICTION RESULT")

print("=" * 60)

print()

print("Prediction :")

print(prediction)

print()

print(f"Confidence : {confidence:.2f}%")

print()

print("=" * 60)