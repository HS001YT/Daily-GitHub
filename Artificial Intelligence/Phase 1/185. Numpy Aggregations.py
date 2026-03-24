import numpy as np

def create_1d_array():
    try:
        raw = input("Enter elements (space-separated): ").strip()
        if not raw:
            print("Input cannot be empty.")
            return None

        arr = np.array(list(map(float, raw.split())))
        return arr

    except ValueError:
        print("Invalid input. Enter numeric values only.")
        return None


def create_2d_array():
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        if rows <= 0 or cols <= 0:
            print("Rows and columns must be positive.")
            return None

        data = []
        for i in range(rows):
            row = input(f"Row {i+1}: ").strip().split()
            if len(row) != cols:
                print("Invalid column count.")
                return None

            try:
                row = list(map(float, row))
            except ValueError:
                print("Invalid input. Enter numeric values only.")
                return None

            data.append(row)


        return np.array(data)

    except ValueError:
        print("Invalid input.")
        return None


def aggregate_1d(arr):
    try:
        print("\nArray:", arr)
        print("Sum:", np.sum(arr))
        print("Mean:", np.mean(arr))
        print("Min:", np.min(arr))
        print("Max:", np.max(arr))
        print("Standard Deviation:", np.std(arr))

    except Exception as e:
        print("Error:", e)


def aggregate_2d(arr):
    try:
        print("\nArray:\n", arr)

        # Entire array
        print("\n--- Overall ---")
        print("Sum:", np.sum(arr))
        print("Mean:", np.mean(arr))
        print("Min:", np.min(arr))
        print("Max:", np.max(arr))
        print("Standard Deviation:", np.std(arr))

        # Axis-wise
        print("\n--- Column-wise (axis=0) ---")
        print("Sum:", np.sum(arr, axis=0))
        print("Mean:", np.mean(arr, axis=0))
        print("Min:", np.min(arr, axis=0))
        print("Max:", np.max(arr, axis=0))
        print("Std:", np.std(arr, axis=0))

        print("\n--- Row-wise (axis=1) ---")
        print("Sum:", np.sum(arr, axis=1))
        print("Mean:", np.mean(arr, axis=1))
        print("Min:", np.min(arr, axis=1))
        print("Max:", np.max(arr, axis=1))
        print("Std:", np.std(arr, axis=1))

    except Exception as e:
        print("Error:", e)


def main_menu():
    while True:
        print("\n===== NUMPY AGGREGATION MENU =====")
        print("1. 1D Array Aggregation")
        print("2. 2D Array Aggregation")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            arr = create_1d_array()
            if arr is not None:
                aggregate_1d(arr)

        elif choice == "2":
            arr = create_2d_array()
            if arr is not None:
                aggregate_2d(arr)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()