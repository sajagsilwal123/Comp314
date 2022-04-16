import math as mt

def BinarySearch(arr, target, l, r):
    if r>l:
        mid = (r+l)//2
        if(arr[mid]==target):
            return mid
        elif(target>arr[mid]):
            return BinarySearch(arr, target, mid+1, r )
        elif(target<arr[mid]):
            return BinarySearch(arr, target, l, mid-1)
    else:
        return -1


arr = sorted([1,9, 4, 3, 20, 0, 500, 300, 35])
test  = BinarySearch(arr, 90 , 0, len(arr)-1)
print(test)
