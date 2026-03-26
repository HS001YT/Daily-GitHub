def create_vector():
    import numpy as np
    try:
        raw = input("Enter vector elements (space-separated): ").strip()
        if not raw:
            print("Input cannot be empty.")
            return None

        vector = np.array(list(map(float, raw.split())))
        return vector

    except ValueError:
        print("Invalid input. Enter numeric values only.")
        return None


def validate_same_length(v1, v2):
    if v1 is None or v2 is None:
        return False
    if v1.shape != v2.shape:
        print("Error: Vectors must have the same length.")
        return False
    return True


def dot_product(v1, v2):
    import numpy as np
    try:
        result = np.dot(v1, v2)
        print("\nDot Product:", result)
    except Exception as e:
        print("Error in dot product:", e)


def vector_magnitude(v):
    import numpy as np
    try:
        magnitude = np.sqrt(np.sum(v ** 2))
        print("Magnitude:", magnitude)
    except Exception as e:
        print("Error in magnitude:", e)


def main_menu():
    while True:
        print("\n===== VECTOR OPERATIONS MENU =====")
        print("1. Dot Product")
        print("2. Magnitude of Vector")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            print("\n--- Dot Product ---")
            v1 = create_vector()
            v2 = create_vector()

            if validate_same_length(v1, v2):
                print("Vector 1:", v1)
                print("Vector 2:", v2)
                dot_product(v1, v2)

        elif choice == "2":
            print("\n--- Vector Magnitude ---")
            v = create_vector()

            if v is not None:
                print("Vector:", v)
                vector_magnitude(v)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()