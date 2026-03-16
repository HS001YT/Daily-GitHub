# ================= SORTING ALGORITHMS =================

def bubble_sort(arr):

    a = arr.copy()

    for i in range(len(a)):
        for j in range(0, len(a)-i-1):

            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

    return a


def selection_sort(arr):

    a = arr.copy()

    for i in range(len(a)):

        min_index = i

        for j in range(i+1, len(a)):

            if a[j] < a[min_index]:
                min_index = j

        a[i], a[min_index] = a[min_index], a[i]

    return a


def insertion_sort(arr):

    a = arr.copy()

    for i in range(1, len(a)):

        key = a[i]
        j = i - 1

        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1

        a[j+1] = key

    return a


# ================= MERGE SORT =================

def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr)//2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):

    result = []
    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# ================= QUICK SORT =================

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


# ================= SEARCHING =================

def linear_search(arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


# ================= DATA STORAGE =================

data = []


# ================= DATA INPUT =================

def input_data():

    global data

    data = list(map(int, input("Enter numbers separated by space: ").split()))

    print("Data stored successfully.")


# ================= DISPLAY DATA =================

def display_data():

    if not data:
        print("No data available.")
        return

    print("Current Data:", data)


# ================= SORT MENU =================

def sorting_menu():

    if not data:
        print("Enter data first.")
        return

    print("\n===== SORTING MENU =====")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Sorted:", bubble_sort(data))

    elif choice == 2:
        print("Sorted:", selection_sort(data))

    elif choice == 3:
        print("Sorted:", insertion_sort(data))

    elif choice == 4:
        print("Sorted:", merge_sort(data))

    elif choice == 5:
        print("Sorted:", quick_sort(data))

    else:
        print("Invalid choice")


# ================= SEARCH MENU =================

def search_menu():

    if not data:
        print("Enter data first.")
        return

    print("\n===== SEARCH MENU =====")
    print("1. Linear Search")
    print("2. Binary Search")

    choice = int(input("Enter choice: "))

    target = int(input("Enter element to search: "))

    if choice == 1:

        index = linear_search(data, target)

    elif choice == 2:

        sorted_data = sorted(data)
        index = binary_search(sorted_data, target)

        print("Sorted Data:", sorted_data)

    else:
        print("Invalid choice")
        return

    if index != -1:
        print("Element found at index:", index)
    else:
        print("Element not found")


# ================= MAIN MENU =================

def main_menu():

    while True:

        print("\n====== SEARCH & SORT TOOLKIT ======")
        print("1. Enter Data")
        print("2. Display Data")
        print("3. Sorting Algorithms")
        print("4. Searching Algorithms")
        print("5. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            input_data()

        elif choice == 2:
            display_data()

        elif choice == 3:
            sorting_menu()

        elif choice == 4:
            search_menu()

        elif choice == 5:
            print("Exiting program.")
            break

        else:
            print("Invalid choice")


# ================= PROGRAM START =================

if __name__ == "__main__":
    main_menu()