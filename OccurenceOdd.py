def occurence_odd(arr, key):
    count = 0
    for i in range(0, len(arr), 2):
        if arr[i] == key:
            count += 1
    return count
arr=[1,2,3,2,5,3,2]
key=2
print(occurence_odd(arr,key))