import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

import joblib
import os


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATASET_PATH = os.path.join(
    BASE_DIR,
    "heart.csv"
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
    "heart_model.pkl"
)


data = pd.read_csv(
    DATASET_PATH
)

print("\nDataset Shape:")
print(data.shape)

print("\nColumns:")
print(data.columns)

X = data.drop(
    "condition",
    axis=1
)

y = data[
    "condition"
]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

accuracy = model.score(
    X_test,
    y_test
)

joblib.dump(
    model,
    MODEL_PATH
)

print(
    f"\nModel Accuracy: {accuracy:.2%}"
)

print(
    f"\nModel Saved Successfully:\n{MODEL_PATH}"
)