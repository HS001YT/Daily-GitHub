import os
import pickle

import numpy as np

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.callbacks import EarlyStopping


# ---------------------------------------
# Create other_files folder
# ---------------------------------------

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

OTHER_FILES = os.path.join(
    BASE_DIR,
    "other_files"
)

os.makedirs(
    OTHER_FILES,
    exist_ok=True
)


# ---------------------------------------
# Load Dataset
# ---------------------------------------

(x_train, y_train), (x_test, y_test) = mnist.load_data()


print()

print("Training Images :", x_train.shape)

print("Testing Images :", x_test.shape)


# ---------------------------------------
# Normalize Images
# ---------------------------------------

x_train = x_train.astype("float32") / 255.0

x_test = x_test.astype("float32") / 255.0


# ---------------------------------------
# Build Neural Network
# ---------------------------------------

model = Sequential(

    [

        Flatten(
            input_shape=(28, 28)
        ),

        Dense(
            256,
            activation="relu"
        ),

        Dense(
            128,
            activation="relu"
        ),

        Dense(
            64,
            activation="relu"
        ),

        Dense(
            10,
            activation="softmax"
        )

    ]

)


# ---------------------------------------
# Compile
# ---------------------------------------

model.compile(

    optimizer="adam",

    loss="sparse_categorical_crossentropy",

    metrics=["accuracy"]

)


# ---------------------------------------
# Early Stopping
# ---------------------------------------

early_stop = EarlyStopping(

    monitor="val_loss",

    patience=5,

    restore_best_weights=True

)


# ---------------------------------------
# Train
# ---------------------------------------

history = model.fit(

    x_train,

    y_train,

    validation_split=0.2,

    epochs=20,

    batch_size=64,

    callbacks=[early_stop],

    verbose=1

)


# ---------------------------------------
# Evaluate
# ---------------------------------------

loss, accuracy = model.evaluate(

    x_test,

    y_test,

    verbose=0

)


print()

print("=" * 40)

print("TEST ACCURACY")

print("=" * 40)

print()

print(f"Accuracy : {accuracy*100:.2f}%")

print()

print(f"Loss : {loss:.4f}")

print()


# ---------------------------------------
# Save Model
# ---------------------------------------

MODEL_PATH = os.path.join(

    OTHER_FILES,

    "digit_model.keras"

)

model.save(

    MODEL_PATH

)


# ---------------------------------------
# Save History
# ---------------------------------------

HISTORY_PATH = os.path.join(

    OTHER_FILES,

    "history.pkl"

)

with open(

    HISTORY_PATH,

    "wb"

) as file:

    pickle.dump(

        history.history,

        file

    )


print("=" * 40)

print("MODEL SAVED SUCCESSFULLY")

print("=" * 40)

print()

print("Saved To")

print(MODEL_PATH)