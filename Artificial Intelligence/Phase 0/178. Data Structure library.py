import sys
import os

# Add other_files folder to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "other_files"))

from ds_library import Stack, Queue, LinkedList


def main_menu():

    stack = Stack()
    queue = Queue()
    ll = LinkedList()

    while True:

        print("\n====== DATA STRUCTURE LIBRARY ======")
        print("1. Stack Push")
        print("2. Stack Pop")
        print("3. Queue Enqueue")
        print("4. Queue Dequeue")
        print("5. Linked List Insert")
        print("6. Linked List Delete")
        print("7. Display All")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            val = int(input("Enter value: "))
            stack.push(val)

        elif choice == "2":
            print("Popped:", stack.pop())

        elif choice == "3":
            val = int(input("Enter value: "))
            queue.enqueue(val)

        elif choice == "4":
            print("Dequeued:", queue.dequeue())

        elif choice == "5":
            val = int(input("Enter value: "))
            ll.insert(val)

        elif choice == "6":
            val = int(input("Enter value to delete: "))
            ll.delete(val)

        elif choice == "7":
            stack.display()
            queue.display()
            ll.display()

        elif choice == "8":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()