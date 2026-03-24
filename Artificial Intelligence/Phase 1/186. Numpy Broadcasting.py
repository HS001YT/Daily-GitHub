import numpy as np

def create_1d_array():
    try:
        raw = input("Enter 1D array elements (space-separated): ").strip()
        if not raw:
            print("Input cannot be empty.")
            return None
        return np.array(list(map(float, raw.split())))
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


def create_scalar():
    try:
        val = float(input("Enter scalar value: "))
        return val
    except ValueError:
        print("Invalid scalar input.")
        return None


def perform_operations(arr1, arr2):
    try:
        print("\nShape of Array 1:", np.shape(arr1))
        print("Shape of Array 2:", np.shape(arr2))

        opr = input("Enter operation (+, -, *): ").strip()

        if opr == "+":
            result = arr1 + arr2
        elif opr == "-":
            result = arr1 - arr2
        elif opr == "*":
            result = arr1 * arr2
        else:
            print("Invalid operation.")
            return

        print("\nResult:\n", result)
        print("Result Shape:", result.shape)

    except ValueError as e:
        print("Broadcasting Error:", e)
    except Exception as e:
        print("Error:", e)


def oneD_twoD_broadcast():
    print("\n--- 1D with 2D Broadcasting ---")
    arr1 = create_1d_array()
    arr2 = create_2d_array()

    if arr1 is not None and arr2 is not None:
        perform_operations(arr1, arr2)


def scalar_array_broadcast():
    print("\n--- Scalar with Array Broadcasting ---")
    scalar = create_scalar()
    print("Choose array type:")
    print("1. 1D Array")
    print("2. 2D Array")

    choice = input("Enter choice: ")

    if choice == "1":
        arr = create_1d_array()
    elif choice == "2":
        arr = create_2d_array()
    else:
        print("Invalid choice.")
        return

    if scalar is not None and arr is not None:
        perform_operations(arr, scalar)


def main_menu():
    while True:
        print("\n===== NUMPY BROADCASTING MENU =====")
        print("1. 1D vs 2D Broadcasting")
        print("2. Scalar vs Array Broadcasting")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            oneD_twoD_broadcast()
        elif choice == "2":
            scalar_array_broadcast()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()