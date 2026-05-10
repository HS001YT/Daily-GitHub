def load_dataset():
    import pandas as pd
    import os

    try:
        file = input("Enter CSV file path (e.g., other_files/decision_tree_students.csv): ").strip()

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
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.metrics import accuracy_score

        X = df[["Hours", "Attendance"]]
        y = df["Pass"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y,
            test_size=0.2,
            random_state=42
        )

        model = DecisionTreeClassifier(random_state=42)

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        accuracy = accuracy_score(y_test, predictions)

        print("\nDecision Tree Model Trained Successfully.")
        print(f"Accuracy: {round(accuracy, 3)}")

        return model, X_test, y_test

    except Exception as e:
        print("Error:", e)
        return None, None, None


def predict_test(model, X_test, y_test):
    try:
        if model is None:
            print("Train model first.")
            return

        predictions = model.predict(X_test)

        print("\n--- Decision Tree Predictions ---")
        print("Actual | Predicted")

        for actual, pred in zip(y_test, predictions):
            print(f"{actual} | {pred}")

    except Exception as e:
        print("Error:", e)


def predict_custom(model):
    try:
        if model is None:
            print("Train model first.")
            return

        hours = float(input("Enter study hours: "))
        attendance = float(input("Enter attendance: "))

        prediction = model.predict([[hours, attendance]])

        print(f"\nPredicted Class (Pass=1 / Fail=0): {prediction[0]}")

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
        print("\n===== DECISION TREE MENU =====")
        print("1. Train Model")
        print("2. Predict Test Data")
        print("3. Predict Custom Input")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            model, X_test, y_test = train_model(df)

        elif choice == "2":
            predict_test(model, X_test, y_test)

        elif choice == "3":
            predict_custom(model)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()