# 🔹 Algorithms You Must Implement
# 1️⃣ Bubble Sort
# Simple comparison-based
# Stable
# Worst-case: O(n²)

# 2️⃣ Selection Sort
# Not stable
# Fewer swaps than bubble
# Worst-case: O(n²)

# 3️⃣ Insertion Sort
# Good for small or nearly sorted data
# Stable
# Worst-case: O(n²)

# 4️⃣ Merge Sort
# Divide and conquer
# Stable
# Time: O(n log n)
# Uses extra space

# 5️⃣ Quick Sort
# Divide and conquer
# In-place
# Average: O(n log n)
# Worst-case: O(n²)
# Not stable

# 6️⃣ Heap Sort
# Uses heap data structure
# Not stable
# O(n log n)
# In-place

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr





def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr





def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr





def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result





def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1




def counting_sort(arr):
    if len(arr) == 0:
        return arr

    max_val = max(arr)
    min_val = min(arr)

    # Handle negative numbers as well
    range_of_elements = max_val - min_val + 1

    count = [0] * range_of_elements
    output = [0] * len(arr)

    # Count frequency
    for num in arr:
        count[num - min_val] += 1

    # Prefix sum (to make it stable)
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build output array (reverse loop for stability)
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1

    return output




def radix_sort(arr):
    if len(arr) == 0:
        return arr

    max_num = max(arr)
    exp = 1  # 10^i

    while max_num // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

    return arr




def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    # Put elements into buckets
    for num in arr:
        index = int(bucket_count * num)
        if index == bucket_count:
            index -= 1
        buckets[index].append(num)

    # Sort individual buckets
    for i in range(bucket_count):
        buckets[i].sort()

    # Concatenate buckets
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array




def main_menu():
    while True:
        print("\n====== SORTING MENU ======")
        print("1. Bubble Sort (Best for small or nearly sorted data)")
        print("2. Selection Sort (When fewer swaps are required)")
        print("3. Insertion Sort (Best for small or nearly sorted data)")
        print("4. Merge Sort (Best for large datasets, stable)")
        print("5. Quick Sort (Best average performance, large data)")
        print("6. Heap Sort (Guaranteed O(n log n), in-place)")
        print("7. Counting Sort (Best for small integer ranges)")
        print("8. Radix Sort (Digit-by-digit integer sorting)")
        print("9. Bucket Sort (Best for uniformly distributed float data)")
        print("10. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        if choice == 10:
            print("Exiting program...")
            break

        if choice < 1 or choice > 10:
            print("Invalid choice! Try again.")
            continue

        # For Bucket Sort → allow floats
        if choice == 9:
            try:
                arr = list(map(float, input("Enter elements separated by space (0 to 1 range preferred): ").split()))
                if not arr:
                    print("List cannot be empty.")
                    continue
            except ValueError:
                print("Invalid input! Enter numbers only.")
                continue
        else:
            try:
                arr = list(map(int, input("Enter elements separated by space: ").split()))
                if not arr:
                    print("List cannot be empty.")
                    continue
            except ValueError:
                print("Invalid input! Enter integers only.")
                continue

        arr_copy = arr.copy()

        if choice == 1:
            print("Using Bubble Sort...")
            print("Sorted Data:", bubble_sort(arr_copy))

        elif choice == 2:
            print("Using Selection Sort...")
            print("Sorted Data:", selection_sort(arr_copy))

        elif choice == 3:
            print("Using Insertion Sort...")
            print("Sorted Data:", insertion_sort(arr_copy))

        elif choice == 4:
            print("Using Merge Sort...")
            print("Sorted Data:", merge_sort(arr_copy))

        elif choice == 5:
            print("Using Quick Sort...")
            quick_sort(arr_copy, 0, len(arr_copy) - 1)
            print("Sorted Data:", arr_copy)

        elif choice == 6:
            print("Using Heap Sort...")
            print("Sorted Data:", heap_sort(arr_copy))

        elif choice == 7:
            print("Using Counting Sort...")
            print("Sorted Data:", counting_sort(arr_copy))

        elif choice == 8:
            print("Using Radix Sort...")
            print("Sorted Data:", radix_sort(arr_copy))

        elif choice == 9:
            print("Using Bucket Sort...")
            print("Sorted Data:", bucket_sort(arr_copy))

main_menu()