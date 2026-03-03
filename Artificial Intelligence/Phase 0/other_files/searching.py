# 🔹 Task 1 – Linear Search
# 🎯 Requirement:
# Create a function linear_search(arr, target)
# Traverse the list one by one
# If element found → return index
# If not found → return -1

def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1




# 🔹 Task 2 – Binary Search
# 🎯 Requirement:
# Create a function binary_search(arr, target)
# It must work only on sorted list
# Use start, end, mid logic

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1




def interpolation_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high and key >= arr[low] and key <= arr[high]:

        # If only one element
        if low == high:
            if arr[low] == key:
                return low
            return -1

        # Estimate position
        pos = low + ((key - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == key:
            return pos
        elif arr[pos] < key:
            low = pos + 1
        else:
            high = pos - 1

    return -1





def main_menu():
    while True:
        print("\n====== SEARCH MENU ======")
        print("1. Linear Search")
        print("2. Binary Search")
        print("3. Interpolation Search")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:
            try:
                arr = list(map(int, input("Enter elements separated by space: ").split()))
                if not arr:
                    print("List is empty.")
                    continue

                target = int(input("Enter target element: "))

                result = linear_search(arr, target)

                if result != -1:
                    print("Element found at index:", result)
                else:
                    print("Element not found.")

            except ValueError:
                print("Invalid input! Please enter integers only.")

        elif choice == 2:
            try:
                arr = list(map(int, input("Enter sorted elements separated by space: ").split()))
                if not arr:
                    print("List is empty.")
                    continue

                if arr != sorted(arr):
                    print("Error: Binary search requires a sorted list.")
                    continue

                target = int(input("Enter target element: "))

                result = binary_search(arr, target)

                if result != -1:
                    print("Element found at index:", result)
                else:
                    print("Element not found.")

            except ValueError:
                print("Invalid input! Please enter integers only.")

        elif choice == 3:
            try:
                arr = list(map(int, input("Enter sorted elements separated by space: ").split()))
                if not arr:
                    print("List is empty.")
                    continue

                if arr != sorted(arr):
                    print("Error: Interpolation search requires a sorted list.")
                    continue

                target = int(input("Enter target element: "))

                result = interpolation_search(arr, target)

                if result != -1:
                    print("Element found at index:", result)
                else:
                    print("Element not found.")

            except ValueError:
                print("Invalid input! Please enter integers only.")

        elif choice == 4:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")
        
main_menu()