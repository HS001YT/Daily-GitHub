# 🔹 Task 1 – Implement Stack Using List# 🎯 Requirement:
# Create a class named Stack.
# It must include:
# An internal list to store elements
# Method push(element) → add element
# Method pop() → remove top element
# Method peek() → show top element without removing
# Method is_empty() → return True/False
# Method display() → show full stack

class Stack:
    def __init__(self):
        self.stack = []   # internal list

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack elements (top -> bottom):")
            for element in reversed(self.stack):
                print(element)



# 🔹 Task 2 – Implement Queue Using collections.deque
# Use:

# from collections import deque

# Create a class named Queue.
# 🎯 Requirement:
# Internal deque to store elements
# Method enqueue(element) → add to rear
# Method dequeue() → remove from front
# Method front() → show first element
# Method is_empty()
# Method display()

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()   # internal deque

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.popleft()

    def front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue elements (front -> rear):")
            for element in self.queue:
                print(element)

def main_menu():
    stack = Stack()
    queue = Queue()

    while True:
        print("\n====== MAIN MENU ======")
        print("1. Stack Operations")
        print("2. Queue Operations")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        # ---------------- STACK MENU ----------------
        if choice == 1:
            while True:
                print("\n--- Stack Menu ---")
                print("1. Push")
                print("2. Pop")
                print("3. Peek")
                print("4. Is Empty")
                print("5. Display")
                print("6. Back")

                try:
                    stack_choice = int(input("Enter your choice: "))
                except ValueError:
                    print("Invalid input! Enter a number.")
                    continue

                try:
                    if stack_choice == 1:
                        element = input("Enter element to push: ")
                        stack.push(element)
                        print("Element pushed successfully.")

                    elif stack_choice == 2:
                        print("Popped element:", stack.pop())

                    elif stack_choice == 3:
                        print("Top element:", stack.peek())

                    elif stack_choice == 4:
                        print("Stack is empty?", stack.is_empty())

                    elif stack_choice == 5:
                        stack.display()

                    elif stack_choice == 6:
                        break

                    else:
                        print("Invalid choice!")

                except Exception as e:
                    print("Error:", e)

        # ---------------- QUEUE MENU ----------------
        elif choice == 2:
            while True:
                print("\n--- Queue Menu ---")
                print("1. Enqueue")
                print("2. Dequeue")
                print("3. Front")
                print("4. Is Empty")
                print("5. Display")
                print("6. Back")

                try:
                    queue_choice = int(input("Enter your choice: "))
                except ValueError:
                    print("Invalid input! Enter a number.")
                    continue

                try:
                    if queue_choice == 1:
                        element = input("Enter element to enqueue: ")
                        queue.enqueue(element)
                        print("Element enqueued successfully.")

                    elif queue_choice == 2:
                        print("Dequeued element:", queue.dequeue())

                    elif queue_choice == 3:
                        print("Front element:", queue.front())

                    elif queue_choice == 4:
                        print("Queue is empty?", queue.is_empty())

                    elif queue_choice == 5:
                        queue.display()

                    elif queue_choice == 6:
                        break

                    else:
                        print("Invalid choice!")

                except Exception as e:
                    print("Error:", e)

        elif choice == 3:
            print("Exiting program...")
            break

        else:
            print("Invalid choice!")
main_menu()