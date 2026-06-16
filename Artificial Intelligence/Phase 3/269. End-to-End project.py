# Open terminal:
#     streamlit run streamlit_app.py


import streamlit as st
import pandas as pd
import joblib
import os
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


def preprocess_text(text):

    text = text.lower()

    text = re.sub(
        r"\d+",
        "",
        text
    )

    text = re.sub(
        r"[^\w\s]",
        "",
        text
    )

    return text


def train_and_save_model():

    dataset_path = os.path.join(
        base_dir,
        "other_files",
        "sentiment_dataset.csv"
    )

    df = pd.read_csv(
        dataset_path
    )

    df["Review"] = (
        df["Review"]
        .apply(preprocess_text)
    )

    X = df["Review"]

    y = df["Sentiment"]

    vectorizer = TfidfVectorizer()

    X_vectorized = (
        vectorizer.fit_transform(X)
    )

    model = LogisticRegression()

    model.fit(
        X_vectorized,
        y
    )

    joblib.dump(
        model,
        model_path
    )

    joblib.dump(
        vectorizer,
        vectorizer_path
    )

    return model, vectorizer


base_dir = os.path.dirname(
    os.path.abspath(__file__)
)

model_path = os.path.join(
    base_dir,
    "other_files",
    "sentiment_model.joblib"
)

vectorizer_path = os.path.join(
    base_dir,
    "other_files",
    "vectorizer.joblib"
)

if (
    os.path.exists(model_path)
    and
    os.path.exists(vectorizer_path)
):

    model = joblib.load(
        model_path
    )

    vectorizer = joblib.load(
        vectorizer_path
    )

else:

    model, vectorizer = (
        train_and_save_model()
    )


st.title(
    "AI Sentiment Analysis System"
)

st.write(
    "Complete NLP + ML + UI Project"
)

review = st.text_area(
    "Enter Review"
)

if st.button(
    "Predict Sentiment"
):

    if review.strip() == "":

        st.warning(
            "Please enter a review."
        )

    else:

        review = preprocess_text(
            review
        )

        review_vector = (
            vectorizer.transform(
                [review]
            )
        )

        prediction = (
            model.predict(
                review_vector
            )[0]
        )

        st.success(
            f"Predicted Sentiment: {prediction}"
        )