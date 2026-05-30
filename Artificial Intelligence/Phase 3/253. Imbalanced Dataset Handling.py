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

        print(df.head())

        print("\nShape:")
        print(df.shape)

        print("\nClass Distribution:")
        print(df["Fraud"].value_counts())

    except Exception as e:
        print("Error:", e)


def compare_models(df):

    try:
        import matplotlib.pyplot as plt

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

        from imblearn.over_sampling import SMOTE

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

        scaler = StandardScaler()

        X_train_scaled = scaler.fit_transform(X_train)

        X_test_scaled = scaler.transform(X_test)

        models = {}

        # ---------------- Normal Random Forest ----------------

        normal_model = RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )

        normal_model.fit(
            X_train_scaled,
            y_train
        )

        models["Normal RF"] = normal_model

        # ---------------- Balanced Random Forest ----------------

        balanced_model = RandomForestClassifier(
            n_estimators=100,
            class_weight="balanced",
            random_state=42
        )

        balanced_model.fit(
            X_train_scaled,
            y_train
        )

        models["Balanced RF"] = balanced_model

        # ---------------- SMOTE ----------------

        smote = SMOTE(
            random_state=42
        )

        X_smote, y_smote = smote.fit_resample(
            X_train_scaled,
            y_train
        )

        smote_model = RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )

        smote_model.fit(
            X_smote,
            y_smote
        )

        models["SMOTE + RF"] = smote_model

        f1_scores = {}

        print("\n===== MODEL COMPARISON =====")

        for name, model in models.items():

            predictions = model.predict(
                X_test_scaled
            )

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

            f1_scores[name] = f1

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
            f1_scores,
            key=f1_scores.get
        )

        print("\n===== BEST MODEL =====")

        print(best_model)

        print(
            f"Best F1 Score: "
            f"{round(f1_scores[best_model], 3)}"
        )

        plt.figure(figsize=(8, 5))

        plt.bar(
            list(f1_scores.keys()),
            list(f1_scores.values())
        )

        plt.title("Model Comparison (F1 Score)")

        plt.xlabel("Models")

        plt.ylabel("F1 Score")

        plt.tight_layout()

        plt.show()

    except Exception as e:
        print("Error:", e)


def main_menu():

    df = load_dataset()

    if df is None:
        return

    while True:

        print("\n===== IMBALANCED DATASET MENU =====")
        print("1. View Dataset Info")
        print("2. Compare Balancing Techniques")
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