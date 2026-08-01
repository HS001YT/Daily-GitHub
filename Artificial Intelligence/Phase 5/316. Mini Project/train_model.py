import os
import pickle
import joblib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.callbacks import EarlyStopping

print("=" * 70)
print("STUDENT PERFORMANCE PREDICTOR")
print("=" * 70)

# ==========================================================
# Create Folders
# ==========================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATASET_FOLDER = os.path.join(
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

# ==========================================================
# Load Dataset
# ==========================================================

DATASET_PATH = os.path.join(
    DATASET_FOLDER,
    "student_performance.csv"
)

df = pd.read_csv(
    DATASET_PATH
)

print()
print("Dataset Loaded Successfully")
print()

print(df.head())

print()

print(df.info())

print()

# ==========================================================
# Remove Duplicate Records
# ==========================================================

df.drop_duplicates(
    inplace=True
)

print("Duplicates Removed")

# ==========================================================
# Target Column
# ==========================================================

TARGET_COLUMN = "Exam_Score"

X = df.drop(
    TARGET_COLUMN,
    axis=1
)

y = df[TARGET_COLUMN]

# ==========================================================
# Detect Column Types
# ==========================================================

categorical_columns = X.select_dtypes(
    include=["object"]
).columns.tolist()

numerical_columns = X.select_dtypes(
    exclude=["object"]
).columns.tolist()

print()

print("Categorical Columns")

print(categorical_columns)

print()

print("Numerical Columns")

print(numerical_columns)

print()

# ==========================================================
# Numerical Pipeline
# ==========================================================

numeric_pipeline = Pipeline(

    steps=[

        (

            "imputer",

            SimpleImputer(

                strategy="median"

            )

        ),

        (

            "scaler",

            StandardScaler()

        )

    ]

)

# ==========================================================
# Categorical Pipeline
# ==========================================================

categorical_pipeline = Pipeline(

    steps=[

        (

            "imputer",

            SimpleImputer(

                strategy="most_frequent"

            )

        ),

        (

            "encoder",

            OneHotEncoder(

                handle_unknown="ignore"

            )

        )

    ]

)

# ==========================================================
# Combine Pipelines
# ==========================================================

preprocessor = ColumnTransformer(

    transformers=[

        (

            "numeric",

            numeric_pipeline,

            numerical_columns

        ),

        (

            "categorical",

            categorical_pipeline,

            categorical_columns

        )

    ]

)

# ==========================================================
# Train Test Split
# ==========================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42

)

# ==========================================================
# Apply Preprocessing
# ==========================================================

X_train = preprocessor.fit_transform(
    X_train
)

X_test = preprocessor.transform(
    X_test
)

print()

print("Training Shape")

print(X_train.shape)

print()

print("Testing Shape")

print(X_test.shape)

print()

# ==========================================================
# Save Preprocessor
# ==========================================================

joblib.dump(

    preprocessor,

    os.path.join(

        OTHER_FILES,

        "preprocessor.pkl"

    )

)

print("Preprocessor Saved")

# ==========================================================
# Build Deep Learning Model
# ==========================================================

input_features = X_train.shape[1]

model = Sequential(

    [

        Dense(

            128,

            activation="relu",

            input_shape=(input_features,)

        ),

        Dropout(

            0.30

        ),

        Dense(

            64,

            activation="relu"

        ),

        Dropout(

            0.20

        ),

        Dense(

            32,

            activation="relu"

        ),

        Dense(

            1

        )

    ]

)

print()

print(model.summary())

# ==========================================================
# Compile Model
# ==========================================================

model.compile(

    optimizer="adam",

    loss="mse",

    metrics=[

        "mae"

    ]

)

# ==========================================================
# Early Stopping
# ==========================================================

early_stop = EarlyStopping(

    monitor="val_loss",

    patience=10,

    restore_best_weights=True

)

# ==========================================================
# Train Model
# ==========================================================

print()

print("=" * 70)

print("TRAINING MODEL")

print("=" * 70)

history = model.fit(

    X_train,

    y_train,

    validation_split=0.20,

    epochs=100,

    batch_size=32,

    callbacks=[

        early_stop

    ],

    verbose=1

)

print()

print("Training Completed")
# ==========================================================
# Evaluate Model
# ==========================================================

print()

print("=" * 70)

print("MODEL EVALUATION")

print("=" * 70)

loss, mae = model.evaluate(

    X_test,

    y_test,

    verbose=1

)

print()

print(f"Mean Squared Error : {loss:.4f}")

print(f"Mean Absolute Error : {mae:.4f}")

print()

predictions = model.predict(

    X_test,

    verbose=0

)

predictions = predictions.flatten()

print()

print("Sample Predictions")

print()

for actual, predicted in zip(

    y_test.iloc[:10],

    predictions[:10]

):

    print(

        f"Actual : {actual:.2f}   Predicted : {predicted:.2f}"

    )

print()

# ==========================================================
# Save Model
# ==========================================================

MODEL_PATH = os.path.join(

    OTHER_FILES,

    "student_model.keras"

)

model.save(

    MODEL_PATH

)

print("Model Saved")

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

print("History Saved")

from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)

# ==========================================================
# Regression Metrics
# ==========================================================

r2 = r2_score(

    y_test,

    predictions

)

mae_score = mean_absolute_error(

    y_test,

    predictions

)

mse = mean_squared_error(

    y_test,

    predictions

)

rmse = np.sqrt(

    mse

)

print()

print("=" * 70)

print("REGRESSION METRICS")

print("=" * 70)

print()

print(f"R² Score              : {r2:.4f}")

print(f"Mean Absolute Error   : {mae_score:.4f}")

print(f"Mean Squared Error    : {mse:.4f}")

print(f"Root Mean Square Error: {rmse:.4f}")

print()

# ==========================================================
# Plot Loss Curve
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

plt.grid(True)

plt.legend()

LOSS_GRAPH = os.path.join(

    OTHER_FILES,

    "loss_curve.png"

)

plt.savefig(

    LOSS_GRAPH,

    dpi=300,

    bbox_inches="tight"

)

plt.close()

print("Loss Graph Saved")

# ==========================================================
# Prediction Scatter Plot
# ==========================================================

plt.figure(

    figsize=(7,7)

)

plt.scatter(

    y_test,

    predictions,

    alpha=0.7

)

plt.plot(

    [

        y_test.min(),

        y_test.max()

    ],

    [

        y_test.min(),

        y_test.max()

    ],

    color="red",

    linewidth=2

)

plt.xlabel(

    "Actual Exam Score"

)

plt.ylabel(

    "Predicted Exam Score"

)

plt.title(

    "Actual vs Predicted"

)

plt.grid(True)

SCATTER_GRAPH = os.path.join(

    OTHER_FILES,

    "prediction_scatter.png"

)

plt.savefig(

    SCATTER_GRAPH,

    dpi=300,

    bbox_inches="tight"

)

plt.close()

print("Prediction Scatter Plot Saved")

# ==========================================================
# Save Metrics
# ==========================================================

metrics = {

    "R2 Score": float(r2),

    "MAE": float(mae_score),

    "MSE": float(mse),

    "RMSE": float(rmse)

}

METRICS_PATH = os.path.join(

    OTHER_FILES,

    "metrics.pkl"

)

with open(

    METRICS_PATH,

    "wb"

) as file:

    pickle.dump(

        metrics,

        file

    )

print("Metrics Saved")

# ==========================================================
# Final Report
# ==========================================================

print()

print("=" * 70)

print("TRAINING COMPLETED SUCCESSFULLY")

print("=" * 70)

print()

print(f"Dataset Shape : {df.shape}")

print()

print(f"Training Samples : {X_train.shape[0]}")

print(f"Testing Samples  : {X_test.shape[0]}")

print()

print(f"Input Features : {input_features}")

print()

print(f"Best Validation Loss : {min(history.history['val_loss']):.4f}")

print()

print(f"R² Score : {r2:.4f}")

print(f"RMSE     : {rmse:.4f}")

print()

print("Saved Files")

print("------------------------------------------")

print("student_model.keras")

print("preprocessor.pkl")

print("history.pkl")

print("metrics.pkl")

print("loss_curve.png")

print("prediction_scatter.png")

print()

print("=" * 70)