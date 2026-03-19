def create_numpy_arrays():

    import numpy as np

    try:
        # -------- 1D ARRAY --------
        raw = input("Enter elements for 1D array (space separated): ")
        arr1 = np.array([int(x) for x in raw.split()])

        print("\n--- 1D ARRAY ---")
        print("Array:", arr1)
        print("Shape:", arr1.shape)
        print("Size:", arr1.size)
        print("Data Type:", arr1.dtype)


        # -------- 2D ARRAY --------
        rows = int(input("\nEnter number of rows: "))
        cols = int(input("Enter number of columns: "))

        print("Enter elements row-wise:")

        data = []
        for i in range(rows):
            row = list(map(int, input(f"Row {i+1}: ").split()))

            if len(row) != cols:
                print("Invalid column count. Try again.")
                return

            data.append(row)

        arr2 = np.array(data)

        print("\n--- 2D ARRAY ---")
        print(arr2)
        print("Shape:", arr2.shape)
        print("Size:", arr2.size)
        print("Data Type:", arr2.dtype)


    except ValueError:
        print("Invalid input! Please enter integers only.")


# -------- MAIN MENU --------

def main_menu():

    while True:
        print("\n===== NUMPY BASICS MENU =====")
        print("1. Create Arrays")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_numpy_arrays()

        elif choice == "2":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


# -------- RUN --------

if __name__ == "__main__":
    main_menu()