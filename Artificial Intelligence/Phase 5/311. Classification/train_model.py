import os
import pickle
import joblib

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping


# ------------------------------------
# Paths
# ------------------------------------

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "diabetes.csv"
)

OTHER_FILES = os.path.join(
    BASE_DIR,
    "other_files"
)

os.makedirs(
    OTHER_FILES,
    exist_ok=True
)


# ------------------------------------
# Load Dataset
# ------------------------------------

df = pd.read_csv(DATASET_PATH)

print(df.head())

print()

print(df.info())


# ------------------------------------
# Features & Target
# ------------------------------------

X = df.drop(
    "Outcome",
    axis=1
)

y = df["Outcome"]


# ------------------------------------
# Feature Scaling
# ------------------------------------

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

joblib.dump(

    scaler,

    os.path.join(

        OTHER_FILES,

        "scaler.pkl"

    )

)


# ------------------------------------
# Train Test Split
# ------------------------------------

X_train, X_test, y_train, y_test = train_test_split(

    X_scaled,

    y,

    test_size=0.2,

    random_state=42,

    stratify=y

)


# ------------------------------------
# Neural Network
# ------------------------------------

model = Sequential(

    [

        Dense(

            64,

            activation="relu",

            input_shape=(8,)

        ),

        Dense(

            32,

            activation="relu"

        ),

        Dense(

            16,

            activation="relu"

        ),

        Dense(

            1,

            activation="sigmoid"

        )

    ]

)


# ------------------------------------
# Compile Model
# ------------------------------------

model.compile(

    optimizer="adam",

    loss="binary_crossentropy",

    metrics=[

        "accuracy"

    ]

)


# ------------------------------------
# Early Stopping
# ------------------------------------

early_stop = EarlyStopping(

    monitor="val_loss",

    patience=10,

    restore_best_weights=True

)


# ------------------------------------
# Train Model
# ------------------------------------

history = model.fit(

    X_train,

    y_train,

    validation_split=0.2,

    epochs=100,

    batch_size=16,

    callbacks=[early_stop],

    verbose=1

)


# ------------------------------------
# Save Model
# ------------------------------------

model.save(

    os.path.join(

        OTHER_FILES,

        "diabetes_model.keras"

    )

)


# ------------------------------------
# Save Training History
# ------------------------------------

with open(

    os.path.join(

        OTHER_FILES,

        "history.pkl"

    ),

    "wb"

) as file:

    pickle.dump(

        history.history,

        file

    )


# ------------------------------------
# Evaluation
# ------------------------------------

probabilities = model.predict(

    X_test,

    verbose=0

)

predictions = (

    probabilities > 0.5

).astype(int)


accuracy = accuracy_score(

    y_test,

    predictions

)

print()

print("=" * 45)

print("MODEL EVALUATION")

print("=" * 45)

print()

print(

    f"Accuracy : {accuracy * 100:.2f}%"

)

print()

print("Confusion Matrix")

print(

    confusion_matrix(

        y_test,

        predictions

    )

)

print()

print("Classification Report")

print(

    classification_report(

        y_test,

        predictions

    )

)


print()

print("=" * 45)

print("Model Saved Successfully")

print("=" * 45)