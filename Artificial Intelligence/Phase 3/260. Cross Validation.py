def load_dataset():
    import pandas as pd
    import os

    try:
        file = input("Enter CSV file path (e.g., other_files/train.csv): ").strip()

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


def show_dataset_info(df):

    print("\n===== DATASET INFO =====")

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nShape:")
    print(df.shape)

    print("\nNull Values:")
    print(df.isnull().sum())


def preprocess_data(df):

    from sklearn.preprocessing import LabelEncoder

    df = df.copy()

    df["Age"] = df["Age"].fillna(df["Age"].median())

    df["Fare"] = df["Fare"].fillna(df["Fare"].median())

    encoder = LabelEncoder()

    df["Sex"] = encoder.fit_transform(df["Sex"])

    X = df[
        [
            "Pclass",
            "Sex",
            "Age",
            "Fare"
        ]
    ]

    y = df["Survived"]

    return X, y


def perform_kfold_validation(df):

    try:
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.model_selection import KFold
        from sklearn.model_selection import cross_val_score

        X, y = preprocess_data(df)

        model = DecisionTreeClassifier(
            random_state=42
        )

        kfold = KFold(
            n_splits=5,
            shuffle=True,
            random_state=42
        )

        scores = cross_val_score(
            model,
            X,
            y,
            cv=kfold,
            scoring="accuracy"
        )

        print("\n===== K-FOLD RESULTS =====")

        for i, score in enumerate(scores, start=1):

            print(
                f"Fold {i}: {score:.4f}"
            )

        print(
            f"\nMean Accuracy: "
            f"{scores.mean():.4f}"
        )

        print(
            f"Standard Deviation: "
            f"{scores.std():.4f}"
        )

    except Exception as e:

        print("Error:", e)


def perform_stratified_kfold(df):

    try:
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.model_selection import StratifiedKFold
        from sklearn.model_selection import cross_val_score

        X, y = preprocess_data(df)

        model = DecisionTreeClassifier(
            random_state=42
        )

        stratified_kfold = StratifiedKFold(
            n_splits=5,
            shuffle=True,
            random_state=42
        )

        scores = cross_val_score(
            model,
            X,
            y,
            cv=stratified_kfold,
            scoring="accuracy"
        )

        print(
            "\n===== STRATIFIED K-FOLD RESULTS ====="
        )

        for i, score in enumerate(scores, start=1):

            print(
                f"Fold {i}: {score:.4f}"
            )

        print(
            f"\nMean Accuracy: "
            f"{scores.mean():.4f}"
        )

        print(
            f"Standard Deviation: "
            f"{scores.std():.4f}"
        )

    except Exception as e:

        print("Error:", e)


def compare_methods(df):

    try:
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.model_selection import (
            KFold,
            StratifiedKFold,
            cross_val_score
        )

        X, y = preprocess_data(df)

        model = DecisionTreeClassifier(
            random_state=42
        )

        kfold = KFold(
            n_splits=5,
            shuffle=True,
            random_state=42
        )

        stratified = StratifiedKFold(
            n_splits=5,
            shuffle=True,
            random_state=42
        )

        k_scores = cross_val_score(
            model,
            X,
            y,
            cv=kfold,
            scoring="accuracy"
        )

        s_scores = cross_val_score(
            model,
            X,
            y,
            cv=stratified,
            scoring="accuracy"
        )

        print("\n===== COMPARISON =====")

        print(
            f"K-Fold Mean Accuracy: "
            f"{k_scores.mean():.4f}"
        )

        print(
            f"Stratified K-Fold Mean Accuracy: "
            f"{s_scores.mean():.4f}"
        )

    except Exception as e:

        print("Error:", e)


def main_menu():

    df = load_dataset()

    if df is None:
        return

    while True:

        print("\n===== CROSS VALIDATION MENU =====")

        print("1. View Dataset Info")
        print("2. K-Fold Validation")
        print("3. Stratified K-Fold Validation")
        print("4. Compare Both Methods")
        print("5. Exit")

        choice = input(
            "Enter choice: "
        ).strip()

        if choice == "1":

            show_dataset_info(df)

        elif choice == "2":

            perform_kfold_validation(df)

        elif choice == "3":

            perform_stratified_kfold(df)

        elif choice == "4":

            compare_methods(df)

        elif choice == "5":

            print("Exiting...")
            break

        else:

            print("Invalid Choice")


if __name__ == "__main__":
    main_menu()