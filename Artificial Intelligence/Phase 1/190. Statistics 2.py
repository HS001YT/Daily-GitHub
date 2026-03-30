def simulate_coin():
    import numpy as np
    try:
        trials = int(input("Enter number of coin tosses: "))
        if trials <= 0:
            print("Trials must be positive.")
            return

        # 0 = Heads, 1 = Tails
        outcomes = np.random.randint(0, 2, trials)

        heads = np.sum(outcomes == 0)
        tails = np.sum(outcomes == 1)

        print("\n--- Coin Toss Simulation ---")
        print("Total Trials:", trials)
        print("Heads Count:", heads)
        print("Tails Count:", tails)
        print("P(Heads):", heads / trials)
        print("P(Tails):", tails / trials)

    except ValueError:
        print("Invalid input.")


def simulate_dice():
    import numpy as np
    try:
        trials = int(input("Enter number of dice rolls: "))
        if trials <= 0:
            print("Trials must be positive.")
            return

        # Dice values: 1 to 6
        outcomes = np.random.randint(1, 7, trials)

        print("\n--- Dice Roll Simulation ---")
        print("Total Trials:", trials)

        for i in range(1, 7):
            count = np.sum(outcomes == i)
            probability = count / trials
            print(f"Face {i}: Count = {count}, Probability = {probability}")

    except ValueError:
        print("Invalid input.")


def main_menu():
    while True:
        print("\n===== PROBABILITY SIMULATION MENU =====")
        print("1. Coin Toss Simulation")
        print("2. Dice Roll Simulation")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            simulate_coin()

        elif choice == "2":
            simulate_dice()

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()