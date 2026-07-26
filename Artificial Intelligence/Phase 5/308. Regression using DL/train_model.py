import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "housing.csv"
)

OTHER_FILES = os.path.join(
    BASE_DIR,
    "other_files"
)

os.makedirs(
    OTHER_FILES,
    exist_ok=True
)


df = pd.read_csv(DATASET_PATH)


print(df.head())

print(df.info())


# -----------------------------
# Remove rows having missing data
# -----------------------------

df = df.dropna()


# -----------------------------
# Remove categorical column
# -----------------------------

X = df.drop(
    [
        "median_house_value",
        "ocean_proximity"
    ],
    axis=1
)

y = df["median_house_value"]


# -----------------------------
# Scaling
# -----------------------------

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

joblib.dump(
    scaler,
    os.path.join(
        OTHER_FILES,
        "scaler.pkl"
    )
)


# -----------------------------
# Train Test Split
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(

    X_scaled,

    y,

    test_size=0.2,

    random_state=42

)


# -----------------------------
# Neural Network
# -----------------------------

model = Sequential(

    [

        Dense(
            128,
            activation="relu",
            input_shape=(X_train.shape[1],)
        ),

        Dense(
            64,
            activation="relu"
        ),

        Dense(
            32,
            activation="relu"
        ),

        Dense(
            16,
            activation="relu"
        ),

        Dense(
            1
        )

    ]

)


model.compile(

    optimizer="adam",

    loss="mse",

    metrics=["mae"]

)


early_stop = EarlyStopping(

    monitor="val_loss",

    patience=10,

    restore_best_weights=True

)


history = model.fit(

    X_train,

    y_train,

    validation_split=0.2,

    epochs=100,

    batch_size=32,

    callbacks=[early_stop],

    verbose=1

)


# -----------------------------
# Evaluation
# -----------------------------

predictions = model.predict(
    X_test,
    verbose=0
)


print("\n")

print(
    "Mean Absolute Error:",
    mean_absolute_error(
        y_test,
        predictions
    )
)

print(
    "Mean Squared Error:",
    mean_squared_error(
        y_test,
        predictions
    )
)

print(
    "R2 Score:",
    r2_score(
        y_test,
        predictions
    )
)


# -----------------------------
# Save Model
# -----------------------------

model.save(

    os.path.join(

        OTHER_FILES,

        "model.keras"

    )

)

print("\nModel Saved Successfully!")