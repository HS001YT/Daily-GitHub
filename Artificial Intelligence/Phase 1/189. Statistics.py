def create_dataset():
    import numpy as np
    try:
        raw = input("Enter dataset values (space-separated): ").strip()
        if not raw:
            print("Input cannot be empty.")
            return None

        data = np.array(list(map(float, raw.split())))
        return data

    except ValueError:
        print("Invalid input. Enter numeric values only.")
        return None


def compute_statistics(data):
    import numpy as np
    try:
        mean_val = np.mean(data)
        median_val = np.median(data)
        variance_val = np.var(data)

        print("\nDataset:", data)
        print("Mean:", mean_val)
        print("Median:", median_val)
        print("Variance:", variance_val)

    except Exception as e:
        print("Error in computation:", e)


def main_menu():
    while True:
        print("\n===== STATISTICS MENU =====")
        print("1. Compute Mean, Median, Variance")
        print("2. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            data = create_dataset()
            if data is not None:
                compute_statistics(data)

        elif choice == "2":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()