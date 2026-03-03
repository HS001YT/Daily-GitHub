import json
import time

from other_files import (
    bubble_sort, selection_sort, insertion_sort,
    merge_sort, quick_sort, heap_sort,
    counting_sort, radix_sort, bucket_sort,
    linear_search, binary_search, interpolation_search,
    Stack, Queue, LinkedList,
    validate_integer_list, recursive_sum, factorial
)


# ================= DATA MANAGER =================

class DataManager:

    def __init__(self):
        self.datasets = {}

    def create_dataset(self):
        name = input("Enter dataset name: ").strip()

        raw = input("Enter numbers separated by space: ")
        data = validate_integer_list(raw)

        if data is None:
            print("Invalid input.")
            return

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

    def list_datasets(self):
        print("Available datasets:", list(self.datasets.keys()))

    def get_dataset(self, name):
        return self.datasets.get(name)


# ================= SORTING =================

SORTING_METHODS = {
    1: bubble_sort,
    2: selection_sort,
    3: insertion_sort,
    4: merge_sort,
    5: quick_sort,
    6: heap_sort,
    7: counting_sort,
    8: radix_sort,
    9: bucket_sort,
}


def sorting_module(data):
    if not data:
        print("Dataset not found.")
        return

    print("\n====== SORTING MENU ======")
    for k, v in SORTING_METHODS.items():
        print(f"{k}. {v.__name__}")

    choice = int(input("Enter choice: "))
    func = SORTING_METHODS.get(choice)

    if not func:
        print("Invalid choice.")
        return

    start = time.time()
    result = func(data.copy())
    end = time.time()

    print("Sorted Data:", result)
    print("Time Taken:", round(end - start, 6))


# ================= SEARCHING =================

SEARCH_METHODS = {
    1: linear_search,
    2: binary_search,
    3: interpolation_search,
}


def searching_module(data):
    if not data:
        print("Dataset not found.")
        return

    print("\n====== SEARCH MENU ======")
    for k, v in SEARCH_METHODS.items():
        print(f"{k}. {v.__name__}")

    choice = int(input("Enter choice: "))
    target = int(input("Enter element: "))

    func = SEARCH_METHODS.get(choice)
    if not func:
        print("Invalid choice.")
        return

    if func != linear_search:
        data = sorted(data)

    index = func(data, target)

    print("Found at index:" if index != -1 else "Not found.", index)


# ================= STACK =================

def stack_module(data):
    stack = Stack()
    [stack.push(x) for x in data]
    stack.display()


# ================= QUEUE =================

def queue_module(data):
    queue = Queue()
    [queue.enqueue(x) for x in data]
    queue.display()


# ================= LINKED LIST =================

def linked_list_module(data):
    ll = LinkedList()
    for x in data:
        ll.insert_at_end(x)
    ll.traverse()


# ================= RECURSION =================

def recursion_module(data):
    print("Recursive Sum:", recursive_sum(data))
    print("Factorial of length:", factorial(len(data)))


# ================= MAIN =================

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

        elif choice in [4,5,6,7,8,9]:
            manager.list_datasets()
            name = input("Enter dataset name: ")
            data = manager.get_dataset(name)

            if choice == 4:
                sorting_module(data)
            elif choice == 5:
                searching_module(data)
            elif choice == 6:
                stack_module(data)
            elif choice == 7:
                queue_module(data)
            elif choice == 8:
                linked_list_module(data)
            elif choice == 9:
                recursion_module(data)

        elif choice == 10:
            print("Exiting...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()