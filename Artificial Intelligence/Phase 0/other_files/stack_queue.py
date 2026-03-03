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

