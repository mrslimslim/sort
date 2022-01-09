def sortArr(arr):
    n = len(arr)
    if n <= 1 :
        return arr
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
        
    return arr
print(sortArr([4, 2, 1, 3]))    