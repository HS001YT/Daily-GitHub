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

    text = re.sub(r'\d+', '', text)

    text = re.sub(r'[^\w\s]', '', text)

    return text


def show_dataset_info(df):

    print("\n===== DATASET INFO =====")

    print(df.head())

    print("\nShape:")
    print(df.shape)

    print("\nNull Values:")
    print(df.isnull().sum())


def train_sentiment_model(df):

    try:
        from sklearn.model_selection import train_test_split
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.linear_model import LogisticRegression
        from sklearn.metrics import accuracy_score

        df = df.copy()

        df["Review"] = (
            df["Review"]
            .apply(preprocess_text)
        )

        X = df["Review"]

        y = df["Sentiment"]

        vectorizer = TfidfVectorizer()

        X_vectorized = vectorizer.fit_transform(X)

        X_train, X_test, y_train, y_test = train_test_split(
            X_vectorized,
            y,
            test_size=0.2,
            random_state=42
        )

        model = LogisticRegression()

        model.fit(
            X_train,
            y_train
        )

        predictions = model.predict(
            X_test
        )

        accuracy = accuracy_score(
            y_test,
            predictions
        )

        print(
            f"\nModel Accuracy: "
            f"{accuracy:.2f}"
        )

        return model, vectorizer

    except Exception as e:

        print("Error:", e)

        return None, None


def predict_sentiment(model, vectorizer):

    try:

        if model is None:

            print(
                "Train model first."
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
            f"\nPredicted Sentiment: "
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
            "\n===== SENTIMENT ANALYSIS MENU ====="
        )

        print("1. View Dataset Info")
        print("2. Train Model")
        print("3. Predict Sentiment")
        print("4. Exit")

        choice = input(
            "Enter choice: "
        )

        if choice == "1":

            show_dataset_info(df)

        elif choice == "2":

            model, vectorizer = (
                train_sentiment_model(df)
            )

        elif choice == "3":

            predict_sentiment(
                model,
                vectorizer
            )

        elif choice == "4":

            print("Exiting...")
            break

        else:

            print("Invalid Choice")


if __name__ == "__main__":
    main_menu()