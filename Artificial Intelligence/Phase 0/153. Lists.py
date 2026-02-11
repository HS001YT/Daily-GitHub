# Implement list operations, remove duplicates using set, tuple unpacking

# 🔹 Task 1: List Operations (Core Task)
# Requirements:
# Take n numbers from user and store in a list
# Print:
# The list
# Sum of elements
# Largest and smallest element
# Add one new number to the list
# Remove one number from the list (user chooses)

# List Operations

def list_opr():
    nums = input("Enter elements of list space separated: ")
    nums = [int(i) for i in nums.split()]

    while True:
        print("""\nChoose what to do by entering number:
    1. Print list
    2. Print sum of elements of list
    3. Print largest and smallest element
    4. Add new element in list
    5. Remove element from the list
    6. Back""")
    
        choice = int(input("Enter your choice: "))
        if (choice == 1):
            print("Entered list:", nums)

        elif (choice == 2):
            sum = 0
            for i in nums:
                sum+=i
            print("Sum of elements:", sum)

        elif (choice == 3):
            largest = smallest = nums[0]
            for i in nums:
                if(i > largest):
                    largest = i
                if(i < smallest):
                    smallest = i
            print("Largest Number: %d\nSmallest Number: %d" % (largest, smallest))

        elif (choice == 4):
            new_element = int(input("Enter the element you want to enter: "))
            position = int(input("Enter the position where you want to insert:\n For reference size of list is (%d)\n" % (len(nums))))
            if ((position < 1) or position > (len(nums)+1)):
                print("Invalid Position")
            else:
                nums.insert(position - 1, new_element)

        elif(choice == 5):
            choice2 = int(input("Delete by element(1) or by position(2): "))
            if (choice2 == 1):
                element = int(input("Enter the element you want to delete: "))
                nums.remove(element)
            elif (choice2 == 2):
                positon = int(input("Enter the position from where you want to insert the element: "))
                nums.pop(positon)
            else:
                print("Invalid Choice!")

        elif (choice == 6):
            print("Exited from list operations.")
            break
        else:
            print("Invalid Choice.")



# 🔹 Task 2: Remove Duplicates Using Set
# Requirements:
# Take n numbers from user (allow duplicates)
# Store them in a list
# Convert list into a set to remove duplicates
# Convert back to list and print final result

def remove_duplicates():
    elements = input("Enter numbers with spaces: ")
    elements = [int(i) for i in elements.split()]
    original = elements

    elements = sorted(list(set(elements)))
    print("Original list with duplicates:", original)
    print("Modified list without duplicates:", elements)

    choice2 = int(input("Tell me whether you want to remove elements from list(1) or go back(2)\n"))
    if(choice2 == 1):
        remove_duplicates()
    elif(choice2 == 2):
        main_menu()
    else:
        print("Invalid Choce")



# 🔹 Task 3: Tuple Unpacking
# Requirements:
# Take 3 values as input:
# name
# age
# branch
# Store them in a tuple
# Unpack tuple into separate variables
# Print each variable separately

def tuple_unpack():
    while True:
        print("\n--- Tuple Unpacking ---")

        name = input("Enter name: ")
        age = int(input("Enter age: "))
        branch = input("Enter branch: ")

        # Store in tuple
        student = (name, age, branch)

        # Unpack tuple
        name_u, age_u, branch_u = student

        print("\nStored Tuple:", student)
        print("Name:", name_u)
        print("Age:", age_u)
        print("Branch:", branch_u)

        choice = int(input("\nDo you want to try again? Yes(1) / Back(2): "))

        if choice == 1:
            continue
        elif choice == 2:
            print("Exited from tuple unpacking.")
            break
        else:
            print("Invalid choice. Returning to main menu.")
            break



# Main Menu
def main_menu():
    print("""\nChoose what to do by entering number:
    1. List operations
    2. Remove duplicates Using set
    3. Tuple Unpacking
    4. Exit.""")
    
    choice = int(input("Enter your choice: "))
    if (choice == 1):
        list_opr()
        main_menu()
    elif (choice == 2):
        remove_duplicates()
    elif (choice == 3):
        tuple_unpack()
    elif (choice == 4):
        exit()
    else:
        print("Invalid Choice.")
main_menu()