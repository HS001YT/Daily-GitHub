def load_dataset():
    import pandas as pd
    import os

    try:
        file = input(
            "Enter CSV file path (e.g., other_files/fraud_dataset.csv): "
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


def train_model(df):

    try:
        from sklearn.model_selection import train_test_split

        from sklearn.pipeline import Pipeline

        from sklearn.preprocessing import StandardScaler

        from sklearn.ensemble import RandomForestClassifier

        from sklearn.metrics import (
            accuracy_score,
            precision_score,
            recall_score,
            f1_score,
            confusion_matrix
        )

        features = [
            "TransactionAmount",
            "TransactionTime",
            "LocationChange",
            "MultipleAttempts",
            "International"
        ]

        target = "Fraud"

        X = df[features]

        y = df[target]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        pipeline = Pipeline([
            (
                "scaler",
                StandardScaler()
            ),
            (
                "model",
                RandomForestClassifier(
                    n_estimators=100,
                    random_state=42
                )
            )
        ])

        pipeline.fit(X_train, y_train)

        predictions = pipeline.predict(X_test)

        accuracy = accuracy_score(
            y_test,
            predictions
        )

        precision = precision_score(
            y_test,
            predictions
        )

        recall = recall_score(
            y_test,
            predictions
        )

        f1 = f1_score(
            y_test,
            predictions
        )

        cm = confusion_matrix(
            y_test,
            predictions
        )

        print("\n===== MODEL TRAINED =====")

        print(f"\nAccuracy : {round(accuracy, 3)}")
        print(f"Precision: {round(precision, 3)}")
        print(f"Recall   : {round(recall, 3)}")
        print(f"F1 Score : {round(f1, 3)}")

        print("\nConfusion Matrix:")
        print(cm)

        return pipeline

    except Exception as e:
        print("Error:", e)
        return None


def predict_transaction(model):

    try:
        import pandas as pd

        if model is None:
            print("Train model first.")
            return

        amount = float(
            input("Enter transaction amount: ")
        )

        time = int(
            input("Enter transaction time (0-23): ")
        )

        location_change = int(
            input("Location changed? (0/1): ")
        )

        multiple_attempts = int(
            input("Multiple attempts? (0/1): ")
        )

        international = int(
            input("International transaction? (0/1): ")
        )

        custom_df = pd.DataFrame([
            {
                "TransactionAmount": amount,
                "TransactionTime": time,
                "LocationChange": location_change,
                "MultipleAttempts": multiple_attempts,
                "International": international
            }
        ])

        prediction = pipeline.predict(custom_df)[0]

        probability = pipeline.predict_proba(custom_df)[0]

        print("\n===== FRAUD PREDICTION =====")

        if prediction == 1:
            print("Prediction: FRAUD")
        else:
            print("Prediction: NORMAL")

        print(
            f"Fraud Probability: "
            f"{round(probability[1], 3)}"
        )

    except Exception as e:
        print("Error:", e)


def main_menu():

    df = load_dataset()

    if df is None:
        return

    pipeline = None

    while True:

        print("\n===== FRAUD DETECTION MENU =====")
        print("1. View Dataset Info")
        print("2. Train Fraud Detection Model")
        print("3. Predict Transaction")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":

            show_dataset_info(df)

        elif choice == "2":

            pipeline = train_model(df)

        elif choice == "3":

            predict_transaction(pipeline)

        elif choice == "4":

            print("Exiting...")
            break

        else:

            print("Invalid choice")


if __name__ == "__main__":
    main_menu()