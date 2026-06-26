from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

import joblib
import os

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

OTHER_FILES_DIR = os.path.join(
    BASE_DIR,
    "other_files"
)

os.makedirs(
    OTHER_FILES_DIR,
    exist_ok=True
)

MODEL_PATH = os.path.join(
    OTHER_FILES_DIR,
    "model.pkl"
)

X, y = load_iris(
    return_X_y=True
)

model = RandomForestClassifier()

model.fit(
    X,
    y
)

joblib.dump(
    model,
    MODEL_PATH
)

print(
    f"Model saved successfully at:\n{MODEL_PATH}"
)