import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression

import joblib
import os


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATASET_PATH = os.path.join(
    BASE_DIR,
    "spam.csv"
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
    "spam_model.pkl"
)

VECTORIZER_PATH = os.path.join(
    OTHER_FILES_DIR,
    "vectorizer.pkl"
)

data = pd.read_csv(
    DATASET_PATH,
    encoding="latin-1"
)

data = data[
    ["v1", "v2"]
]

data.columns = [
    "label",
    "message"
]

X = data["message"]

y = data["label"]

vectorizer = TfidfVectorizer(
    stop_words="english"
)

X_vectorized = vectorizer.fit_transform(
    X
)

X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression(
    max_iter=1000
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

joblib.dump(
    vectorizer,
    VECTORIZER_PATH
)

print(
    f"Accuracy: {accuracy:.2%}"
)

print(
    "Model Saved Successfully"
)