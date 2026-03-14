# ================= STACK =================

class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            print("Stack Underflow")
            return None
        return self.items.pop()

    def display(self):
        print("Stack:", self.items)


# ================= QUEUE =================

class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.items:
            print("Queue Underflow")
            return None
        return self.items.pop(0)

    def display(self):
        print("Queue:", self.items)


# ================= LINKED LIST =================

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None


    def insert(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node


    def delete(self, key):

        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None

        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        prev.next = temp.next


    def display(self):

        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")