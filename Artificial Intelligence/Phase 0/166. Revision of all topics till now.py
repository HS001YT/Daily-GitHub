# 🎯 Task: Build a “Data Structure & Algorithm Manager System”

# You will create a menu-driven system that integrates your previous implementations.

# 🔹 PART 1 – Data Storage System (OOP + File)
# Create a class:
# DataManager
# It should:
# Store multiple numeric datasets (lists)
# Save datasets to file
# Load datasets from file
# Remove duplicates using set
# Maintain record in dictionary format:
# Example structure:
# {
#    "dataset1": [5,2,8,1],
#    "dataset2": [10,4,7]
# }

# 🔹 PART 2 – Sorting Module
# Allow user to choose:
# Bubble
# Selection
# Insertion
# Merge
# Quick
# Heap
# Counting
# Radix
# Bucket
# System should:
# Take selected dataset
# Apply chosen sort
# Display sorted result
# Show time taken

# 🔹 PART 3 – Searching Module
# Linear search
# Binary search
# Interpolation search
# Return index or message

# 🔹 PART 4 – Stack & Queue Integration
# Allow user to:
# Push sorted dataset elements into stack
# Enqueue them into queue
# Perform operations and display

# 🔹 PART 5 – Linked List Conversion
# Convert one dataset into linked list
# Allow:
# Insert
# Delete
# Traverse

# 🔹 PART 6 – Recursion Use
# Use recursion in at least one place:
# Recursive factorial of dataset length
# OR
# Recursive sum of dataset

# 🔥 Final Structure (Menu Example)
# 1. Create Dataset
# 2. Save Dataset
# 3. Load Dataset
# 4. Sort Dataset
# 5. Search in Dataset
# 6. Stack Operations
# 7. Queue Operations
# 8. Linked List Operations
# 9. Recursive Operations
# 10. Exit

# ================= IMPORTS =================
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "other_files"))

from sorting import *
from searching import *
from stack_queue import Stack, Queue
from linked_list import LinkedList

import time
import json


# Class - Data Manager

class DataManager:

    def __init__(self):
        self.datasets = {}

    def save_to_file(self):
        filename = input("Enter filename to save (example: data.json): ")

        # Base directory path
        base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "other-files")
        os.makedirs(base_path, exist_ok=True)
        full_path = os.path.join(base_path, filename)

        with open(full_path, "w") as file:
            json.dump(self.datasets, file)

        print("Data saved successfully.")


    def load_from_file(self):
        filename = input("Enter filename to load: ")

        base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "other-files")
        full_path = os.path.join(base_path, filename)

        try:
            with open(full_path, "r") as file:
                self.datasets = json.load(file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("File not found.")

    def load_from_file(self):
        filename = input("Enter filename to load: ")

        try:
            with open(filename, "r") as file:
                self.datasets = json.load(file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("File not found.")

    def get_dataset(self):
        name = input("Enter dataset name: ")
        return self.datasets.get(name)


# Sorting

def sorting_module(data):

    if not data:
        print("Dataset not found.")
        return

    print("\n====== SORTING MENU ======")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    print("6. Heap Sort")
    print("7. Counting Sort")
    print("8. Radix Sort")
    print("9. Bucket Sort")

    choice = int(input("Enter choice: "))

    start = time.time()

    if choice == 1:
        result = bubble_sort(data.copy())
    elif choice == 2:
        result = selection_sort(data.copy())
    elif choice == 3:
        result = insertion_sort(data.copy())
    elif choice == 4:
        result = merge_sort(data.copy())
    elif choice == 5:
        result = quick_sort(data.copy())
    elif choice == 6:
        result = heap_sort(data.copy())
    elif choice == 7:
        result = counting_sort(data.copy())
    elif choice == 8:
        result = radix_sort(data.copy())
    elif choice == 9:
        result = bucket_sort(data.copy())
    else:
        print("Invalid choice.")
        return

    end = time.time()

    print("Sorted Data:", result)
    print("Time Taken:", end - start)


# Searching

def searching_module(data):

    if not data:
        print("Dataset not found.")
        return

    print("\n====== SEARCH MENU ======")
    print("1. Linear Search")
    print("2. Binary Search")
    print("3. Interpolation Search")

    choice = int(input("Enter choice: "))
    target = int(input("Enter element to search: "))

    if choice == 1:
        index = linear_search(data, target)
    elif choice == 2:
        index = binary_search(sorted(data), target)
    elif choice == 3:
        index = interpolation_search(sorted(data), target)
    else:
        print("Invalid choice.")
        return

    if index != -1:
        print("Element found at index:", index)
    else:
        print("Element not found.")


# Stack

def stack_module(data):

    stack = Stack()

    for item in data:
        stack.push(item)

    print("Stack after pushing elements:")
    stack.display()


# Queue

def queue_module(data):

    queue = Queue()

    for item in data:
        queue.enqueue(item)

    print("Queue after enqueue:")
    queue.display()


# Linked List

def linked_list_module(data):

    ll = LinkedList()

    for item in data:
        ll.insert_at_end(item)

    print("Linked List elements:")
    ll.traverse()


# Recursion

def recursive_sum(data):
    if len(data) == 0:
        return 0
    return data[0] + recursive_sum(data[1:])

def recursion_module(data):
    print("Recursive Sum of Dataset:", recursive_sum(data))


# Main Menu

def main():

    manager = DataManager()

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

        if choice == 1:
            manager.create_dataset()

        elif choice == 2:
            manager.save_to_file()

        elif choice == 3:
            manager.load_from_file()

        elif choice == 4:
            data = manager.get_dataset()
            sorting_module(data)

        elif choice == 5:
            data = manager.get_dataset()
            searching_module(data)

        elif choice == 6:
            data = manager.get_dataset()
            stack_module(data)

        elif choice == 7:
            data = manager.get_dataset()
            queue_module(data)

        elif choice == 8:
            data = manager.get_dataset()
            linked_list_module(data)

        elif choice == 9:
            data = manager.get_dataset()
            recursion_module(data)

        elif choice == 10:
            print("Exiting...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()