def load_dataset():
    import pandas as pd
    import os

    try:
        file = input("Enter CSV file path (e.g., other_files/kmeans_students.csv): ").strip()

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


def train_kmeans(df):
    try:
        from sklearn.cluster import KMeans

        X = df[["Hours", "Attendance"]]

        model = KMeans(
            n_clusters=2,
            random_state=42
        )

        model.fit(X)

        print("\nK-Means Model Trained Successfully.")

        return model, X

    except Exception as e:
        print("Error:", e)
        return None, None


def plot_clusters(model, X):
    try:
        import matplotlib.pyplot as plt

        if model is None:
            print("Train model first.")
            return

        labels = model.labels_
        centers = model.cluster_centers_

        plt.figure()

        # Cluster points
        plt.scatter(
            X["Hours"],
            X["Attendance"],
            c=labels
        )

        # Centroids
        plt.scatter(
            centers[:, 0],
            centers[:, 1],
            marker="X",
            s=200
        )

        plt.title("K-Means Cluster Visualization")
        plt.xlabel("Hours")
        plt.ylabel("Attendance")

        plt.show()

    except Exception as e:
        print("Error:", e)


def main_menu():
    df = load_dataset()

    if df is None:
        return

    model = None
    X = None

    while True:
        print("\n===== CLUSTER VISUALIZATION MENU =====")
        print("1. Train K-Means Model")
        print("2. Plot Clusters")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            model, X = train_kmeans(df)

        elif choice == "2":
            plot_clusters(model, X)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()