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




def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If root is not largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr




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




