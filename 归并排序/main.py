import math

def mergeSort(arr): 
    n = len(arr)
    if n < 2:
        return arr
    mid = math.floor(n/2)
    left = arr[:mid]
    right = arr[mid:]
    print(left, right)
    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) :
        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))

    while len(left) > 0:
        result.append(left.pop(0))

    while len(right) > 0:
        result.append(right.pop(0))
    return result


print(mergeSort([4,3,1,2]))