def LinearSearch(value, target):
    n = len(value)
    for i in range(n):
        if value[i] == target:
            return i
    return -1
    
