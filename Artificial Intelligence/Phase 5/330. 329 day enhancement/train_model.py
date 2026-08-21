import os
import tensorflow as tf

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Conv2D,
    MaxPooling2D,
    BatchNormalization,
    Flatten,
    Dense,
    Dropout
)
from tensorflow.keras.callbacks import (
    EarlyStopping,
    ReduceLROnPlateau
)


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATASET_DIR = os.path.join(
    BASE_DIR,
    "dataset"
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
    "image_classifier.keras"
)


IMAGE_SIZE = (128, 128)
BATCH_SIZE = 32
EPOCHS = 30


print("Checking dataset...")


if not os.path.exists(DATASET_DIR):

    raise FileNotFoundError(
        "Dataset folder not found."
    )


print("Loading images...")


datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    validation_split=0.2,

    rotation_range=20,
    width_shift_range=0.15,
    height_shift_range=0.15,
    zoom_range=0.15,
    horizontal_flip=True
)


train_data = datagen.flow_from_directory(
    DATASET_DIR,
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="binary",
    subset="training",
    shuffle=True
)


validation_data = datagen.flow_from_directory(
    DATASET_DIR,
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="binary",
    subset="validation",
    shuffle=False
)


print()
print("Classes:")
print(train_data.class_indices)

print()
print(f"Training images: {train_data.samples}")
print(f"Validation images: {validation_data.samples}")


model = Sequential([

    tf.keras.Input(
        shape=(128, 128, 3)
    ),


    Conv2D(
        32,
        (3, 3),
        activation="relu"
    ),

    BatchNormalization(),

    MaxPooling2D(
        (2, 2)
    ),


    Conv2D(
        64,
        (3, 3),
        activation="relu"
    ),

    BatchNormalization(),

    MaxPooling2D(
        (2, 2)
    ),


    Conv2D(
        128,
        (3, 3),
        activation="relu"
    ),

    BatchNormalization(),

    MaxPooling2D(
        (2, 2)
    ),


    Conv2D(
        256,
        (3, 3),
        activation="relu"
    ),

    BatchNormalization(),

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
        1,
        activation="sigmoid"
    )

])


model.compile(
    optimizer=tf.keras.optimizers.Adam(
        learning_rate=0.001
    ),
    loss="binary_crossentropy",
    metrics=["accuracy"]
)


print()
print("Model summary:")
model.summary()


early_stopping = EarlyStopping(
    monitor="val_accuracy",
    patience=7,
    mode="max",
    restore_best_weights=True
)


reduce_lr = ReduceLROnPlateau(
    monitor="val_loss",
    factor=0.5,
    patience=3,
    min_lr=0.00001,
    verbose=1
)


print()
print("Starting training...")
print()


history = model.fit(
    train_data,
    validation_data=validation_data,
    epochs=EPOCHS,
    callbacks=[
        early_stopping,
        reduce_lr
    ],
    verbose=1
)


print()
print("Training completed.")


best_accuracy = max(
    history.history["val_accuracy"]
)


print(
    f"Best validation accuracy: "
    f"{best_accuracy * 100:.2f}%"
)


print()
print("Saving model...")


model.save(
    MODEL_PATH
)


print(
    f"Model saved: {MODEL_PATH}"
)

print()
print("Day 330 model training completed.")