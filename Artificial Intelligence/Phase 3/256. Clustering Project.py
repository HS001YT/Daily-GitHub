def load_dataset():
    import pandas as pd
    import os

    try:
        file = input(
            "Enter CSV file path (e.g., other_files/customers.csv): "
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


def elbow_method(df):

    try:
        import matplotlib.pyplot as plt

        from sklearn.cluster import KMeans
        from sklearn.preprocessing import StandardScaler

        X = df[
            ["AnnualIncome", "SpendingScore"]
        ]

        scaler = StandardScaler()

        X_scaled = scaler.fit_transform(X)

        inertia_values = []

        k_range = range(1, 11)

        for k in k_range:

            model = KMeans(
                n_clusters=k,
                random_state=42,
                n_init=10
            )

            model.fit(X_scaled)

            inertia_values.append(
                model.inertia_
            )

        plt.figure(figsize=(8, 5))

        plt.plot(
            k_range,
            inertia_values,
            marker="o"
        )

        plt.title("Elbow Method")

        plt.xlabel("Number of Clusters (K)")

        plt.ylabel("Inertia")

        plt.grid(True)

        plt.show()

    except Exception as e:
        print("Error:", e)


def perform_clustering(df):

    try:
        import matplotlib.pyplot as plt

        from sklearn.cluster import KMeans
        from sklearn.preprocessing import StandardScaler

        X = df[
            ["AnnualIncome", "SpendingScore"]
        ]

        scaler = StandardScaler()

        X_scaled = scaler.fit_transform(X)

        k = int(
            input(
                "Enter number of clusters (e.g., 3): "
            )
        )

        model = KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10
        )

        clusters = model.fit_predict(
            X_scaled
        )

        df["Cluster"] = clusters

        print("\n===== CLUSTER ASSIGNMENTS =====")

        print(
            df[
                [
                    "CustomerID",
                    "AnnualIncome",
                    "SpendingScore",
                    "Cluster"
                ]
            ]
        )

        plt.figure(figsize=(8, 5))

        plt.scatter(
            df["AnnualIncome"],
            df["SpendingScore"],
            c=df["Cluster"]
        )

        plt.title(
            "Customer Segmentation"
        )

        plt.xlabel(
            "Annual Income"
        )

        plt.ylabel(
            "Spending Score"
        )

        plt.show()

    except Exception as e:
        print("Error:", e)


def main_menu():

    df = load_dataset()

    if df is None:
        return

    while True:

        print("\n===== CUSTOMER SEGMENTATION MENU =====")

        print("1. View Dataset Info")
        print("2. Show Elbow Method")
        print("3. Perform K-Means Clustering")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            show_dataset_info(df)

        elif choice == "2":

            elbow_method(df)

        elif choice == "3":

            perform_clustering(df)

        elif choice == "4":

            print("Exiting...")
            break

        else:

            print("Invalid Choice")


if __name__ == "__main__":
    main_menu()