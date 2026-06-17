# Run to Install dependencies:
#     pip install -r requirements.txt

# Run app:
#     streamlit run app.py

# Open:
#     http://localhost:8501



import streamlit as st
import pandas as pd
import joblib
import os
import re
import nltk

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# =========================
# NLTK SETUP
# =========================

try:
    nltk.data.find("corpora/stopwords")
except:
    nltk.download("stopwords")

# =========================
# PATHS
# =========================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATASET_PATH = os.path.join(
    BASE_DIR,
    "other_files",
    "IMDB_Dataset.csv"
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "other_files",
    "sentiment_model.joblib"
)

VECTORIZER_PATH = os.path.join(
    BASE_DIR,
    "other_files",
    "vectorizer.joblib"
)

# =========================
# TEXT PREPROCESSING
# =========================

def preprocess_text(text):

    stemmer = PorterStemmer()

    text = str(text).lower()

    text = re.sub(
        r'[^a-zA-Z\s]',
        '',
        text
    )

    words = text.split()

    stop_words = set(
        stopwords.words("english")
    )

    words = [
        stemmer.stem(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)

# =========================
# TRAIN MODEL
# =========================

def train_model():

    df = pd.read_csv(
        DATASET_PATH
    )

    df["review"] = (
        df["review"]
        .apply(preprocess_text)
    )

    X = df["review"]

    y = df["sentiment"]

    X_train, X_test, y_train, y_test = (
        train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )
    )

    vectorizer = (
        TfidfVectorizer(
            max_features=10000
        )
    )

    X_train_vec = (
        vectorizer.fit_transform(
            X_train
        )
    )

    X_test_vec = (
        vectorizer.transform(
            X_test
        )
    )

    model = LogisticRegression(
        max_iter=1000
    )

    model.fit(
        X_train_vec,
        y_train
    )

    predictions = (
        model.predict(
            X_test_vec
        )
    )

    accuracy = (
        accuracy_score(
            y_test,
            predictions
        )
    )

    joblib.dump(
        model,
        MODEL_PATH
    )

    joblib.dump(
        vectorizer,
        VECTORIZER_PATH
    )

    return (
        model,
        vectorizer,
        accuracy
    )

# =========================
# LOAD MODEL
# =========================

def load_model():

    model = joblib.load(
        MODEL_PATH
    )

    vectorizer = joblib.load(
        VECTORIZER_PATH
    )

    return (
        model,
        vectorizer
    )

# =========================
# AUTO TRAIN
# =========================

if (
    not os.path.exists(
        MODEL_PATH
    )
    or
    not os.path.exists(
        VECTORIZER_PATH
    )
):

    model, vectorizer, accuracy = (
        train_model()
    )

else:

    model, vectorizer = (
        load_model()
    )

    accuracy = None

# =========================
# STREAMLIT UI
# =========================

st.set_page_config(
    page_title="AI Sentiment Analyzer",
    layout="centered"
)

st.title(
    "🎬 AI Sentiment Analyzer"
)

st.write(
    "Movie Review Sentiment Analysis using Machine Learning"
)

# =========================
# SIDEBAR
# =========================

st.sidebar.header(
    "Project Information"
)

st.sidebar.write(
    "Dataset: IMDb 50K Reviews"
)

st.sidebar.write(
    "Model: Logistic Regression"
)

st.sidebar.write(
    "Vectorizer: TF-IDF"
)

if accuracy is not None:

    st.sidebar.write(
        f"Accuracy: {accuracy:.2%}"
    )

# =========================
# USER INPUT
# =========================

review = st.text_area(
    "Enter Review"
)

# =========================
# PREDICT
# =========================

if st.button(
    "Predict Sentiment"
):

    if review.strip() == "":

        st.warning(
            "Please enter a review."
        )

    else:

        cleaned_review = (
            preprocess_text(
                review
            )
        )

        review_vector = (
            vectorizer.transform(
                [cleaned_review]
            )
        )

        prediction = (
            model.predict(
                review_vector
            )[0]
        )

        confidence = max(
            model.predict_proba(
                review_vector
            )[0]
        ) * 100

        if prediction.lower() == "positive":

            st.success(
                f"😊 Positive Review"
            )

        else:

            st.error(
                f"😞 Negative Review"
            )

        st.info(
            f"Confidence: {confidence:.2f}%"
        )

# =========================
# FOOTER
# =========================

st.markdown("---")

st.caption(
    "Phase 3 Final Project - NLP + Machine Learning + Streamlit"
)