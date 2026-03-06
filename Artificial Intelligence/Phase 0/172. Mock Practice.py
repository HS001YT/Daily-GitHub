# ================= PALINDROME STRING =================

def palindrome_string():
    text = input("Enter a string: ")

    if text == text[::-1]:
        print("It is a palindrome.")
    else:
        print("Not a palindrome.")


# ================= LARGEST NUMBER IN LIST =================

def largest_number_list():
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))

    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    print("Largest number:", largest)


# ================= ARMSTRONG NUMBER =================

def armstrong_number():
    num = int(input("Enter a number: "))

    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    if total == num:
        print("It is an Armstrong number.")
    else:
        print("Not an Armstrong number.")


# ================= PRIME NUMBER =================

def prime_number():
    num = int(input("Enter a number: "))

    if num <= 1:
        print("Not a prime number.")
        return

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not a prime number.")
            return

    print("It is a prime number.")


# ================= SUM OF DIGITS =================

def sum_of_digits():
    num = int(input("Enter a number: "))

    total = 0

    while num > 0:
        digit = num % 10
        total += digit
        num //= 10

    print("Sum of digits:", total)


# ================= MAIN MENU =================

def main_menu():

    while True:

        print("\n====== MOCK PRACTICE MENU ======")
        print("1. Palindrome String")
        print("2. Largest Number in List")
        print("3. Armstrong Number")
        print("4. Prime Number Check")
        print("5. Sum of Digits")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            palindrome_string()

        elif choice == 2:
            largest_number_list()

        elif choice == 3:
            armstrong_number()

        elif choice == 4:
            prime_number()

        elif choice == 5:
            sum_of_digits()

        elif choice == 6:
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")


# ================= PROGRAM START =================

if __name__ == "__main__":
    main_menu()