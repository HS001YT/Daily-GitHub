# ==========================================================
# Day 325 - Transfer Learning Project
# MobileNetV2 Image Feature Extraction
# ==========================================================

import os
import numpy as np
import tensorflow as tf

from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import (
    preprocess_input,
    decode_predictions
)


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

os.makedirs(
    OTHER_FILES,
    exist_ok=True
)


# ==========================================================
# Configuration
# ==========================================================

IMAGE_SIZE = (224, 224)

MODEL_PATH = os.path.join(
    OTHER_FILES,
    "mobilenetv2_feature_extractor.keras"
)


# ==========================================================
# Load MobileNetV2
# ==========================================================

print("Loading MobileNetV2...")

model = MobileNetV2(
    weights="imagenet",
    include_top=True,
    input_shape=(224, 224, 3)
)

print("MobileNetV2 loaded successfully.")


# ==========================================================
# Save Model
# ==========================================================

model.save(
    MODEL_PATH
)

print("Model saved successfully.")


# ==========================================================
# Feature Extraction Model
# ==========================================================

feature_model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    pooling="avg",
    input_shape=(224, 224, 3)
)


FEATURE_MODEL_PATH = os.path.join(
    OTHER_FILES,
    "mobilenetv2_features.keras"
)

feature_model.save(
    FEATURE_MODEL_PATH
)

print("Feature extractor saved.")


# ==========================================================
# Display Model Information
# ==========================================================

print()
print("Model Information:")
print("Input size      :", IMAGE_SIZE)
print("Output classes  : 1000 ImageNet classes")
print("Feature vector  : 1280 values")
print("Model           : MobileNetV2")
print("Weights         : ImageNet")
print()


# ==========================================================
# Test with Random Image
# ==========================================================
# This is only a test to verify that the model works.
# No dataset is downloaded.

print("Testing model...")

random_image = np.random.randint(
    0,
    256,
    size=(1, 224, 224, 3),
    dtype=np.uint8
)

random_image = tf.cast(
    random_image,
    tf.float32
)

random_image = preprocess_input(
    random_image
)


# ==========================================================
# ImageNet Prediction
# ==========================================================

predictions = model.predict(
    random_image,
    verbose=0
)

decoded = decode_predictions(
    predictions,
    top=5
)[0]


print()
print("Sample ImageNet Predictions:")
print()

for _, class_name, probability in decoded:

    print(
        f"{class_name:<30} "
        f"{probability * 100:.2f}%"
    )


# ==========================================================
# Feature Extraction
# ==========================================================

features = feature_model.predict(
    random_image,
    verbose=0
)

print()
print(
    "Extracted Feature Vector Shape:",
    features.shape
)

print(
    "Feature Vector Length:",
    features.shape[1]
)


# ==========================================================
# Save Sample Feature Vector
# ==========================================================

FEATURE_PATH = os.path.join(
    OTHER_FILES,
    "sample_features.npy"
)

np.save(
    FEATURE_PATH,
    features
)


# ==========================================================
# Final Information
# ==========================================================

print()
print("=" * 60)
print("DAY 325 COMPLETED")
print("=" * 60)
print()

print("Generated files:")
print("1. mobilenetv2_feature_extractor.keras")
print("2. mobilenetv2_features.keras")
print("3. sample_features.npy")

print()
print("Transfer learning model is ready.")
print("No external dataset was used.")
print()