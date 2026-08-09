# ==========================================================
# Day 322 - CNN Improvement
# Data Augmentation with Fashion-MNIST
# ==========================================================


# ==========================================================
# Imports
# ==========================================================

import os
import pickle

import numpy as np

import matplotlib.pyplot as plt

import tensorflow as tf

from tensorflow.keras import Sequential

from tensorflow.keras.layers import (
    Input,
    Conv2D,
    MaxPooling2D,
    Flatten,
    Dense,
    Dropout
)

from tensorflow.keras.preprocessing.image import ImageDataGenerator

from tensorflow.keras.callbacks import (
    EarlyStopping,
    ModelCheckpoint
)

from tensorflow.keras.datasets import fashion_mnist


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

os.makedirs(
    OTHER_FILES,
    exist_ok=True
)


# ==========================================================
# Random Seeds
# ==========================================================

np.random.seed(42)

tf.random.set_seed(42)


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


# ==========================================================
# Load Fashion-MNIST Dataset
# ==========================================================

print()

print("=" * 70)

print("LOADING FASHION-MNIST DATASET")

print("=" * 70)

print()


(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()


print(

    "Original Training Data:",

    X_train.shape

)

print(

    "Original Testing Data :",

    X_test.shape

)

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


print(

    "Using training images:",

    len(X_train)

)

print(

    "Using testing images :",

    len(X_test)

)

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
# Convert to Float32
# ==========================================================

X_train = X_train.astype(

    "float32"

)

X_test = X_test.astype(

    "float32"

)


# ==========================================================
# Normalize Pixel Values
# ==========================================================

X_train = X_train / 255.0

X_test = X_test / 255.0


print(

    "Training Shape:",

    X_train.shape

)

print(

    "Testing Shape :",

    X_test.shape

)

print()


# ==========================================================
# Data Augmentation
# ==========================================================

print("=" * 70)

print("CREATING DATA AUGMENTATION PIPELINE")

print("=" * 70)

print()


datagen = ImageDataGenerator(

    rotation_range=15,

    width_shift_range=0.10,

    height_shift_range=0.10,

    zoom_range=0.10,

    horizontal_flip=True

)


datagen.fit(

    X_train

)


print("Data augmentation configured.")

print()


# ==========================================================
# Visualize Augmented Images
# ==========================================================

sample_image = X_train[0]

sample_image = np.expand_dims(

    sample_image,

    axis=0

)


augmentation_generator = datagen.flow(

    sample_image,

    batch_size=1,

    shuffle=False

)


plt.figure(

    figsize=(10, 6)

)


for i in range(6):

    augmented_image = next(

        augmentation_generator

    )[0]

    augmented_image = augmented_image.squeeze()

    plt.subplot(

        2,

        3,

        i + 1

    )

    plt.imshow(

        augmented_image,

        cmap="gray"

    )

    plt.axis("off")

    plt.title(

        "Augmented Image"

    )


plt.tight_layout()


AUGMENTATION_IMAGE_PATH = os.path.join(

    OTHER_FILES,

    "data_augmentation_examples.png"

)


plt.savefig(

    AUGMENTATION_IMAGE_PATH,

    dpi=150,

    bbox_inches="tight"

)


plt.close()


print(

    "Augmentation visualization saved."

)

print()


# ==========================================================
# Build CNN Model
# ==========================================================

print("=" * 70)

print("BUILDING CNN MODEL")

print("=" * 70)

print()


model = Sequential([

    Input(

        shape=(28, 28, 1)

    ),

    Conv2D(

        32,

        (3, 3),

        activation="relu"

    ),

    MaxPooling2D(

        (2, 2)

    ),

    Conv2D(

        64,

        (3, 3),

        activation="relu"

    ),

    MaxPooling2D(

        (2, 2)

    ),

    Flatten(),

    Dense(

        128,

        activation="relu"

    ),

    Dropout(

        0.5

    ),

    Dense(

        10,

        activation="softmax"

    )

])


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


# ==========================================================
# Display Model
# ==========================================================

model.summary()


# ==========================================================
# Model Path
# ==========================================================

MODEL_PATH = os.path.join(

    OTHER_FILES,

    "fashion_mnist_augmented_model.keras"

)


# ==========================================================
# Callbacks
# ==========================================================

early_stopping = EarlyStopping(

    monitor="val_loss",

    patience=5,

    restore_best_weights=True

)


model_checkpoint = ModelCheckpoint(

    MODEL_PATH,

    monitor="val_accuracy",

    save_best_only=True,

    verbose=1

)


# ==========================================================
# Train Model
# ==========================================================

print()

print("=" * 70)

print("TRAINING CNN WITH DATA AUGMENTATION")

print("=" * 70)

print()


history = model.fit(

    datagen.flow(

        X_train,

        y_train,

        batch_size=64

    ),

    epochs=30,

    validation_data=(

        X_test,

        y_test

    ),

    callbacks=[

        early_stopping,

        model_checkpoint

    ],

    verbose=1

)


# ==========================================================
# Evaluate Model
# ==========================================================

print()

print("=" * 70)

print("MODEL EVALUATION")

print("=" * 70)

print()


loss, accuracy = model.evaluate(

    X_test,

    y_test,

    verbose=1

)


print()

print(

    f"Test Loss     : {loss:.4f}"

)

print(

    f"Test Accuracy : {accuracy:.4f}"

)

print(

    f"Test Accuracy : {accuracy * 100:.2f}%"

)

print()


# ==========================================================
# Predictions
# ==========================================================

predictions = model.predict(

    X_test,

    verbose=0

)


predicted_classes = np.argmax(

    predictions,

    axis=1

)


print()

print("=" * 70)

print("SAMPLE PREDICTIONS")

print("=" * 70)

print()


for i in range(10):

    actual = class_names[

        y_test[i]

    ]

    predicted = class_names[

        predicted_classes[i]

    ]

    confidence = (

        predictions[i][

            predicted_classes[i]

        ] * 100

    )


    print(

        f"Actual    : {actual}"

    )

    print(

        f"Predicted : {predicted}"

    )

    print(

        f"Confidence: {confidence:.2f}%"

    )

    print("-" * 50)


# ==========================================================
# Save Final Model
# ==========================================================

model.save(

    MODEL_PATH

)


print()

print(

    "Final model saved successfully."

)

print(

    f"Location: {MODEL_PATH}"

)

print()


# ==========================================================
# Accuracy Graph
# ==========================================================

plt.figure(

    figsize=(8, 5)

)


plt.plot(

    history.history["accuracy"],

    label="Training Accuracy"

)

plt.plot(

    history.history["val_accuracy"],

    label="Validation Accuracy"

)


plt.title(

    "CNN Accuracy with Data Augmentation"

)

plt.xlabel(

    "Epoch"

)

plt.ylabel(

    "Accuracy"

)

plt.legend()

plt.grid(

    True

)


ACCURACY_PATH = os.path.join(

    OTHER_FILES,

    "augmented_accuracy_curve.png"

)


plt.savefig(

    ACCURACY_PATH,

    dpi=150,

    bbox_inches="tight"

)


plt.close()


# ==========================================================
# Loss Graph
# ==========================================================

plt.figure(

    figsize=(8, 5)

)


plt.plot(

    history.history["loss"],

    label="Training Loss"

)

plt.plot(

    history.history["val_loss"],

    label="Validation Loss"

)


plt.title(

    "CNN Loss with Data Augmentation"

)

plt.xlabel(

    "Epoch"

)

plt.ylabel(

    "Loss"

)

plt.legend()

plt.grid(

    True

)


LOSS_PATH = os.path.join(

    OTHER_FILES,

    "augmented_loss_curve.png"

)


plt.savefig(

    LOSS_PATH,

    dpi=150,

    bbox_inches="tight"

)


plt.close()


# ==========================================================
# Final Information
# ==========================================================

print()

print("=" * 70)

print("DAY 322 COMPLETED")

print("=" * 70)

print()

print("Generated Files:")

print()

print(

    "1.",

    "fashion_mnist_augmented_model.keras"

)

print(

    "2.",

    "class_names.pkl"

)

print(

    "3.",

    "data_augmentation_examples.png"

)

print(

    "4.",

    "augmented_accuracy_curve.png"

)

print(

    "5.",

    "augmented_loss_curve.png"

)

print()

print(

    "CNN + Data Augmentation training completed."

)

print()