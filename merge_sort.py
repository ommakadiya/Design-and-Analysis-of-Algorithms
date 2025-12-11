def merge_sort(a,b):
    result= []
    i=j= 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    # while i < len(a):
    #     result.append(a[i])
    #     i += 1
    # while j < len(b):
    #     result.append(b[j])
    #     j += 1
    return result

def merge(arr):
    if len(arr) <= 1:
        return arr
    mid = int(len(arr)/2)
    left = arr[:mid]
    right = arr[mid:]
    left = merge(left)
    right = merge(right)
    return merge_sort(left, right)

arr= [38, 27, 43, 3, 9, 82, 10]
print(merge(arr)) 


