# 🔹 Task – Implement Singly Linked List
# 🎯 Step 1 – Create Node Class
# Each node must contain:
# data
# next (reference to next node)
# 🎯 Step 2 – Create LinkedList Class

# It must contain:
# head (initially None)
# 🔹 Mandatory Methods
# 1️⃣ insert_at_end(data)
# Create new node
# If list empty → make it head
# Otherwise traverse till last and attach
# 2️⃣ insert_at_beginning(data)
# New node’s next → current head
# Update head
# 3️⃣ delete(data)
# Delete first occurrence of given value
# If value not found → print message
# 4️⃣ traverse()
# Print all elements in order

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # 1️⃣ Insert at End
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # 2️⃣ Insert at Beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 3️⃣ Delete first occurrence of value
    def delete(self, data):
        if self.head is None:
            print("List is empty")
            return

        # If head needs to be deleted
        if self.head.data == data:
            self.head = self.head.next
            return

        temp = self.head
        prev = None

        while temp and temp.data != data:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found in list")
            return

        prev.next = temp.next

    # 4️⃣ Traverse
    def traverse(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")






def main_menu():
    ll = LinkedList()

    while True:
        print("\n====== SINGLY LINKED LIST MENU ======")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Delete")
        print("4. Traverse")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:
            data = input("Enter value to insert at beginning: ")
            ll.insert_at_beginning(data)
            print("Inserted successfully.")

        elif choice == 2:
            data = input("Enter value to insert at end: ")
            ll.insert_at_end(data)
            print("Inserted successfully.")

        elif choice == 3:
            data = input("Enter value to delete: ")
            ll.delete(data)

        elif choice == 4:
            ll.traverse()

        elif choice == 5:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")
