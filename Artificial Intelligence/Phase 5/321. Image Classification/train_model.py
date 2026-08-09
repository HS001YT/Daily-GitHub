import os
import pickle

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import fashion_mnist


# ==========================================================
# Project Configuration
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


print("=" * 70)
print("CIFAR-10 IMAGE CLASSIFICATION")
print("=" * 70)

print()


# ==========================================================
# Class Names
# ==========================================================

class_names = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot"
]


# ==========================================================
# Save Class Names
# ==========================================================

CLASS_NAMES_PATH = os.path.join(

    OTHER_FILES,

    "class_names.pkl"

)

with open(

    CLASS_NAMES_PATH,

    "wb"

) as file:

    pickle.dump(

        class_names,

        file

    )


print("Class names saved.")

print()


# ==========================================================
# Load Fashion-MNIST Dataset
# ==========================================================

print("Loading Fashion-MNIST dataset...")

(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

print()
print("Dataset loaded.")
print()
print("Original Training Shape:", X_train.shape)
print("Original Testing Shape :", X_test.shape)
print()


# ==========================================================
# Use Small Dataset
# ==========================================================

TRAIN_SIZE = 5000
TEST_SIZE = 1000

X_train = X_train[:TRAIN_SIZE]

y_train = y_train[:TRAIN_SIZE]

X_test = X_test[:TEST_SIZE]

y_test = y_test[:TEST_SIZE]


print("Small dataset selected.")

print()

print("Training Images:", X_train.shape)

print("Testing Images :", X_test.shape)

print()

# ==========================================================
# Add Channel Dimension
# ==========================================================

X_train = np.expand_dims(

    X_train,

    axis=-1

)

X_test = np.expand_dims(

    X_test,

    axis=-1

)

# ==========================================================
# Convert Labels to 1D
# ==========================================================

y_train = y_train.flatten()

y_test = y_test.flatten()


print("Labels reshaped.")

print()

print("Training Labels Shape :", y_train.shape)

print("Testing Labels Shape  :", y_test.shape)

print()


# ==========================================================
# Normalize Pixel Values
# ==========================================================

X_train = X_train.astype("float32") / 255.0

X_test = X_test.astype("float32") / 255.0


print("Images normalized.")

print()

print(

    "Pixel value range:",

    X_train.min(),

    "to",

    X_train.max()

)

print()


# ==========================================================
# Display Dataset Information
# ==========================================================

print("=" * 70)
print("DATASET INFORMATION")
print("=" * 70)

print()

print("Number of Training Images :", len(X_train))

print("Number of Testing Images  :", len(X_test))

print("Image Height              :", X_train.shape[1])

print("Image Width               :", X_train.shape[2])

print("Color Channels            :", X_train.shape[3])

print("Number of Classes         :", len(class_names))

print()

print("Classes:")

for index, class_name in enumerate(class_names):

    print(

        f"{index} : {class_name}"

    )

print()


# ==========================================================
# Display Sample Images
# ==========================================================

plt.figure(

    figsize=(12, 8)

)

for i in range(20):

    plt.subplot(

        4,

        5,

        i + 1

    )

    plt.imshow(

        X_train[i]

    )

    plt.title(

        class_names[y_train[i]]

    )

    plt.axis("off")


plt.tight_layout()


SAMPLE_PATH = os.path.join(

    OTHER_FILES,

    "sample_images.png"

)

plt.savefig(

    SAMPLE_PATH,

    dpi=300,

    bbox_inches="tight"

)

plt.close()


print("Sample images saved.")

print()

print("=" * 70)
print("DATA PREPROCESSING COMPLETED")
print("=" * 70)

print()

print("Input Shape:", X_train.shape[1:])

print()

print("Ready for CNN training.")

# ==========================================================
# CNN Model
# ==========================================================

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import (
    Input,
    Conv2D,
    MaxPooling2D,
    Flatten,
    Dense,
    Dropout
)

from tensorflow.keras.callbacks import EarlyStopping


print("=" * 70)
print("BUILDING CNN MODEL")
print("=" * 70)

print()


# ==========================================================
# Create CNN Architecture
# ==========================================================

model = Sequential(

    [

        Input(
            shape=(28, 28, 1)
        ),

        # --------------------------------------------------
        # Convolution Block 1
        # --------------------------------------------------

        Conv2D(
            filters=32,
            kernel_size=(3, 3),
            activation="relu",
            padding="same"
        ),

        Conv2D(
            filters=32,
            kernel_size=(3, 3),
            activation="relu",
            padding="same"
        ),

        MaxPooling2D(
            pool_size=(2, 2)
        ),

        # --------------------------------------------------
        # Convolution Block 2
        # --------------------------------------------------

        Conv2D(
            filters=64,
            kernel_size=(3, 3),
            activation="relu",
            padding="same"
        ),

        Conv2D(
            filters=64,
            kernel_size=(3, 3),
            activation="relu",
            padding="same"
        ),

        MaxPooling2D(
            pool_size=(2, 2)
        ),

        # --------------------------------------------------
        # Convolution Block 3
        # --------------------------------------------------

        Conv2D(
            filters=128,
            kernel_size=(3, 3),
            activation="relu",
            padding="same"
        ),

        Conv2D(
            filters=128,
            kernel_size=(3, 3),
            activation="relu",
            padding="same"
        ),

        MaxPooling2D(
            pool_size=(2, 2)
        ),

        # --------------------------------------------------
        # Flatten
        # --------------------------------------------------

        Flatten(),

        # --------------------------------------------------
        # Fully Connected Layers
        # --------------------------------------------------

        Dense(
            256,
            activation="relu"
        ),

        Dropout(
            0.5
        ),

        Dense(
            10,
            activation="softmax"
        )

    ]

)


# ==========================================================
# Display Model Summary
# ==========================================================

print()

print("=" * 70)
print("CNN MODEL SUMMARY")
print("=" * 70)

print()

model.summary()

print()


# ==========================================================
# Compile Model
# ==========================================================

model.compile(

    optimizer="adam",

    loss="sparse_categorical_crossentropy",

    metrics=[

        "accuracy"

    ]

)


print("Model compiled successfully.")

print()


# ==========================================================
# Early Stopping
# ==========================================================

early_stopping = EarlyStopping(

    monitor="val_loss",

    patience=5,

    restore_best_weights=True

)


# ==========================================================
# Train Model
# ==========================================================

print("=" * 70)
print("TRAINING CNN MODEL")
print("=" * 70)

print()

history = model.fit(

    X_train,

    y_train,

    validation_split=0.20,

    epochs=30,

    batch_size=64,

    callbacks=[

        early_stopping

    ],

    verbose=1

)


print()

print("=" * 70)
print("TRAINING COMPLETED")
print("=" * 70)

print()


# ==========================================================
# Save Model
# ==========================================================

MODEL_PATH = os.path.join(

    OTHER_FILES,

    "cifar10_model.keras"

)

model.save(

    MODEL_PATH

)


print("Model saved successfully.")

print()

print(

    "Model Path:",

    MODEL_PATH

)

print()

# ==========================================================
# Evaluate Model
# ==========================================================

print("=" * 70)
print("MODEL EVALUATION")
print("=" * 70)

print()

test_loss, test_accuracy = model.evaluate(

    X_test,

    y_test,

    verbose=1

)

print()

print(f"Test Loss     : {test_loss:.4f}")

print(

    f"Test Accuracy : {test_accuracy * 100:.2f}%"

)

print()


# ==========================================================
# Generate Predictions
# ==========================================================

print("Generating predictions...")

predictions = model.predict(

    X_test,

    verbose=1

)

predicted_labels = np.argmax(

    predictions,

    axis=1

)

print()

print("Predictions generated successfully.")

print()


# ==========================================================
# Classification Report
# ==========================================================

from sklearn.metrics import classification_report

from sklearn.metrics import confusion_matrix


print("=" * 70)
print("CLASSIFICATION REPORT")
print("=" * 70)

print()

report = classification_report(

    y_test,

    predicted_labels,

    target_names=class_names

)

print(report)


# ==========================================================
# Save Classification Report
# ==========================================================

REPORT_PATH = os.path.join(

    OTHER_FILES,

    "classification_report.txt"

)

with open(

    REPORT_PATH,

    "w"

) as file:

    file.write(report)


print()

print(

    "Classification report saved:",

    REPORT_PATH

)

print()


# ==========================================================
# Confusion Matrix
# ==========================================================

print("=" * 70)
print("CREATING CONFUSION MATRIX")
print("=" * 70)

print()

cm = confusion_matrix(

    y_test,

    predicted_labels

)


plt.figure(

    figsize=(10, 8)

)

plt.imshow(

    cm,

    cmap="Blues"

)

plt.title(

    "CIFAR-10 Confusion Matrix"

)

plt.colorbar()

plt.xlabel(

    "Predicted Class"

)

plt.ylabel(

    "Actual Class"

)

plt.xticks(

    np.arange(len(class_names)),

    class_names,

    rotation=45,

    ha="right"

)

plt.yticks(

    np.arange(len(class_names)),

    class_names

)


for i in range(

    cm.shape[0]

):

    for j in range(

        cm.shape[1]

    ):

        plt.text(

            j,

            i,

            str(cm[i, j]),

            ha="center",

            va="center"

        )


plt.tight_layout()


CONFUSION_PATH = os.path.join(

    OTHER_FILES,

    "confusion_matrix.png"

)

plt.savefig(

    CONFUSION_PATH,

    dpi=300,

    bbox_inches="tight"

)

plt.close()


print(

    "Confusion matrix saved:",

    CONFUSION_PATH

)

print()


# ==========================================================
# Accuracy Curve
# ==========================================================

print("Creating accuracy curve...")

plt.figure(

    figsize=(10, 6)

)

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

plt.title(

    "Training and Validation Accuracy"

)

plt.xlabel(

    "Epoch"

)

plt.ylabel(

    "Accuracy"

)

plt.legend()

plt.grid(True)

plt.tight_layout()


ACCURACY_PATH = os.path.join(

    OTHER_FILES,

    "accuracy_curve.png"

)

plt.savefig(

    ACCURACY_PATH,

    dpi=300,

    bbox_inches="tight"

)

plt.close()


print(

    "Accuracy curve saved:",

    ACCURACY_PATH

)

print()


# ==========================================================
# Loss Curve
# ==========================================================

print("Creating loss curve...")

plt.figure(

    figsize=(10, 6)

)

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

plt.title(

    "Training and Validation Loss"

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


LOSS_PATH = os.path.join(

    OTHER_FILES,

    "loss_curve.png"

)

plt.savefig(

    LOSS_PATH,

    dpi=300,

    bbox_inches="tight"

)

plt.close()


print(

    "Loss curve saved:",

    LOSS_PATH

)

print()


# ==========================================================
# Sample Predictions
# ==========================================================

print("=" * 70)
print("SAMPLE PREDICTIONS")
print("=" * 70)

print()


for i in range(10):

    actual_class = class_names[

        y_test[i]

    ]

    predicted_class = class_names[

        predicted_labels[i]

    ]

    confidence = (

        np.max(

            predictions[i]

        ) * 100

    )

    print(

        f"Image {i + 1}"

    )

    print(

        f"Actual     : {actual_class}"

    )

    print(

        f"Predicted  : {predicted_class}"

    )

    print(

        f"Confidence : {confidence:.2f}%"

    )

    print(

        "-" * 40

    )


print()


# ==========================================================
# Final Summary
# ==========================================================

print("=" * 70)
print("CIFAR-10 MODEL TRAINING COMPLETED")
print("=" * 70)

print()

print(

    f"Final Test Accuracy : "

    f"{test_accuracy * 100:.2f}%"

)

print()

print("Generated Files:")

print()

print("1. cifar10_model.keras")

print("2. class_names.pkl")

print("3. sample_images.png")

print("4. classification_report.txt")

print("5. confusion_matrix.png")

print("6. accuracy_curve.png")

print("7. loss_curve.png")

print()

print("=" * 70)