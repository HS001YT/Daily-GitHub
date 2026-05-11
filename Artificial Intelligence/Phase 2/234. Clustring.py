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

        labels = model.labels_
        centers = model.cluster_centers_

        print("\nK-Means Model Trained Successfully.")

        print("\n--- Cluster Labels ---")
        for i, label in enumerate(labels):
            print(f"Row {i+1}: Cluster {label}")

        print("\n--- Cluster Centers ---")
        for i, center in enumerate(centers):
            print(f"Cluster {i}: {center}")

        return model

    except Exception as e:
        print("Error:", e)
        return None


def predict_custom(model):
    try:
        if model is None:
            print("Train model first.")
            return

        hours = float(input("Enter study hours: "))
        attendance = float(input("Enter attendance: "))

        cluster = model.predict([[hours, attendance]])

        print(f"\nAssigned Cluster: {cluster[0]}")

    except Exception as e:
        print("Error:", e)


def main_menu():
    df = load_dataset()

    if df is None:
        return

    model = None

    while True:
        print("\n===== K-MEANS CLUSTERING MENU =====")
        print("1. Train K-Means Model")
        print("2. Predict Cluster")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            model = train_kmeans(df)

        elif choice == "2":
            predict_custom(model)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()