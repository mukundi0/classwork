def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j + 1 ], arr[j]

    return arr

arr = [1,7,6,5,3,4,2,8,10,9]

sorted_arr = bubble_sort(arr)
print("Bubble Sort:", sorted_arr)