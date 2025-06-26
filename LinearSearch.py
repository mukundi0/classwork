def linear_Search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i #return index of target

    return -1

arr = [10, 3, 7, 8, 2, 5]
target = 8
result = linear_Search(arr,target)

print("Linear Search Result:", "Found at index" if result != -1 else "Not found", result)