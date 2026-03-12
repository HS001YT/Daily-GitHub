# ================= BASE CLASS =================

class BankAccount:

    def __init__(self, acc_no, holder_name, balance=0):
        self.acc_no = acc_no
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):

        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.balance += amount
        print("Amount deposited successfully.")

    def withdraw(self, amount):

        if amount > self.balance:
            raise ValueError("Insufficient balance.")

        self.balance -= amount
        print("Withdrawal successful.")

    def show_balance(self):
        print("Current Balance:", self.balance)


# ================= SAVINGS ACCOUNT =================

class SavingsAccount(BankAccount):

    MIN_BALANCE = 500

    def withdraw(self, amount):

        if self.balance - amount < self.MIN_BALANCE:
            raise ValueError("Minimum balance of 500 must be maintained.")

        super().withdraw(amount)


# ================= CURRENT ACCOUNT =================

class CurrentAccount(BankAccount):

    OVERDRAFT_LIMIT = 1000

    def withdraw(self, amount):

        if self.balance - amount < -self.OVERDRAFT_LIMIT:
            raise ValueError("Overdraft limit exceeded.")

        self.balance -= amount
        print("Withdrawal successful.")


# ================= BANK SYSTEM =================

class BankSystem:

    def __init__(self):
        self.accounts = {}

    def create_account(self):

        acc_no = input("Enter Account Number: ")

        if acc_no in self.accounts:
            print("Account already exists.")
            return

        name = input("Enter Holder Name: ")
        acc_type = input("Enter Account Type (savings/current): ").lower()

        if acc_type == "savings":
            account = SavingsAccount(acc_no, name, 1000)

        elif acc_type == "current":
            account = CurrentAccount(acc_no, name, 0)

        else:
            print("Invalid account type.")
            return

        self.accounts[acc_no] = account
        print("Account created successfully.")

    def get_account(self):

        acc_no = input("Enter Account Number: ")

        account = self.accounts.get(acc_no)

        if not account:
            print("Account not found.")
            return None

        return account


# ================= MENU SYSTEM =================

def main_menu():

    bank = BankSystem()

    while True:

        print("\n===== BANK ACCOUNT SYSTEM =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter choice: ")

        try:

            if choice == "1":
                bank.create_account()

            elif choice == "2":

                account = bank.get_account()
                if account:
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)

            elif choice == "3":

                account = bank.get_account()
                if account:
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)

            elif choice == "4":

                account = bank.get_account()
                if account:
                    account.show_balance()

            elif choice == "5":
                print("Exiting system.")
                break

            else:
                print("Invalid choice.")

        except ValueError as e:
            print("Error:", e)


# ================= PROGRAM START =================

if __name__ == "__main__":
    main_menu()