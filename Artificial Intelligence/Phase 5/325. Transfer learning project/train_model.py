# ==========================================================
# Day 325 - Transfer Learning Project
# MobileNetV2 Image Classifier
# ==========================================================

import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow.keras import layers, Model
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.datasets import cifar10


# ==========================================================
# Paths
# ==========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OTHER_FILES = os.path.join(BASE_DIR, "other_files")
os.makedirs(OTHER_FILES, exist_ok=True)

MODEL_PATH = os.path.join(OTHER_FILES, "mobilenet_classifier.keras")


# ==========================================================
# Configuration
# ==========================================================

IMG_SIZE = 96
BATCH_SIZE = 32
TRAIN_PER_CLASS = 300
TEST_PER_CLASS = 100
EPOCHS = 5
SEED = 42

np.random.seed(SEED)
tf.random.set_seed(SEED)


# ==========================================================
# Load CIFAR-10
# ==========================================================

print("Loading small CIFAR-10 dataset...")

(X_train, y_train), (X_test, y_test) = cifar10.load_data()

print("CIFAR-10 loaded.")


# ==========================================================
# Select Airplane and Automobile
# CIFAR labels:
# 0 = airplane
# 1 = automobile
# ==========================================================

train_mask = np.isin(
    y_train.flatten(),
    [0, 1]
)

test_mask = np.isin(
    y_test.flatten(),
    [0, 1]
)

X_train = X_train[train_mask]
y_train = y_train[train_mask].flatten()

X_test = X_test[test_mask]
y_test = y_test[test_mask].flatten()


# ==========================================================
# Keep Small Dataset
# ==========================================================

def select_samples(X, y, count):
    indexes = []

    for label in [0, 1]:
        label_indexes = np.where(y == label)[0]
        indexes.extend(label_indexes[:count])

    indexes = np.array(indexes)
    np.random.shuffle(indexes)

    return X[indexes], y[indexes]


X_train, y_train = select_samples(
    X_train,
    y_train,
    TRAIN_PER_CLASS
)

X_test, y_test = select_samples(
    X_test,
    y_test,
    TEST_PER_CLASS
)

print(f"Training images: {len(X_train)}")
print(f"Testing images: {len(X_test)}")


# ==========================================================
# Convert Labels
# airplane = 0
# automobile = 1
# ==========================================================

class_names = np.array([
    "airplane",
    "automobile"
])

np.save(
    os.path.join(OTHER_FILES, "class_names.npy"),
    class_names
)


# ==========================================================
# Resize Images
# ==========================================================

X_train = tf.image.resize(
    X_train,
    (IMG_SIZE, IMG_SIZE)
)

X_test = tf.image.resize(
    X_test,
    (IMG_SIZE, IMG_SIZE)
)

X_train = preprocess_input(
    tf.cast(X_train, tf.float32)
)

X_test = preprocess_input(
    tf.cast(X_test, tf.float32)
)


# ==========================================================
# MobileNetV2
# ==========================================================

print("Loading MobileNetV2...")

base_model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    input_shape=(IMG_SIZE, IMG_SIZE, 3)
)

base_model.trainable = False

print("MobileNetV2 loaded.")


# ==========================================================
# Build Model
# ==========================================================

inputs = tf.keras.Input(
    shape=(IMG_SIZE, IMG_SIZE, 3)
)

x = base_model(
    inputs,
    training=False
)

x = layers.GlobalAveragePooling2D()(x)

x = layers.Dropout(0.3)(x)

outputs = layers.Dense(
    1,
    activation="sigmoid"
)(x)

model = Model(
    inputs,
    outputs
)


# ==========================================================
# Compile
# ==========================================================

model.compile(
    optimizer=tf.keras.optimizers.Adam(
        learning_rate=0.0001
    ),
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

model.summary()


# ==========================================================
# Callbacks
# ==========================================================

checkpoint = ModelCheckpoint(
    MODEL_PATH,
    monitor="val_accuracy",
    save_best_only=True,
    verbose=1
)

early_stopping = EarlyStopping(
    monitor="val_loss",
    patience=2,
    restore_best_weights=True
)


# ==========================================================
# Train Classification Head
# ==========================================================

print("Training classification head...")

history = model.fit(
    X_train,
    y_train,
    validation_data=(X_test, y_test),
    epochs=EPOCHS,
    batch_size=BATCH_SIZE,
    callbacks=[
        checkpoint,
        early_stopping
    ],
    verbose=1
)


# ==========================================================
# Fine-Tuning
# ==========================================================

print("Starting fine-tuning...")

base_model.trainable = True

for layer in base_model.layers[:-20]:
    layer.trainable = False

model.compile(
    optimizer=tf.keras.optimizers.Adam(
        learning_rate=0.00001
    ),
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

model.fit(
    X_train,
    y_train,
    validation_data=(X_test, y_test),
    epochs=3,
    batch_size=BATCH_SIZE,
    callbacks=[
        checkpoint,
        early_stopping
    ],
    verbose=1
)


# ==========================================================
# Evaluation
# ==========================================================

loss, accuracy = model.evaluate(
    X_test,
    y_test,
    verbose=0
)

print(f"Test Loss: {loss:.4f}")
print(f"Test Accuracy: {accuracy * 100:.2f}%")


# ==========================================================
# Save Model
# ==========================================================

model.save(MODEL_PATH)

print("Model saved successfully.")


# ==========================================================
# Accuracy Graph
# ==========================================================

plt.figure(figsize=(8, 5))

plt.plot(
    history.history["accuracy"],
    label="Training Accuracy"
)

plt.plot(
    history.history["val_accuracy"],
    label="Validation Accuracy"
)

plt.title("MobileNetV2 Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)

plt.savefig(
    os.path.join(
        OTHER_FILES,
        "accuracy.png"
    ),
    dpi=150,
    bbox_inches="tight"
)

plt.close()


# ==========================================================
# Loss Graph
# ==========================================================

plt.figure(figsize=(8, 5))

plt.plot(
    history.history["loss"],
    label="Training Loss"
)

plt.plot(
    history.history["val_loss"],
    label="Validation Loss"
)

plt.title("MobileNetV2 Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)

plt.savefig(
    os.path.join(
        OTHER_FILES,
        "loss.png"
    ),
    dpi=150,
    bbox_inches="tight"
)

plt.close()


# ==========================================================
# Done
# ==========================================================

print("Day 325 completed.")
print("Model: MobileNetV2")
print("Classes: Airplane, Automobile")
print("Transfer learning + fine-tuning completed.")
print("Saved in other_files.")