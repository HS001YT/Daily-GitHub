import pandas as pd
from sklearn.linear_model import LinearRegression

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
    "house_price_model.pkl"
)

DATASET_PATH = os.path.join(
    BASE_DIR,
    "house_data.csv"
)

data = pd.read_csv(
    DATASET_PATH
)

X = data[
    [
        "Area",
        "Bedrooms",
        "Age"
    ]
]

y = data[
    "Price"
]

model = LinearRegression()

model.fit(
    X,
    y
)

joblib.dump(
    model,
    MODEL_PATH
)

print(
    "Model Saved Successfully"
)