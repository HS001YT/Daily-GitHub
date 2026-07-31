import os
import pickle

import matplotlib.pyplot as plt
import numpy as np

from tensorflow.keras.datasets import mnist

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import (
    Dense,
    Flatten,
    Dropout
)

from tensorflow.keras.callbacks import EarlyStopping

from tensorflow.keras.optimizers import Adam


# ==========================================================
# Create Folders
# ==========================================================

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


# ==========================================================
# Load Dataset
# ==========================================================

(x_train, y_train), (x_test, y_test) = mnist.load_data()


print("\nDataset Loaded Successfully\n")

print("Training Images :", x_train.shape)
print("Testing Images  :", x_test.shape)


# ==========================================================
# Normalize Images
# ==========================================================

x_train = x_train.astype(
    "float32"
) / 255.0

x_test = x_test.astype(
    "float32"
) / 255.0


print("\nNormalization Completed")


# ==========================================================
# Build Neural Network
# ==========================================================

model = Sequential(

    [

        Flatten(
            input_shape=(28, 28)
        ),

        Dense(
            256,
            activation="relu"
        ),

        Dropout(
            0.30
        ),

        Dense(
            128,
            activation="relu"
        ),

        Dropout(
            0.30
        ),

        Dense(
            64,
            activation="relu"
        ),

        Dropout(
            0.20
        ),

        Dense(
            10,
            activation="softmax"
        )

    ]

)


# ==========================================================
# Compile Model
# ==========================================================

model.compile(

    optimizer=Adam(

        learning_rate=0.001

    ),

    loss="sparse_categorical_crossentropy",

    metrics=[

        "accuracy"

    ]

)


print("\nModel Compiled Successfully\n")


# ==========================================================
# Early Stopping
# ==========================================================

early_stop = EarlyStopping(

    monitor="val_loss",

    patience=5,

    restore_best_weights=True,

    verbose=1

)


print("EarlyStopping Enabled\n")


# ==========================================================
# Model Summary
# ==========================================================

model.summary()


# ==========================================================
# Training Starts Here
# ==========================================================

history = model.fit(

    x_train,

    y_train,

    validation_split=0.20,

    epochs=50,

    batch_size=64,

    callbacks=[

        early_stop

    ],

    verbose=1

)

# ==========================================================
# Evaluate Model
# ==========================================================

print("\nEvaluating Model...\n")

test_loss, test_accuracy = model.evaluate(

    x_test,

    y_test,

    verbose=1

)

print("\n" + "=" * 50)

print("FINAL TEST RESULTS")

print("=" * 50)

print(f"Test Accuracy : {test_accuracy * 100:.2f}%")

print(f"Test Loss     : {test_loss:.4f}")

print("=" * 50)


# ==========================================================
# Plot Accuracy
# ==========================================================

plt.figure(figsize=(8, 5))

plt.plot(

    history.history["accuracy"],

    label="Training Accuracy",

    linewidth=2

)

plt.plot(

    history.history["val_accuracy"],

    label="Validation Accuracy",

    linewidth=2

)

plt.title("Training vs Validation Accuracy")

plt.xlabel("Epoch")

plt.ylabel("Accuracy")

plt.legend()

plt.grid(True)

accuracy_plot = os.path.join(

    OTHER_FILES,

    "accuracy_curve.png"

)

plt.savefig(

    accuracy_plot,

    dpi=300,

    bbox_inches="tight"

)

plt.close()


# ==========================================================
# Plot Loss
# ==========================================================

plt.figure(figsize=(8, 5))

plt.plot(

    history.history["loss"],

    label="Training Loss",

    linewidth=2

)

plt.plot(

    history.history["val_loss"],

    label="Validation Loss",

    linewidth=2

)

plt.title("Training vs Validation Loss")

plt.xlabel("Epoch")

plt.ylabel("Loss")

plt.legend()

plt.grid(True)

loss_plot = os.path.join(

    OTHER_FILES,

    "loss_curve.png"

)

plt.savefig(

    loss_plot,

    dpi=300,

    bbox_inches="tight"

)

plt.close()


# ==========================================================
# Save Model
# ==========================================================

model_path = os.path.join(

    OTHER_FILES,

    "digit_model.keras"

)

model.save(

    model_path

)


# ==========================================================
# Save Training History
# ==========================================================

history_path = os.path.join(

    OTHER_FILES,

    "history.pkl"

)

with open(

    history_path,

    "wb"

) as file:

    pickle.dump(

        history.history,

        file

    )


# ==========================================================
# Final Report
# ==========================================================

print("\n" + "=" * 50)

print("TRAINING COMPLETED SUCCESSFULLY")

print("=" * 50)

print()

print("Model Saved At")

print(model_path)

print()

print("History Saved At")

print(history_path)

print()

print("Accuracy Graph Saved At")

print(accuracy_plot)

print()

print("Loss Graph Saved At")

print(loss_plot)

print()

print("=" * 50)