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


def predict_test(model, X_test, y_test):
    try:
        if model is None:
            print("Train model first.")
            return

        predictions = model.predict(X_test)
        probabilities = model.predict_proba(X_test)

        print("\n--- Prediction with Probabilities ---")
        print("Actual | Predicted | Prob(Fail) | Prob(Pass)")

        for actual, pred, prob in zip(y_test, predictions, probabilities):
            print(f"{actual} | {pred} | {round(prob[0],2)} | {round(prob[1],2)}")

    except Exception as e:
        print("Error:", e)


def predict_custom(model):
    try:
        if model is None:
            print("Train model first.")
            return

        hours = float(input("Enter study hours: "))

        prediction = model.predict([[hours]])[0]
        probability = model.predict_proba([[hours]])[0]

        print("\n--- Custom Prediction ---")
        print(f"Predicted Class: {prediction}")
        print(f"Probability (Fail): {round(probability[0],2)}")
        print(f"Probability (Pass): {round(probability[1],2)}")

        if probability[1] >= 0.5:
            print("Decision: PASS")
        else:
            print("Decision: FAIL")

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
        print("\n===== LOGISTIC REGRESSION PREDICTION MENU =====")
        print("1. Train Model")
        print("2. Predict on Test Data")
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