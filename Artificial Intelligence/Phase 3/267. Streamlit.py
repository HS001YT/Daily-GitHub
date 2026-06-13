# Run Application

# Open terminal:
#     streamlit run streamlit_app.py

# Output:

# Local URL:
#     http://localhost:8501

# Open in browser:
#     http://localhost:8501



import streamlit as st
import joblib
import os
import re


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

model = joblib.load(
    model_path
)

vectorizer = joblib.load(
    vectorizer_path
)

st.title(
    "Sentiment Analysis App"
)

st.write(
    "Enter a review and predict its sentiment."
)

review = st.text_area(
    "Enter Review"
)

if st.button(
    "Predict Sentiment"
):

    if review.strip() == "":

        st.warning(
            "Please enter some text."
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