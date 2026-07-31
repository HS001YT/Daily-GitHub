import os
import pickle
from datetime import datetime

import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout

from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.callbacks import TensorBoard

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

LOG_DIR = os.path.join(
    BASE_DIR,
    "logs",
    datetime.now().strftime("%Y%m%d-%H%M%S")
)

os.makedirs(
    OTHER_FILES,
    exist_ok=True
)

os.makedirs(
    LOG_DIR,
    exist_ok=True
)

dataset = load_breast_cancer()

X = dataset.data

y = dataset.target

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42,

    stratify=y

)

scaler = StandardScaler()

X_train = scaler.fit_transform(
    X_train
)

X_test = scaler.transform(
    X_test
)

with open(

    os.path.join(

        OTHER_FILES,

        "scaler.pkl"

    ),

    "wb"

) as file:

    pickle.dump(

        scaler,

        file

    )

model = Sequential(

    [

        Dense(

            128,

            activation="relu",

            input_shape=(30,)

        ),

        Dropout(

            0.40

        ),

        Dense(

            64,

            activation="relu"

        ),

        Dropout(

            0.30

        ),

        Dense(

            32,

            activation="relu"

        ),

        Dense(

            1,

            activation="sigmoid"

        )

    ]

)

model.compile(

    optimizer="adam",

    loss="binary_crossentropy",

    metrics=[

        "accuracy"

    ]

)

early_stop = EarlyStopping(

    monitor="val_loss",

    patience=10,

    restore_best_weights=True

)

tensorboard = TensorBoard(

    log_dir=LOG_DIR,

    histogram_freq=1,

    write_graph=True,

    write_images=True,

    update_freq="epoch"

)

history = model.fit(

    X_train,

    y_train,

    validation_split=0.20,

    epochs=100,

    batch_size=16,

    callbacks=[

        early_stop,

        tensorboard

    ],

    verbose=1

)

# ==========================================================
# Evaluate Model
# ==========================================================

print()

print("=" * 60)

print("MODEL EVALUATION")

print("=" * 60)

loss, accuracy = model.evaluate(

    X_test,

    y_test,

    verbose=1

)

print()

print(f"Test Accuracy : {accuracy * 100:.2f}%")

print(f"Test Loss     : {loss:.4f}")

print()

# ==========================================================
# Save Model
# ==========================================================

MODEL_PATH = os.path.join(

    OTHER_FILES,

    "cancer_model.keras"

)

model.save(

    MODEL_PATH

)

print("Model Saved Successfully")

print()

# ==========================================================
# Save History
# ==========================================================

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

print("Training History Saved")

print()

# ==========================================================
# Accuracy Curve
# ==========================================================

plt.figure(

    figsize=(8,5)

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

    "Training vs Validation Accuracy"

)

plt.xlabel(

    "Epoch"

)

plt.ylabel(

    "Accuracy"

)

plt.legend()

plt.grid(True)

plt.savefig(

    os.path.join(

        OTHER_FILES,

        "accuracy_curve.png"

    ),

    dpi=300,

    bbox_inches="tight"

)

plt.close()

# ==========================================================
# Loss Curve
# ==========================================================

plt.figure(

    figsize=(8,5)

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

    "Training vs Validation Loss"

)

plt.xlabel(

    "Epoch"

)

plt.ylabel(

    "Loss"

)

plt.legend()

plt.grid(True)

plt.savefig(

    os.path.join(

        OTHER_FILES,

        "loss_curve.png"

    ),

    dpi=300,

    bbox_inches="tight"

)

plt.close()

# ==========================================================
# TensorBoard Information
# ==========================================================

print()

print("=" * 60)

print("TENSORBOARD LOGS CREATED")

print("=" * 60)

print()

print("Log Directory")

print(LOG_DIR)

print()

print("Start TensorBoard with")

print()

print("tensorboard --logdir logs")

print()

print("Open Browser")

print("http://localhost:6006")

print()

print("=" * 60)

# ==========================================================
# Final Report
# ==========================================================

print()

print("=" * 60)

print("TRAINING COMPLETED")

print("=" * 60)

print()

print("Model")

print(MODEL_PATH)

print()

print("Scaler")

print(

    os.path.join(

        OTHER_FILES,

        "scaler.pkl"

    )

)

print()

print("History")

print(HISTORY_PATH)

print()

print("Accuracy Graph")

print(

    os.path.join(

        OTHER_FILES,

        "accuracy_curve.png"

    )

)

print()

print("Loss Graph")

print(

    os.path.join(

        OTHER_FILES,

        "loss_curve.png"

    )

)

print()

print("TensorBoard Logs")

print(LOG_DIR)

print()

print("=" * 60)

