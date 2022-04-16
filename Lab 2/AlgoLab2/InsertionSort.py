def InsertionSort(A):
    n  = len(A)  
    for j  in range (1,n):
        key =A[j]        
        i = j-1
        while i>=0  and A[i]>key:
            A[i+1] = A[i]
            i  =  i-1
        A[i+1] =  key

array= [10,9,1,8,3,2,4,5,90,5]
print(f"Input Array : \t {array}")
InsertionSort(array)
print(f"Sorted Array : \t {array}")