def get_histogram_input():
    try:
        data = list(map(float, input("Enter data values (space-separated): ").split()))
        
        if len(data) == 0:
            print("Error: Input cannot be empty.")
            return None
        
        return data

    except ValueError:
        print("Invalid input. Enter numeric values only.")
        return None


def get_scatter_input():
    try:
        x = list(map(float, input("Enter X values (space-separated): ").split()))
        y = list(map(float, input("Enter Y values (space-separated): ").split()))

        if len(x) != len(y):
            print("Error: X and Y must have same length.")
            return None, None

        if len(x) == 0:
            print("Error: Input cannot be empty.")
            return None, None

        return x, y

    except ValueError:
        print("Invalid input. Enter numeric values only.")
        return None, None


def plot_histogram(data):
    try:
        import matplotlib.pyplot as plt

        plt.figure()
        plt.hist(data, bins=10)
        plt.title("Histogram (Data Distribution)")
        plt.xlabel("Value")
        plt.ylabel("Frequency")

        plt.show()

    except Exception as e:
        print("Error:", e)


def plot_scatter(x, y):
    try:
        import matplotlib.pyplot as plt

        plt.figure()
        plt.scatter(x, y)
        plt.title("Scatter Plot")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.grid()

        plt.show()

    except Exception as e:
        print("Error:", e)


def main_menu():
    while True:
        print("\n===== VISUALIZATION MENU =====")
        print("1. Histogram")
        print("2. Scatter Plot")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            data = get_histogram_input()
            if data is not None:
                plot_histogram(data)

        elif choice == "2":
            x, y = get_scatter_input()
            if x is not None:
                plot_scatter(x, y)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()