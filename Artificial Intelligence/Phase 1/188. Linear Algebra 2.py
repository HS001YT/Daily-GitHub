def create_matrix():
    import numpy as np
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


def matrix_multiplication(m1, m2):
    import numpy as np
    try:
        if m1.shape[1] != m2.shape[0]:
            print("Error: Columns of Matrix 1 must equal rows of Matrix 2.")
            return

        result = np.matmul(m1, m2)

        print("\nMatrix 1:\n", m1)
        print("\nMatrix 2:\n", m2)
        print("\nResult (Multiplication):\n", result)

    except Exception as e:
        print("Error in multiplication:", e)


def matrix_transpose(matrix):
    try:
        result = matrix.T
        print("\nOriginal Matrix:\n", matrix)
        print("\nTranspose:\n", result)
    except Exception as e:
        print("Error in transpose:", e)


def main_menu():
    while True:
        print("\n===== MATRIX OPERATIONS MENU =====")
        print("1. Matrix Multiplication")
        print("2. Matrix Transpose")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            print("\n--- Matrix Multiplication ---")
            print("Enter Matrix 1:")
            m1 = create_matrix()

            print("\nEnter Matrix 2:")
            m2 = create_matrix()

            if m1 is not None and m2 is not None:
                matrix_multiplication(m1, m2)

        elif choice == "2":
            print("\n--- Matrix Transpose ---")
            matrix = create_matrix()

            if matrix is not None:
                matrix_transpose(matrix)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()