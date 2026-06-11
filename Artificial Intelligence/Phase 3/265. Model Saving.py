def load_dataset():
    import pandas as pd
    import os

    try:
        file = input(
            "Enter CSV file path (e.g., other_files/sentiment_dataset.csv): "
        ).strip()

        base_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(base_dir, file)

        df = pd.read_csv(full_path)

        print("\nDataset Loaded Successfully.\n")

        return df

    except FileNotFoundError:
        print("File not found.")
        return None

    except Exception as e:
        print("Error:", e)
        return None


def preprocess_text(text):

    import re

    text = text.lower()

    text = re.sub(r"\d+", "", text)

    text = re.sub(r"[^\w\s]", "", text)

    return text


def train_model(df):

    try:
        from sklearn.feature_extraction.text import (
            TfidfVectorizer
        )

        from sklearn.linear_model import (
            LogisticRegression
        )

        df = df.copy()

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

        print(
            "\nModel Trained Successfully."
        )

        return model, vectorizer

    except Exception as e:

        print("Error:", e)

        return None, None


def save_using_pickle(model, vectorizer):

    try:

        import pickle

        with open(
            "sentiment_model.pkl",
            "wb"
        ) as file:

            pickle.dump(
                model,
                file
            )

        with open(
            "vectorizer.pkl",
            "wb"
        ) as file:

            pickle.dump(
                vectorizer,
                file
            )

        print(
            "\nSaved using Pickle."
        )

    except Exception as e:

        print("Error:", e)


def load_using_pickle():

    try:

        import pickle

        with open(
            "sentiment_model.pkl",
            "rb"
        ) as file:

            model = pickle.load(
                file
            )

        with open(
            "vectorizer.pkl",
            "rb"
        ) as file:

            vectorizer = pickle.load(
                file
            )

        print(
            "\nModel Loaded Successfully."
        )

        return model, vectorizer

    except Exception as e:

        print("Error:", e)

        return None, None


def save_using_joblib(model, vectorizer):

    try:

        import joblib

        joblib.dump(
            model,
            "sentiment_model.joblib"
        )

        joblib.dump(
            vectorizer,
            "vectorizer.joblib"
        )

        print(
            "\nSaved using Joblib."
        )

    except Exception as e:

        print("Error:", e)


def load_using_joblib():

    try:

        import joblib

        model = joblib.load(
            "sentiment_model.joblib"
        )

        vectorizer = joblib.load(
            "vectorizer.joblib"
        )

        print(
            "\nModel Loaded Successfully."
        )

        return model, vectorizer

    except Exception as e:

        print("Error:", e)

        return None, None


def predict_sentiment(model, vectorizer):

    try:

        if model is None:

            print(
                "Load model first."
            )

            return

        review = input(
            "\nEnter review: "
        )

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

        print(
            f"\nPrediction: "
            f"{prediction}"
        )

    except Exception as e:

        print("Error:", e)


def main_menu():

    df = load_dataset()

    if df is None:
        return

    model = None
    vectorizer = None

    while True:

        print(
            "\n===== MODEL SAVING MENU ====="
        )

        print("1. Train Model")
        print("2. Save Using Pickle")
        print("3. Load Using Pickle")
        print("4. Save Using Joblib")
        print("5. Load Using Joblib")
        print("6. Predict")
        print("7. Exit")

        choice = input(
            "Enter choice: "
        )

        if choice == "1":

            model, vectorizer = (
                train_model(df)
            )

        elif choice == "2":

            save_using_pickle(
                model,
                vectorizer
            )

        elif choice == "3":

            model, vectorizer = (
                load_using_pickle()
            )

        elif choice == "4":

            save_using_joblib(
                model,
                vectorizer
            )

        elif choice == "5":

            model, vectorizer = (
                load_using_joblib()
            )

        elif choice == "6":

            predict_sentiment(
                model,
                vectorizer
            )

        elif choice == "7":

            print("Exiting...")
            break

        else:

            print("Invalid Choice")


if __name__ == "__main__":
    main_menu()