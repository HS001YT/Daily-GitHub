# Day 180 (Part 1)
# Expense Class
# ExpenseManager Class
# Add Expense
# View All Expenses
# Save to CSV
# Load from CSV (on start)
# Input Validation
# Exception Handling
# Menu System (basic)

# Day 180 (Part 2)
# 🔥 What you are adding now:
# Delete Expense
# Category-wise Total (using dictionary)
# Monthly Expense Summary
# Highest Spending Category
# Better formatted output
# Improved menu system
# Auto-save after operations (better UX)

import csv
import os
from datetime import datetime


# ================= EXPENSE CLASS =================

class Expense:

    def __init__(self, amount, category, date, description):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def to_list(self):
        return [self.amount, self.category, self.date, self.description]


# ================= EXPENSE MANAGER =================

class ExpenseManager:

    def __init__(self):

        base_dir = os.path.dirname(os.path.abspath(__file__))
        folder = os.path.join(base_dir, "other_files")
        os.makedirs(folder, exist_ok=True)

        self.file_path = os.path.join(folder, "expenses.csv")
        self.expenses = []

        self.load_expenses()


    # ---------- VALIDATION ----------

    def validate_amount(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be > 0")

    def validate_category(self, category):
        if not category.strip():
            raise ValueError("Category cannot be empty")

    def validate_date(self, date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except:
            raise ValueError("Invalid date format (YYYY-MM-DD)")


    # ---------- ADD EXPENSE ----------

    def add_expense(self):

        try:
            amount = float(input("Enter amount: "))
            self.validate_amount(amount)

            category = input("Enter category: ")
            self.validate_category(category)

            date = input("Enter date (YYYY-MM-DD): ")
            self.validate_date(date)

            description = input("Enter description: ")

            exp = Expense(amount, category, date, description)
            self.expenses.append(exp)

            self.save_expenses()
            print("Expense added & saved.")

        except ValueError as e:
            print("Error:", e)


    # ---------- DELETE EXPENSE ----------

    def delete_expense(self):

        if not self.expenses:
            print("No expenses to delete.")
            return

        self.view_expenses()

        try:
            index = int(input("Enter index to delete: "))

            if 0 <= index < len(self.expenses):
                self.expenses.pop(index)
                self.save_expenses()
                print("Expense deleted.")
            else:
                print("Invalid index.")

        except:
            print("Invalid input.")


    # ---------- VIEW EXPENSES ----------

    def view_expenses(self):

        if not self.expenses:
            print("No expenses found.")
            return

        print("\nIndex | Amount | Category | Date | Description")

        for i, exp in enumerate(self.expenses):
            print(f"{i} | {exp.amount} | {exp.category} | {exp.date} | {exp.description}")


    # ---------- CATEGORY TOTAL ----------

    def category_summary(self):

        summary = {}

        for exp in self.expenses:
            summary[exp.category] = summary.get(exp.category, 0) + exp.amount

        print("\nCategory-wise Total:")
        for cat, amt in summary.items():
            print(cat, ":", amt)


    # ---------- MONTHLY SUMMARY ----------

    def monthly_summary(self):

        summary = {}

        for exp in self.expenses:
            month = exp.date[:7]   # YYYY-MM
            summary[month] = summary.get(month, 0) + exp.amount

        print("\nMonthly Summary:")
        for month, amt in summary.items():
            print(month, ":", amt)


    # ---------- HIGHEST CATEGORY ----------

    def highest_category(self):

        summary = {}

        for exp in self.expenses:
            summary[exp.category] = summary.get(exp.category, 0) + exp.amount

        if not summary:
            print("No data.")
            return

        highest = max(summary, key=summary.get)

        print("Highest Spending Category:", highest)
        print("Amount:", summary[highest])


    # ---------- SAVE ----------

    def save_expenses(self):

        with open(self.file_path, "w", newline="") as file:

            writer = csv.writer(file)
            writer.writerow(["Amount", "Category", "Date", "Description"])

            for exp in self.expenses:
                writer.writerow(exp.to_list())


    # ---------- LOAD ----------

    def load_expenses(self):

        try:
            with open(self.file_path, "r") as file:

                reader = csv.reader(file)
                next(reader)

                for row in reader:
                    amount, category, date, description = row
                    self.expenses.append(
                        Expense(float(amount), category, date, description)
                    )

        except FileNotFoundError:
            pass


# ================= MENU =================

def main_menu():

    manager = ExpenseManager()

    while True:

        print("\n====== SMART EXPENSE ANALYZER ======")
        print("1. Add Expense")
        print("2. Delete Expense")
        print("3. View Expenses")
        print("4. Category-wise Total")
        print("5. Monthly Summary")
        print("6. Highest Spending Category")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            manager.add_expense()

        elif choice == "2":
            manager.delete_expense()

        elif choice == "3":
            manager.view_expenses()

        elif choice == "4":
            manager.category_summary()

        elif choice == "5":
            manager.monthly_summary()

        elif choice == "6":
            manager.highest_category()

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


# ================= START =================

if __name__ == "__main__":
    main_menu()