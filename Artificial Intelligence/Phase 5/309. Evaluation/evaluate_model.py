import os
import pickle
import joblib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

from tensorflow.keras.models import load_model


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "housing.csv"
)

OTHER_FILES = os.path.join(
    BASE_DIR,
    "other_files"
)


# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv(
    DATASET_PATH
)

df = df.dropna()


X = df.drop(
    [
        "median_house_value",
        "ocean_proximity"
    ],
    axis=1
)

y = df[
    "median_house_value"
]


# -----------------------------
# Load Scaler
# -----------------------------

scaler = joblib.load(

    os.path.join(

        OTHER_FILES,

        "scaler.pkl"

    )

)

X_scaled = scaler.transform(
    X
)


# -----------------------------
# Same Train/Test Split
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(

    X_scaled,

    y,

    test_size=0.2,

    random_state=42

)


# -----------------------------
# Load Model
# -----------------------------

model = load_model(

    os.path.join(

        OTHER_FILES,

        "model.keras"

    )

)


# -----------------------------
# Prediction
# -----------------------------

predictions = model.predict(

    X_test,

    verbose=0

).flatten()


# -----------------------------
# Metrics
# -----------------------------

mae = mean_absolute_error(

    y_test,

    predictions

)

mse = mean_squared_error(

    y_test,

    predictions

)

rmse = np.sqrt(
    mse
)

r2 = r2_score(

    y_test,

    predictions

)


print()

print("=" * 50)

print("MODEL EVALUATION")

print("=" * 50)

print()

print("MAE  :", mae)

print("MSE  :", mse)

print("RMSE :", rmse)

print("R²   :", r2)


# -----------------------------
# Save Metrics
# -----------------------------

with open(

    os.path.join(

        OTHER_FILES,

        "metrics.txt"

    ),

    "w"

) as file:

    file.write(

        f"MAE : {mae}\n"

    )

    file.write(

        f"MSE : {mse}\n"

    )

    file.write(

        f"RMSE : {rmse}\n"

    )

    file.write(

        f"R2 Score : {r2}\n"

    )


print()

print("metrics.txt Saved")


# -----------------------------
# Load History
# -----------------------------

with open(

    os.path.join(

        OTHER_FILES,

        "history.pkl"

    ),

    "rb"

) as file:

    history = pickle.load(
        file
    )


# -----------------------------
# Loss Curve
# -----------------------------

plt.figure(

    figsize=(8,5)

)

plt.plot(

    history["loss"],

    label="Training Loss"

)

plt.plot(

    history["val_loss"],

    label="Validation Loss"

)

plt.title(
    "Loss Curve"
)

plt.xlabel(
    "Epoch"
)

plt.ylabel(
    "Loss"
)

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig(

    os.path.join(

        OTHER_FILES,

        "loss_curve.png"

    )

)

plt.close()


print(
    "loss_curve.png Saved"
)


# -----------------------------
# Prediction vs Actual
# -----------------------------

plt.figure(

    figsize=(8,6)

)

plt.scatter(

    y_test,

    predictions,

    alpha=0.6

)

minimum = min(

    y_test.min(),

    predictions.min()

)

maximum = max(

    y_test.max(),

    predictions.max()

)

plt.plot(

    [minimum, maximum],

    [minimum, maximum],

    linestyle="--"

)

plt.xlabel(
    "Actual Price"
)

plt.ylabel(
    "Predicted Price"
)

plt.title(
    "Prediction vs Actual"
)

plt.grid(True)

plt.tight_layout()

plt.savefig(

    os.path.join(

        OTHER_FILES,

        "prediction_vs_actual.png"

    )

)

plt.close()


print(
    "prediction_vs_actual.png Saved"
)

print()

print("=" * 50)

print("Evaluation Completed Successfully")

print("=" * 50)