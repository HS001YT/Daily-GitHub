def load_dataset():
    import pandas as pd
    import os

    try:
        file = input("Enter CSV file path (e.g., other_files/students_logistic.csv): ").strip()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(base_dir, file)

        df = pd.read_csv(full_path)
        print("\nDataset Loaded Successfully.\n")
        return df

    except FileNotFoundError:
        print("File not found. Check the path.")
        return None
    except Exception as e:
        print("Error:", e)
        return None


def train_model(df):
    try:
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LogisticRegression

        X = df[["Hours"]]
        y = df["Pass"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        model = LogisticRegression()
        model.fit(X_train, y_train)

        print("\nModel Trained Successfully.")
        return model, X_test, y_test

    except Exception as e:
        print("Error:", e)
        return None, None, None


def evaluate_model(model, X_test, y_test):
    try:
        from sklearn.metrics import confusion_matrix, accuracy_score

        if model is None:
            print("Train model first.")
            return

        predictions = model.predict(X_test)

        print("\n--- Actual vs Predicted ---")
        print("Actual | Predicted")
        for actual, pred in zip(y_test, predictions):
            print(f"{actual} | {pred}")

        # Confusion Matrix
        cm = confusion_matrix(y_test, predictions)
        acc = accuracy_score(y_test, predictions)

        print("\n--- Confusion Matrix ---")
        print("        Pred 0   Pred 1")
        print(f"Actual 0   {cm[0][0]}       {cm[0][1]}")
        print(f"Actual 1   {cm[1][0]}       {cm[1][1]}")

        print(f"\nAccuracy: {round(acc, 3)}")

    except Exception as e:
        print("Error:", e)


def main_menu():
    df = load_dataset()
    if df is None:
        return

    model = None
    X_test = None
    y_test = None

    while True:
        print("\n===== LOGISTIC REGRESSION EVALUATION MENU =====")
        print("1. Train Model")
        print("2. Evaluate Model")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            model, X_test, y_test = train_model(df)
        elif choice == "2":
            evaluate_model(model, X_test, y_test)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()