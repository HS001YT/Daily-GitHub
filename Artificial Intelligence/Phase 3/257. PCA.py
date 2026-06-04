def load_dataset():
    import pandas as pd
    import os

    try:
        file = input(
            "Enter CSV file path (e.g., other_files/customers_pca.csv): "
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

    print("\n===== DATASET INFO =====")

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nShape:")
    print(df.shape)

    print("\nNull Values:")
    print(df.isnull().sum())


def perform_pca(df):

    try:
        import pandas as pd
        import matplotlib.pyplot as plt

        from sklearn.preprocessing import StandardScaler
        from sklearn.decomposition import PCA

        features = [
            "Age",
            "AnnualIncome",
            "SpendingScore",
            "Savings"
        ]

        X = df[features]

        scaler = StandardScaler()

        X_scaled = scaler.fit_transform(X)

        pca = PCA(n_components=2)

        pca_result = pca.fit_transform(
            X_scaled
        )

        pca_df = pd.DataFrame(
            pca_result,
            columns=["PC1", "PC2"]
        )

        print("\n===== PCA RESULT =====")

        print(pca_df.head())

        explained_variance = (
            pca.explained_variance_ratio_
        )

        print(
            "\nExplained Variance Ratio:"
        )

        print(explained_variance)

        print(
            f"\nTotal Variance Retained: "
            f"{explained_variance.sum()*100:.2f}%"
        )

        plt.figure(figsize=(8, 5))

        plt.scatter(
            pca_df["PC1"],
            pca_df["PC2"]
        )

        plt.title(
            "PCA Visualization"
        )

        plt.xlabel(
            "Principal Component 1"
        )

        plt.ylabel(
            "Principal Component 2"
        )

        plt.grid(True)

        plt.show()

    except Exception as e:
        print("Error:", e)


def main_menu():

    df = load_dataset()

    if df is None:
        return

    while True:

        print("\n===== PCA MENU =====")

        print("1. View Dataset Info")
        print("2. Perform PCA")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            show_dataset_info(df)

        elif choice == "2":

            perform_pca(df)

        elif choice == "3":

            print("Exiting...")
            break

        else:

            print("Invalid Choice")


if __name__ == "__main__":
    main_menu()