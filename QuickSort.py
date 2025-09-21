def partition(arr,low,high):
    pivot=arr[high]
    pIndex = low
    for i in range(low,high):
        if arr[i] <= pivot:
            arr[pIndex],arr[i]=arr[i],arr[pIndex]
            pIndex+=1
            arr[pIndex],arr[high]=arr[high],arr[pIndex]
    arr[high], arr[pIndex] = arr[pIndex], arr[high]
    return pIndex + 1

def quicksort(arr,low,high):
    if low < high:
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot - 1)
        quicksort(arr, pivot + 1, high)

arr = [64,34,25,12,22,11,90]
quicksort(arr,0,len(arr)-1)
print(arr)
