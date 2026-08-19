# ==========================================================
# Day 327 - Sentiment Analysis using Deep Learning
# ==========================================================

import os
import json
import numpy as np
import tensorflow as tf

from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Embedding,
    LSTM,
    Dense,
    Dropout
)
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.callbacks import EarlyStopping


# ==========================================================
# Configuration
# ==========================================================

VOCAB_SIZE = 10000
MAX_LENGTH = 200
BATCH_SIZE = 32
EPOCHS = 30

TRAIN_SIZE = 2000
TEST_SIZE = 500

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


MODEL_PATH = os.path.join(
    OTHER_FILES,
    "sentiment_model.keras"
)

WORD_INDEX_PATH = os.path.join(
    OTHER_FILES,
    "word_index.json"
)


# ==========================================================
# Load Dataset
# ==========================================================

print("Loading IMDB dataset...")

(X_train, y_train), (X_test, y_test) = imdb.load_data(
    num_words=VOCAB_SIZE
)

print("Dataset loaded.")


# ==========================================================
# Use Small Dataset
# ==========================================================

X_train = X_train[:TRAIN_SIZE]
y_train = y_train[:TRAIN_SIZE]

X_test = X_test[:TEST_SIZE]
y_test = y_test[:TEST_SIZE]

print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")


# ==========================================================
# Padding
# ==========================================================

X_train = pad_sequences(
    X_train,
    maxlen=MAX_LENGTH,
    padding="post",
    truncating="post"
)

X_test = pad_sequences(
    X_test,
    maxlen=MAX_LENGTH,
    padding="post",
    truncating="post"
)

print("Sequences padded.")


# ==========================================================
# Build LSTM Model
# ==========================================================

model = Sequential([
    tf.keras.Input(
        shape=(MAX_LENGTH,)
    ),

    Embedding(
        input_dim=VOCAB_SIZE,
        output_dim=64
    ),

    LSTM(
        64
    ),

    Dropout(
        0.5
    ),

    Dense(
        1,
        activation="sigmoid"
    )
])


# ==========================================================
# Compile
# ==========================================================

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)


print()
print("Model created.")
model.summary()


# ==========================================================
# Train
# ==========================================================

print()
print("Starting training...")

history = model.fit(
    X_train,
    y_train,
    validation_split=0.2,
    epochs=EPOCHS,
    batch_size=BATCH_SIZE,
    verbose=1
)


# ==========================================================
# Evaluate
# ==========================================================

print()
print("Evaluating model...")

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

model.save(
    MODEL_PATH
)

print()
print("Model saved.")


# ==========================================================
# Save Word Index
# ==========================================================

word_index = imdb.get_word_index()

with open(
    WORD_INDEX_PATH,
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        word_index,
        file
    )

print("Word index saved.")


# ==========================================================
# Sample Predictions
# ==========================================================

predictions = model.predict(
    X_test[:10],
    verbose=0
).flatten()


print()
print("Sample Predictions")
print("-" * 50)

for actual, predicted in zip(
    y_test[:10],
    predictions
):

    sentiment = (
        "Positive"
        if predicted >= 0.5
        else "Negative"
    )

    print(
        f"Actual: {actual} | "
        f"Predicted: {sentiment} | "
        f"Confidence: {predicted * 100:.2f}%"
    )


print()
print("=" * 60)
print("DAY 327 TRAINING COMPLETED")
print("=" * 60)