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





