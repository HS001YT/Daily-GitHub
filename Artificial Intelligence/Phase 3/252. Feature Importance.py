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


def analyze_feature_importance(df):

    try:
        import pandas as pd
        import matplotlib.pyplot as plt

        from sklearn.model_selection import train_test_split

        from sklearn.pipeline import Pipeline

        from sklearn.preprocessing import StandardScaler

        from sklearn.ensemble import RandomForestClassifier

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

        model = pipeline.named_steps["model"]

        importance_scores = model.feature_importances_

        importance_df = pd.DataFrame({
            "Feature": features,
            "Importance": importance_scores
        })

        importance_df = importance_df.sort_values(
            by="Importance",
            ascending=False
        )

        print("\n===== FEATURE IMPORTANCE =====")

        print(importance_df)

        plt.figure(figsize=(8, 5))

        plt.bar(
            importance_df["Feature"],
            importance_df["Importance"]
        )

        plt.title("Feature Importance")

        plt.xlabel("Features")

        plt.ylabel("Importance Score")

        plt.xticks(rotation=20)

        plt.tight_layout()

        plt.show()

    except Exception as e:
        print("Error:", e)


def main_menu():

    df = load_dataset()

    if df is None:
        return

    while True:

        print("\n===== FEATURE IMPORTANCE MENU =====")
        print("1. View Dataset Info")
        print("2. Analyze Feature Importance")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":

            show_dataset_info(df)

        elif choice == "2":

            analyze_feature_importance(df)

        elif choice == "3":

            print("Exiting...")
            break

        else:

            print("Invalid choice")


if __name__ == "__main__":
    main_menu()