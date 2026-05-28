def load_dataset():
    import pandas as pd
    import os

    try:
        file = input("Enter CSV file path (e.g., other_files/fraud_dataset.csv): ").strip()

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

        print(df.head())

        print("\nShape:")
        print(df.shape)

        print("\nNull Values:")
        print(df.isnull().sum())

    except Exception as e:
        print("Error:", e)


def compare_models(df):
    try:
        from sklearn.model_selection import train_test_split
        from sklearn.pipeline import Pipeline
        from sklearn.preprocessing import StandardScaler
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import (
            accuracy_score,
            precision_score,
            recall_score,
            f1_score
        )

        from xgboost import XGBClassifier
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

        models = {
            "Random Forest":
            Pipeline([
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
            ]),

            "XGBoost":
            Pipeline([
                (
                    "scaler",
                    StandardScaler()
                ),
                (
                    "model",
                    XGBClassifier(
                        use_label_encoder=False,
                        eval_metric="logloss",
                        random_state=42
                    )
                )
            ])
        }

        results = {}

        print("\n===== MODEL COMPARISON =====")
        for name, pipeline in models.items():
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

            results[name] = f1
            print(f"\n===== {name} =====")
            print(
                f"Accuracy : {round(accuracy, 3)}"
            )

            print(
                f"Precision: {round(precision, 3)}"
            )

            print(
                f"Recall   : {round(recall, 3)}"
            )

            print(
                f"F1 Score : {round(f1, 3)}"
            )

        best_model = max(
            results,
            key=results.get
        )

        print("\n===== BEST MODEL =====")
        print(f"{best_model}")
        print(
            f"Best F1 Score: "
            f"{round(results[best_model], 3)}"
        )

    except Exception as e:
        print("Error:", e)


def main_menu():
    df = load_dataset()
    if df is None:
        return

    while True:
        print("\n===== ENSEMBLE LEARNING MENU =====")
        print("1. View Dataset Info")
        print("2. Compare Models")
        print("3. Exit")

        choice = input("Enter choice: ").strip()
        if choice == "1":
            show_dataset_info(df)

        elif choice == "2":
            compare_models(df)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()