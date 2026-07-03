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
    "diabetes.csv"
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
    "diabetes_model.pkl"
)

data = pd.read_csv(
    DATASET_PATH
)

X = data.drop(
    "Outcome",
    axis=1
)

y = data["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    random_state=42
)

model.fit(
    X_train,
    y_train
)

joblib.dump(
    model,
    MODEL_PATH
)

print(
    "Model Saved Successfully"
)