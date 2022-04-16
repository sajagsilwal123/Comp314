def MergeSort(array, left, right):
    if left >= right:
        return

    middle = (left + right)//2
    MergeSort(array, left, middle)
    MergeSort(array, middle + 1, right)
    Merge(array, left, right, middle)

def Merge(array, left, right, middle):

    leftCopy = array[left:middle + 1]
    rightCopy = array[middle+1:right+1]


    leftCopyIndex = 0
    rightCopyIndex = 0
    sortedIndex = left

   
    while leftCopyIndex < len(leftCopy) and rightCopyIndex < len(rightCopy):

        
        if leftCopy[leftCopyIndex] <= rightCopy[rightCopyIndex]:
            array[sortedIndex] = leftCopy[leftCopyIndex]
            leftCopyIndex = leftCopyIndex + 1
        
        else:
            array[sortedIndex] = rightCopy[rightCopyIndex]
            rightCopyIndex = rightCopyIndex + 1

     
        sortedIndex = sortedIndex + 1


    while leftCopyIndex < len(leftCopy):
        array[sortedIndex] = leftCopy[leftCopyIndex]
        leftCopyIndex = leftCopyIndex + 1
        sortedIndex = sortedIndex + 1

    while rightCopyIndex < len(rightCopy):
        array[sortedIndex] = rightCopy[rightCopyIndex]
        rightCopyIndex = rightCopyIndex + 1
        sortedIndex = sortedIndex + 1


# array=[9,8,7,6,5,4,3,2,1,0]
# print(f"Input Array : \t {array}")

# MergeSort(array,0,len(array))
# print(f"Sorted Array : \t {array}")