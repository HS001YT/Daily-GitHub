# ==========================================================
# Day 323 - Transfer Learning
# Cats vs Dogs Classification using MobileNetV2
# ==========================================================


# ==========================================================
# Imports
# ==========================================================

import os
import random

import numpy as np

import matplotlib.pyplot as plt

import tensorflow as tf

from tensorflow.keras import layers

from tensorflow.keras import Model

from tensorflow.keras.applications import MobileNetV2

from tensorflow.keras.applications.mobilenet_v2 import (
    preprocess_input
)

from tensorflow.keras.preprocessing.image import (
    ImageDataGenerator
)

from tensorflow.keras.callbacks import (
    EarlyStopping,
    ModelCheckpoint
)


# ==========================================================
# Project Paths
# ==========================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATASET_DIR = os.path.join(
    BASE_DIR,
    "dataset"
)

CATS_DIR = os.path.join(
    DATASET_DIR,
    "cats"
)

DOGS_DIR = os.path.join(
    DATASET_DIR,
    "dogs"
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
# Configuration
# ==========================================================

IMAGE_SIZE = (
    160,
    160
)

BATCH_SIZE = 32

EPOCHS = 10

MAX_IMAGES_PER_CLASS = 1000

VALIDATION_SPLIT = 0.2

SEED = 42


# ==========================================================
# Random Seeds
# ==========================================================

random.seed(
    SEED
)

np.random.seed(
    SEED
)

tf.random.set_seed(
    SEED
)


# ==========================================================
# Check Dataset
# ==========================================================

print()

print("=" * 70)

print("DAY 323 - TRANSFER LEARNING")

print("=" * 70)

print()


if not os.path.exists(DATASET_DIR):

    raise FileNotFoundError(

        "Dataset folder not found.\n"

        "Create:\n"

        "dataset/cats/\n"

        "dataset/dogs/"

    )


if not os.path.exists(CATS_DIR):

    raise FileNotFoundError(

        "Cats folder not found:\n"

        + CATS_DIR

    )


if not os.path.exists(DOGS_DIR):

    raise FileNotFoundError(

        "Dogs folder not found:\n"

        + DOGS_DIR

    )


# ==========================================================
# Count Images
# ==========================================================

def count_images(folder):

    valid_extensions = (

        ".jpg",

        ".jpeg",

        ".png",

        ".bmp",

        ".webp"

    )

    count = 0

    for filename in os.listdir(folder):

        if filename.lower().endswith(
            valid_extensions
        ):

            count += 1

    return count


cat_count = count_images(
    CATS_DIR
)

dog_count = count_images(
    DOGS_DIR
)


print(
    "Cats available :",
    cat_count
)

print(
    "Dogs available :",
    dog_count
)

print()


# ==========================================================
# Limit Dataset Size
# ==========================================================

if cat_count < MAX_IMAGES_PER_CLASS:

    print(
        f"Warning: only {cat_count} cat images found."
    )

if dog_count < MAX_IMAGES_PER_CLASS:

    print(
        f"Warning: only {dog_count} dog images found."
    )


# ==========================================================
# Data Generators
# ==========================================================

print("=" * 70)

print("CREATING DATA GENERATORS")

print("=" * 70)

print()


train_datagen = ImageDataGenerator(

    preprocessing_function=preprocess_input,

    validation_split=VALIDATION_SPLIT,

    rotation_range=15,

    width_shift_range=0.10,

    height_shift_range=0.10,

    zoom_range=0.10,

    horizontal_flip=True

)


validation_datagen = ImageDataGenerator(

    preprocessing_function=preprocess_input,

    validation_split=VALIDATION_SPLIT

)


# ==========================================================
# Training Data
# ==========================================================

train_generator = train_datagen.flow_from_directory(

    DATASET_DIR,

    target_size=IMAGE_SIZE,

    batch_size=BATCH_SIZE,

    class_mode="binary",

    subset="training",

    shuffle=True,

    seed=SEED

)


# ==========================================================
# Validation Data
# ==========================================================

validation_generator = validation_datagen.flow_from_directory(

    DATASET_DIR,

    target_size=IMAGE_SIZE,

    batch_size=BATCH_SIZE,

    class_mode="binary",

    subset="validation",

    shuffle=False,

    seed=SEED

)


# ==========================================================
# Display Dataset Information
# ==========================================================

print()

print(
    "Training images :",
    train_generator.samples
)

print(
    "Validation images:",
    validation_generator.samples
)

print()

print(
    "Class mapping:",
    train_generator.class_indices
)

print()


# ==========================================================
# Load MobileNetV2
# ==========================================================

print("=" * 70)

print("LOADING PRETRAINED MOBILENETV2")

print("=" * 70)

print()


base_model = MobileNetV2(

    weights="imagenet",

    include_top=False,

    input_shape=(

        IMAGE_SIZE[0],

        IMAGE_SIZE[1],

        3

    )

)


# ==========================================================
# Freeze Pretrained Layers
# ==========================================================

base_model.trainable = False


print()

print(
    "Pretrained MobileNetV2 loaded."
)

print(
    "Pretrained layers frozen."
)

print()


# ==========================================================
# Build Transfer Learning Model
# ==========================================================

inputs = tf.keras.Input(

    shape=(

        IMAGE_SIZE[0],

        IMAGE_SIZE[1],

        3

    )

)


x = base_model(

    inputs,

    training=False

)


x = layers.GlobalAveragePooling2D()(

    x

)


x = layers.Dropout(

    0.3

)(

    x

)


outputs = layers.Dense(

    1,

    activation="sigmoid"

)(

    x

)


model = Model(

    inputs,

    outputs

)


# ==========================================================
# Compile Model
# ==========================================================

model.compile(

    optimizer=tf.keras.optimizers.Adam(

        learning_rate=0.0001

    ),

    loss="binary_crossentropy",

    metrics=[

        "accuracy"

    ]

)


# ==========================================================
# Model Summary
# ==========================================================

model.summary()


# ==========================================================
# Model Path
# ==========================================================

MODEL_PATH = os.path.join(

    OTHER_FILES,

    "transfer_learning_model.keras"

)


# ==========================================================
# Callbacks
# ==========================================================

early_stopping = EarlyStopping(

    monitor="val_loss",

    patience=3,

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

print("TRAINING TRANSFER LEARNING MODEL")

print("=" * 70)

print()


history = model.fit(

    train_generator,

    validation_data=validation_generator,

    epochs=EPOCHS,

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

    validation_generator,

    verbose=1

)


print()

print(
    f"Validation Loss     : {loss:.4f}"
)

print(
    f"Validation Accuracy : {accuracy:.4f}"
)

print(
    f"Validation Accuracy : {accuracy * 100:.2f}%"
)

print()


# ==========================================================
# Save Final Model
# ==========================================================

model.save(

    MODEL_PATH

)


print(
    "Model saved successfully."
)

print(
    f"Model path: {MODEL_PATH}"
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

    "Transfer Learning Accuracy"

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

    "transfer_learning_accuracy.png"

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

    "Transfer Learning Loss"

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

    "transfer_learning_loss.png"

)


plt.savefig(

    LOSS_PATH,

    dpi=150,

    bbox_inches="tight"

)

plt.close()


# ==========================================================
# Save Class Names
# ==========================================================

CLASS_NAMES = [

    "cat",

    "dog"

]


CLASS_NAMES_PATH = os.path.join(

    OTHER_FILES,

    "class_names.npy"

)


np.save(

    CLASS_NAMES_PATH,

    np.array(CLASS_NAMES)

)


# ==========================================================
# Final Information
# ==========================================================

print()

print("=" * 70)

print("DAY 323 COMPLETED")

print("=" * 70)

print()

print("Generated files:")

print()

print(
    "1. transfer_learning_model.keras"
)

print(
    "2. transfer_learning_accuracy.png"
)

print(
    "3. transfer_learning_loss.png"
)

print(
    "4. class_names.npy"
)

print()

print(
    "Transfer learning training completed."
)

print()