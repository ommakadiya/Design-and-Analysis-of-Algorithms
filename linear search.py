def linear_search(arr, target):
    if target in arr:
        return arr.index(target)
    else:
        return -1

arr = [1, 2, 3, 4, 5, 6, 7]
target = 3
result = linear_search(arr, target)

if result != -1:
    print(f"Target {target} found at index: {result}")
else:
    print(f"Target {target} not found in the array")
