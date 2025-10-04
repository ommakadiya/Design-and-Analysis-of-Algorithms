def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [4, 5, 3, 9, 8, 1, 2, 7]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)
