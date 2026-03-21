def numpy_indexing_slicing():

    import numpy as np

    try:
        
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        print("Enter elements row-wise:")
        data = []

        for i in range(rows):
            row = list(map(int, input(f"Row {i+1}: ").split()))

            if len(row) != cols:
                print("Invalid column count.")
                return

            data.append(row)

        arr = np.array(data)

        print("\nArray:\n", arr)

        
        r = int(input("\nEnter row index: "))
        c = int(input("Enter column index: "))

        print("Element at position:", arr[r, c])

        print("\nRow:", arr[r])
        print("Column:", arr[:, c])

        
        print("\n--- SLICING ---")

        r1 = int(input("Start row: "))
        r2 = int(input("End row: "))
        c1 = int(input("Start col: "))
        c2 = int(input("End col: "))

        sub = arr[r1:r2, c1:c2]

        print("Subarray:\n", sub)

        
        print("\nStep slicing (every 2nd element):")
        print(arr[::2, ::2])

    except IndexError:
        print("Index out of range.")

    except ValueError:
        print("Invalid input.")



def one_d_slicing():

    import numpy as np

    try:
        raw = input("\nEnter 1D array elements: ")
        arr = np.array(list(map(int, raw.split())))

        print("Array:", arr)

        start = int(input("Start index: "))
        end = int(input("End index: "))

        print("Sliced array:", arr[start:end])

        print("Step slicing (every 2nd):", arr[::2])

    except:
        print("Invalid input.")


def main_menu():

    while True:
        print("\n===== NUMPY INDEXING MENU =====")
        print("1. 2D Array Indexing & Slicing")
        print("2. 1D Array Slicing")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            numpy_indexing_slicing()

        elif choice == "2":
            one_d_slicing()

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice")



if __name__ == "__main__":
    main_menu()