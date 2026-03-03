# Changes Done in the code of Day 166







# ✅ 1️⃣ Imports Changed
# 🔴 Original:
# from sorting import *

# 🟢 Refactored:
# import sorting


# ✅ 2️⃣ Removed Large if-elif Chains
# 🔴 Original:
# if choice == 1:
#     result = bubble_sort(data)
# elif choice == 2:
#     result = selection_sort(data)
# ...
# 🟢 Refactored:
# SORTING_METHODS = {
#     1: sorting.bubble_sort,
#     2: sorting.selection_sort,
# }
# sort_function = SORTING_METHODS.get(choice)


# ✅ 3️⃣ Used Dictionary Mapping for Main Menu
# 🔴 Original:
# Long if-elif for every menu item.

# 🟢 Refactored:
# MENU = {
#     1: manager.create_dataset,
#     2: manager.save_to_file,
# }


# ✅ 4️⃣ List Comprehension Used
# 🔴 Original:
# for item in data:
#     stack.push(item)
# 🟢 Refactored:
# [stack.push(item) for item in data]


# ✅ 5️⃣ Set Comprehension for Duplicate Removal
# 🔴 Original:
# self.datasets[name] = list(set(data))
# 🟢 Refactored:
# data = list({int(x) for x in raw_input})


# ✅ 6️⃣ Used all() for Validation
# 🔴 Original:
# Manual checking or no checking.
# 🟢 Refactored:
# if not all(item.lstrip("-").isdigit() for item in raw_input):


# ✅ 7️⃣ Cleaner Recursion Base Case
# 🔴 Original:
# if len(data) == 0:
# 🟢 Refactored:
# return 0 if not data else ...


# ✅ 8️⃣ Removed eval() (Security Fix)
# 🔴 Original:
# self.datasets = eval(content)
# 🟢 Refactored:
# json.load(file)


# ✅ 9️⃣ Function Names Auto Printed
# 🔴 Original:
# Hardcoded menu strings.
# 🟢 Refactored:
# print(f"{key}. {func.__name__}")


# ✅ 🔟 Cleaner Conditional Output
# 🔴 Original:
# if index != -1:
#     print("Found")
# else:
#     print("Not found")
# 🟢 Refactored:
# print("Element found at index:" if index != -1 else "Element not found.", index)


# 🧠 Overall Structural Changes

# Area	                        Original	                Refactored

# Menu Handling	                if-elif chain	            Dictionary mapping
# Sorting Selection	            if-elif	Function            lookup
# Searching	                    if-elif	Function            lookup
# Validation	                Manual	                    all() + generator
# Duplicate Removal	            set()	                    Set comprehension
# File Handling	                eval()	                    JSON
# Recursion	                    Basic	                    Cleaner expression
# Imports	                    * wildcard	                Proper namespace











# IMPORTS


import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "other_files"))

import json
import time

import sorting
import searching
from stack_queue import Stack, Queue
from linked_list import LinkedList


# DATA

class DataManager:

    def __init__(self):
        self.datasets = {}

    def create_dataset(self):
        name = input("Enter dataset name: ").strip()

        raw_input = input("Enter numbers separated by space: ").split()

        # Validate numeric input pythonically
        if not all(item.lstrip("-").isdigit() for item in raw_input):
            print("Invalid input. Only integers allowed.")
            return

        data = list({int(x) for x in raw_input})  # remove duplicates using set comprehension

        self.datasets[name] = data
        print("Dataset created.")

    def save_to_file(self, filename="data.json"):
        with open(filename, "w") as file:
            json.dump(self.datasets, file)
        print("Data saved.")

    def load_from_file(self, filename="data.json"):
        try:
            with open(filename, "r") as file:
                self.datasets = json.load(file)
            print("Data loaded.")
        except FileNotFoundError:
            print("File not found.")

    def get_dataset(self, name):
        return self.datasets.get(name)

    def list_datasets(self):
        print("Available datasets:", list(self.datasets.keys()))


# SORTING

SORTING_METHODS = {
    1: sorting.bubble_sort,
    2: sorting.selection_sort,
    3: sorting.insertion_sort,
    4: sorting.merge_sort,
    5: sorting.quick_sort,
    6: sorting.heap_sort,
    7: sorting.counting_sort,
    8: sorting.radix_sort,
    9: sorting.bucket_sort,
}


def sorting_module(data):
    if not data:
        print("Dataset not found.")
        return

    print("\n====== SORTING MENU ======")
    for key, func in SORTING_METHODS.items():
        print(f"{key}. {func.__name__}")

    choice = int(input("Enter choice: "))
    sort_function = SORTING_METHODS.get(choice)

    if not sort_function:
        print("Invalid choice.")
        return

    start = time.time()
    result = sort_function(data.copy())
    end = time.time()

    print("Sorted Data:", result)
    print("Time Taken:", round(end - start, 6), "seconds")


# SEARCH

SEARCH_METHODS = {
    1: searching.linear_search,
    2: searching.binary_search,
    3: searching.interpolation_search,
}


def searching_module(data):
    if not data:
        print("Dataset not found.")
        return

    print("\n====== SEARCH MENU ======")
    for key, func in SEARCH_METHODS.items():
        print(f"{key}. {func.__name__}")

    choice = int(input("Enter choice: "))
    search_function = SEARCH_METHODS.get(choice)

    if not search_function:
        print("Invalid choice.")
        return

    target = int(input("Enter element to search: "))

    # Ensure sorted for binary & interpolation
    if search_function != searching.linear_search:
        data = sorted(data)

    index = search_function(data, target)

    print("Element found at index:" if index != -1 else "Element not found.", index)


# STACK

def stack_module(data):
    stack = Stack()

    [stack.push(item) for item in data]  # list comprehension side-effect

    print("Stack contents:")
    stack.display()


# QUEUE

def queue_module(data):
    queue = Queue()

    [queue.enqueue(item) for item in data]

    print("Queue contents:")
    queue.display()


# LINKED LIST

def linked_list_module(data):
    ll = LinkedList()

    for item in data:
        ll.insert_at_end(item)

    ll.traverse()


# RECURSION

def recursive_sum(data):
    return 0 if not data else data[0] + recursive_sum(data[1:])

def recursion_module(data):
    print("Recursive Sum:", recursive_sum(data))
    print("Factorial of dataset length:", factorial(len(data)))

def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)


# MAIN MENU

def main():

    manager = DataManager()

    MENU = {
        1: manager.create_dataset,
        2: manager.save_to_file,
        3: manager.load_from_file,
    }

    while True:

        print("\n====== MAIN MENU ======")
        print("1. Create Dataset")
        print("2. Save Dataset")
        print("3. Load Dataset")
        print("4. Sort Dataset")
        print("5. Search in Dataset")
        print("6. Stack Operations")
        print("7. Queue Operations")
        print("8. Linked List Operations")
        print("9. Recursive Operations")
        print("10. Exit")

        choice = int(input("Enter choice: "))

        if choice in MENU:
            MENU[choice]()

        elif choice == 4:
            manager.list_datasets()
            name = input("Enter dataset name: ")
            sorting_module(manager.get_dataset(name))

        elif choice == 5:
            manager.list_datasets()
            name = input("Enter dataset name: ")
            searching_module(manager.get_dataset(name))

        elif choice == 6:
            manager.list_datasets()
            name = input("Enter dataset name: ")
            stack_module(manager.get_dataset(name))

        elif choice == 7:
            manager.list_datasets()
            name = input("Enter dataset name: ")
            queue_module(manager.get_dataset(name))

        elif choice == 8:
            manager.list_datasets()
            name = input("Enter dataset name: ")
            linked_list_module(manager.get_dataset(name))

        elif choice == 9:
            manager.list_datasets()
            name = input("Enter dataset name: ")
            recursion_module(manager.get_dataset(name))

        elif choice == 10:
            print("Exiting...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()