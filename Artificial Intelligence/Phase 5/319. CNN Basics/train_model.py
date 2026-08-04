import os
import pickle

import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.datasets import mnist

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout

from tensorflow.keras.utils import to_categorical

from tensorflow.keras.callbacks import EarlyStopping

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

print("=" * 70)
print("HANDWRITTEN DIGIT RECOGNITION USING CNN")
print("=" * 70)

# ==========================================================
# Create Folder
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

print()

print("Loading MNIST Dataset...")

(X_train, y_train), (X_test, y_test) = mnist.load_data()

print()

print("Dataset Loaded Successfully")

print()

print("Training Images :", X_train.shape)

print("Training Labels :", y_train.shape)

print()

print("Testing Images :", X_test.shape)

print("Testing Labels :", y_test.shape)

print()

# ==========================================================
# Normalize Images
# ==========================================================

X_train = X_train.astype(
    "float32"
) / 255.0

X_test = X_test.astype(
    "float32"
) / 255.0

print("Images Normalized")

print()

# ==========================================================
# Reshape Images
# ==========================================================

X_train = X_train.reshape(

    X_train.shape[0],

    28,

    28,

    1

)

X_test = X_test.reshape(

    X_test.shape[0],

    28,

    28,

    1

)

print("Images Reshaped")

print()

print("Training Shape")

print(X_train.shape)

print()

print("Testing Shape")

print(X_test.shape)

print()

# ==========================================================
# One Hot Encoding
# ==========================================================

y_train = to_categorical(

    y_train,

    10

)

y_test = to_categorical(

    y_test,

    10

)

print("Labels Converted To One-Hot Encoding")

print()

# ==========================================================
# Display Sample Images
# ==========================================================

plt.figure(

    figsize=(10,5)

)

for i in range(10):

    plt.subplot(

        2,

        5,

        i + 1

    )

    plt.imshow(

        X_train[i].reshape(28,28),

        cmap="gray"

    )

    plt.title(

        np.argmax(

            y_train[i]

        )

    )

    plt.axis("off")

plt.tight_layout()

plt.savefig(

    os.path.join(

        OTHER_FILES,

        "sample_images.png"

    ),

    dpi=300,

    bbox_inches="tight"

)

plt.close()

print("Sample Images Saved")

print()

# ==========================================================
# Build CNN Model
# ==========================================================

model = Sequential(

    [

        Input(

            shape=(28,28,1)

        ),

        Conv2D(

            filters=32,

            kernel_size=(3,3),

            activation="relu"

        ),

        MaxPooling2D(

            pool_size=(2,2)

        ),

        Conv2D(

            filters=64,

            kernel_size=(3,3),

            activation="relu"

        ),

        MaxPooling2D(

            pool_size=(2,2)

        ),

        Flatten(),

        Dense(

            128,

            activation="relu"

        ),

        Dropout(

            0.30

        ),

        Dense(

            10,

            activation="softmax"

        )

    ]

)

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

    loss="categorical_crossentropy",

    metrics=[

        "accuracy"

    ]

)

print("Model Compiled Successfully")

print()

# ==========================================================
# Early Stopping
# ==========================================================

early_stop = EarlyStopping(

    monitor="val_loss",

    patience=5,

    restore_best_weights=True

)

print("EarlyStopping Configured")

print()

# ==========================================================
# Train CNN
# ==========================================================

print("=" * 70)

print("TRAINING CNN MODEL")

print("=" * 70)

print()

history = model.fit(

    X_train,

    y_train,

    validation_split=0.20,

    epochs=20,

    batch_size=64,

    callbacks=[

        early_stop

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

    "cnn_digit_model.keras"

)

model.save(

    MODEL_PATH

)

print("CNN Model Saved Successfully")

print()

# ==========================================================
# Save Training History
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
# Evaluate Model
# ==========================================================

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

print(f"Test Loss     : {loss:.4f}")
print(f"Test Accuracy : {accuracy*100:.2f}%")

print()

# ==========================================================
# Predictions
# ==========================================================

print("Making Predictions...")

predictions = model.predict(

    X_test,

    verbose=0

)

predicted_labels = np.argmax(

    predictions,

    axis=1

)

true_labels = np.argmax(

    y_test,

    axis=1

)

print("Prediction Completed")

print()

# ==========================================================
# Display Sample Predictions
# ==========================================================

print("=" * 70)
print("SAMPLE PREDICTIONS")
print("=" * 70)

print()

for i in range(10):

    print(

        f"Image {i+1}"

    )

    print(

        f"Actual    : {true_labels[i]}"

    )

    print(

        f"Predicted : {predicted_labels[i]}"

    )

    print(

        f"Confidence: {np.max(predictions[i])*100:.2f}%"

    )

    print("-" * 40)

print()

# ==========================================================
# Classification Report
# ==========================================================

print("=" * 70)
print("CLASSIFICATION REPORT")
print("=" * 70)
print()

print(

    classification_report(

        true_labels,

        predicted_labels

    )

)

# ==========================================================
# Confusion Matrix
# ==========================================================

cm = confusion_matrix(

    true_labels,

    predicted_labels

)

plt.figure(

    figsize=(8,8)

)

plt.imshow(

    cm,

    cmap="Blues"

)

plt.title(

    "Confusion Matrix"

)

plt.colorbar()

plt.xlabel(

    "Predicted Label"

)

plt.ylabel(

    "True Label"

)

plt.xticks(

    np.arange(10)

)

plt.yticks(

    np.arange(10)

)

for i in range(cm.shape[0]):

    for j in range(cm.shape[1]):

        plt.text(

            j,

            i,

            str(cm[i, j]),

            ha="center",

            va="center",

            color="black"

        )

plt.tight_layout()

plt.savefig(

    os.path.join(

        OTHER_FILES,

        "confusion_matrix.png"

    ),

    dpi=300,

    bbox_inches="tight"

)

plt.close()

print("Confusion Matrix Saved")

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

plt.xlabel("Epoch")

plt.ylabel("Accuracy")

plt.title("Training vs Validation Accuracy")

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

print("Accuracy Curve Saved")

print()

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

plt.xlabel("Epoch")

plt.ylabel("Loss")

plt.title("Training vs Validation Loss")

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

print("Loss Curve Saved")

print()

# ==========================================================
# Final Report
# ==========================================================

print("=" * 70)
print("CNN TRAINING COMPLETED SUCCESSFULLY")
print("=" * 70)

print()

print(f"Training Images : {X_train.shape[0]}")
print(f"Testing Images  : {X_test.shape[0]}")

print()

print(f"Input Shape : {X_train.shape[1:]}")

print()

print(f"Final Accuracy : {accuracy*100:.2f}%")

print()

print("Generated Files")

print("--------------------------------------")

print("cnn_digit_model.keras")

print("history.pkl")

print("sample_images.png")

print("accuracy_curve.png")

print("loss_curve.png")

print("confusion_matrix.png")

print()

print("=" * 70)