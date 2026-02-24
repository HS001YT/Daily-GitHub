# 🔹 Task 1 – Factorial (Recursive)
# 🎯 Requirement:
# Create a function factorial(n)
# Base case: when n reaches stopping condition
# Recursive case: function calls itself
# Conditions:
# If user enters negative number → print message
# Take input from user
# Display result

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)





# 🔹 Task 2 – Fibonacci (Recursive)
# 🎯 Requirement:
# Create a function fibonacci(n)
# It should return the nth Fibonacci number
# Conditions:
# Handle invalid input (negative)
# Take input from user
# Print result

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)






# 🔹 Task 3 – Power Function (Recursive)
# 🎯 Requirement:
# Create function power(base, exponent)
# Compute base^exponent recursively
# Conditions:
# Exponent = 0 → return 1
# Handle negative exponent if you can (optional challenge)

def power(base, exponent):
    if exponent == 0:
        return 1
    if exponent < 0:
        return 1 / power(base, -exponent)
    return base * power(base, exponent - 1)





def main_menu():
    while True:
        print("\n====== RECURSION MENU ======")
        print("1. Factorial")
        print("2. Fibonacci")
        print("3. Power")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        # -------- FACTORIAL --------
        if choice == 1:
            try:
                num = int(input("Enter a non-negative integer: "))
                if num < 0:
                    print("Factorial is not defined for negative numbers.")
                else:
                    print("Factorial =", factorial(num))
            except ValueError:
                print("Invalid input! Please enter an integer.")

        # -------- FIBONACCI --------
        elif choice == 2:
            try:
                num = int(input("Enter a non-negative integer: "))
                if num < 0:
                    print("Fibonacci is not defined for negative numbers.")
                else:
                    print("Fibonacci =", fibonacci(num))
            except ValueError:
                print("Invalid input! Please enter an integer.")

        # -------- POWER --------
        elif choice == 3:
            try:
                base = float(input("Enter base: "))
                exponent = int(input("Enter exponent: "))
                print("Result =", power(base, exponent))
            except ValueError:
                print("Invalid input! Please enter valid numbers.")
            except ZeroDivisionError:
                print("Math error: Cannot divide by zero.")

        # -------- EXIT --------
        elif choice == 4:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")
