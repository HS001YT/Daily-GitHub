def load_dataset():
    import pandas as pd
    import os

    try:
        file = input(
            "Enter CSV file path (e.g., other_files/spam_dataset.csv): "
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


def show_dataset_info(df):

    try:
        print("\n===== DATASET INFO =====")

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nShape:")
        print(df.shape)

        print("\nNull Values:")
        print(df.isnull().sum())

    except Exception as e:
        print("Error:", e)


def clean_text(text):

    try:
        import re

        text = text.lower()

        text = re.sub(r"[^a-zA-Z\s]", "", text)

        return text

    except Exception:
        return text


def train_model(df):

    try:
        from sklearn.model_selection import train_test_split

        from sklearn.pipeline import Pipeline

        from sklearn.feature_extraction.text import (
            TfidfVectorizer
        )

        from sklearn.linear_model import LogisticRegression

        from sklearn.metrics import (
            accuracy_score,
            confusion_matrix,
            classification_report
        )

        df["clean_message"] = df["message"].apply(
            clean_text
        )

        X = df["clean_message"]

        y = df["label"]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        pipeline = Pipeline([
            (
                "tfidf",
                TfidfVectorizer()
            ),
            (
                "model",
                LogisticRegression()
            )
        ])

        pipeline.fit(X_train, y_train)

        predictions = pipeline.predict(X_test)

        accuracy = accuracy_score(
            y_test,
            predictions
        )

        cm = confusion_matrix(
            y_test,
            predictions
        )

        report = classification_report(
            y_test,
            predictions
        )

        print("\n===== MODEL TRAINED =====")

        print(f"\nAccuracy: {round(accuracy, 3)}")

        print("\nConfusion Matrix:")
        print(cm)

        print("\nClassification Report:")
        print(report)

        return pipeline

    except Exception as e:
        print("Error:", e)
        return None


def predict_message(model):

    try:
        if model is None:
            print("Train model first.")
            return

        message = input(
            "Enter message: "
        )

        cleaned = clean_text(message)

        prediction = model.predict([cleaned])[0]

        probability = model.predict_proba([cleaned])[0]

        print("\n===== PREDICTION RESULT =====")

        if prediction == "spam":
            print("Prediction: SPAM")
        else:
            print("Prediction: HAM")

        print(
            f"Spam Probability: "
            f"{round(max(probability), 3)}"
        )

    except Exception as e:
        print("Error:", e)


def main_menu():

    df = load_dataset()

    if df is None:
        return

    model = None

    while True:

        print("\n===== SPAM CLASSIFIER MENU =====")
        print("1. View Dataset Info")
        print("2. Train Spam Classifier")
        print("3. Predict Message")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":

            show_dataset_info(df)

        elif choice == "2":

            model = train_model(df)

        elif choice == "3":

            predict_message(model)

        elif choice == "4":

            print("Exiting...")
            break

        else:

            print("Invalid choice")


if __name__ == "__main__":
    main_menu()