def create_1d_array():
    import numpy as np
    try:
        raw = input("Enter elements (space-separated): ")
        arr = np.array(list(map(float, raw.split())))
        return arr
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
        return None


def create_2d_array():
    import numpy as np
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        data = []
        for i in range(rows):
            row = list(map(float, input(f"Row {i+1}: ").split()))
            if len(row) != cols:
                print("Invalid column count.")
                return None
            data.append(row)

        return np.array(data)

    except ValueError:
        print("Invalid input.")
        return None


def validate_shape(arr1, arr2):
    if arr1 is None or arr2 is None:
        return False
    if arr1.shape != arr2.shape:
        print("Error: Arrays must have the same shape.")
        return False
    return True


def perform_operation(arr1, arr2):
    try:
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

        print("\nArray 1:\n", arr1)
        print("Array 2:\n", arr2)
        print("Result:\n", result)

    except Exception as e:
        print("Error during operation:", e)


def one_d_operations():
    print("\n--- 1D Array Operations ---")
    arr1 = create_1d_array()
    arr2 = create_1d_array()

    if validate_shape(arr1, arr2):
        perform_operation(arr1, arr2)


def two_d_operations():
    print("\n--- 2D Array Operations ---")
    arr1 = create_2d_array()
    arr2 = create_2d_array()

    if validate_shape(arr1, arr2):
        perform_operation(arr1, arr2)


def main_menu():
    while True:
        print("\n===== NUMPY OPERATIONS MENU =====")
        print("1. 1D Array Operations")
        print("2. 2D Array Operations")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            one_d_operations()
        elif choice == "2":
            two_d_operations()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()