import json
import os
from datetime import datetime
import pickle


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


# ==========================================================
# Load Training History
# ==========================================================

history_path = os.path.join(
    OTHER_FILES,
    "history.pkl"
)

with open(
    history_path,
    "rb"
) as file:

    history = pickle.load(file)


# ==========================================================
# Extract Metrics
# ==========================================================

best_accuracy = max(
    history["val_accuracy"]
)

best_loss = min(
    history["val_loss"]
)

epochs = len(
    history["accuracy"]
)


# ==========================================================
# Metadata
# ==========================================================

metadata = {

    "model_name": "Breast Cancer Detection",

    "version": "1.0",

    "framework": "TensorFlow",

    "dataset": "Breast Cancer Wisconsin",

    "problem_type": "Binary Classification",

    "accuracy": round(
        best_accuracy * 100,
        2
    ),

    "loss": round(
        best_loss,
        4
    ),

    "epochs": epochs,

    "created_on": datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )

}


# ==========================================================
# Save Metadata
# ==========================================================

metadata_path = os.path.join(
    OTHER_FILES,
    "metadata.json"
)

with open(
    metadata_path,
    "w"
) as file:

    json.dump(

        metadata,

        file,

        indent=4

    )


print("=" * 60)

print("MODEL METADATA GENERATED")

print("=" * 60)

print()

print("Saved At")

print(metadata_path)

print()

print(json.dumps(
    metadata,
    indent=4
))