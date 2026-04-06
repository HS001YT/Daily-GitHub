def get_input():
    try:
        x = input("Enter X values (space-separated): ").split()
        y = list(map(float, input("Enter Y values (space-separated): ").split()))

        if len(x) != len(y):
            print("Error: X and Y must have same length.")
            return None, None

        if len(x) == 0:
            print("Error: Input cannot be empty.")
            return None, None

        return x, y

    except ValueError:
        print("Invalid input. Y must be numeric.")
        return None, None


def plot_line_chart(x, y):
    try:
        import matplotlib.pyplot as plt

        plt.figure()
        plt.plot(x, y, marker='o')
        plt.title("Line Chart")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.grid()

        plt.show()

    except Exception as e:
        print("Error:", e)


def plot_bar_chart(x, y):
    try:
        import matplotlib.pyplot as plt

        plt.figure()
        plt.bar(x, y)
        plt.title("Bar Chart")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")

        plt.show()

    except Exception as e:
        print("Error:", e)


def main_menu():
    while True:
        print("\n===== VISUALIZATION MENU =====")
        print("1. Line Chart")
        print("2. Bar Chart")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            x, y = get_input()
            if x is not None:
                plot_line_chart(x, y)

        elif choice == "2":
            x, y = get_input()
            if x is not None:
                plot_bar_chart(x, y)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()