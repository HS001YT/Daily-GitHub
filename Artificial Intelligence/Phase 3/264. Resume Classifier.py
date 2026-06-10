def load_dataset():
    import pandas as pd
    import os

    try:
        file = input(
            "Enter CSV file path (e.g., other_files/resume_dataset.csv): "
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

    print("\nCategory Distribution:")
    print(df["Category"].value_counts())


def train_resume_classifier(df):

    try:
        from sklearn.model_selection import train_test_split
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.naive_bayes import MultinomialNB
        from sklearn.metrics import accuracy_score

        df = df.copy()

        df["Resume"] = df["Resume"].apply(
            preprocess_text
        )

        X = df["Resume"]

        y = df["Category"]

        vectorizer = TfidfVectorizer()

        X_vectorized = vectorizer.fit_transform(X)

        X_train, X_test, y_train, y_test = train_test_split(
            X_vectorized,
            y,
            test_size=0.2,
            random_state=42
        )

        model = MultinomialNB()

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
            f"\nModel Accuracy: {accuracy:.2f}"
        )

        return model, vectorizer

    except Exception as e:

        print("Error:", e)

        return None, None


def predict_category(model, vectorizer):

    try:

        if model is None:

            print(
                "Train model first."
            )

            return

        resume = input(
            "\nEnter Resume Text:\n"
        )

        resume = preprocess_text(
            resume
        )

        resume_vector = (
            vectorizer.transform(
                [resume]
            )
        )

        prediction = model.predict(
            resume_vector
        )[0]

        print(
            f"\nPredicted Category: {prediction}"
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
            "\n===== RESUME CLASSIFIER MENU ====="
        )

        print("1. View Dataset Info")
        print("2. Train Model")
        print("3. Classify Resume")
        print("4. Exit")

        choice = input(
            "Enter choice: "
        )

        if choice == "1":

            show_dataset_info(df)

        elif choice == "2":

            model, vectorizer = (
                train_resume_classifier(df)
            )

        elif choice == "3":

            predict_category(
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