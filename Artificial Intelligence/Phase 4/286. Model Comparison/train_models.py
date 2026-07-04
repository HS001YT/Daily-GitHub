import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.tree import DecisionTreeClassifier

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

data = pd.read_csv(
    DATASET_PATH
)

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

models = {

    "Logistic Regression":
    LogisticRegression(
        max_iter=1000
    ),

    "Decision Tree":
    DecisionTreeClassifier(),

    "Random Forest":
    RandomForestClassifier()
}

for model_name, model in models.items():

    model.fit(
        X_train,
        y_train
    )

    accuracy = model.score(
        X_test,
        y_test
    )

    filename = model_name.lower().replace(
        " ",
        "_"
    ) + ".pkl"

    model_path = os.path.join(
        OTHER_FILES_DIR,
        filename
    )

    joblib.dump(
        model,
        model_path
    )

    print(
        f"{model_name}: {accuracy:.2%}"
    )