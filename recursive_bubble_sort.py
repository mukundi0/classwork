def recursive_bubble_sort(arr, n = None):
    if n is None:
        n = len(arr)

    if n == 1:
        return arr

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return recursive_bubble_sort(arr, n - 1)

arr = [1,7,6,5,3,4,2,8,10,9]

sorted_arr = recursive_bubble_sort(arr)
print("Bubble Sort:", sorted_arr)

