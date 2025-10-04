def minmax(arr):
    if(len(arr)==1):
        return arr[0],arr[0]
    mid=int(len(arr)/2)
    lmin,lmax=minmax(arr[:mid])
    rmin,rmax=minmax(arr[mid:])
    return(min(lmin,rmin),max(lmax,rmax))

arr=[2,3,6,9,5,1,7]
minele,maxele=minmax(arr)
print("min ele is ",minele)
print("max ele is ",maxele)
