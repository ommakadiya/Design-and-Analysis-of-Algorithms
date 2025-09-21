def binary_search(arr, left, right, key):
    if left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return binary_search(arr, mid + 1, right, key)
        else:
            return binary_search(arr, left, mid - 1, key)
    else:
        return -1

arr = [2, 7,5, 6,4,8, 9, 1]
left = 0
right = len(arr) - 1
key = 7
print(binary_search(arr, left, right, key))
