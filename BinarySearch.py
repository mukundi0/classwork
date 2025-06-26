def binary_search(arr, target): #works on sorted lists
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

arr = [2, 3, 5, 7, 8, 10]
target = 8
result = binary_search(arr, target)

print("Binary Search result:", "Found at index" if result != -1 else "Not found", result)