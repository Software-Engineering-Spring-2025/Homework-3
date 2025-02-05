import rand

def mergeSort(arr):
    if (len(arr) == 1):
        return arr

    half = len(arr)//2

    return recombine(mergeSort(arr[:half]), mergeSort(arr[half:]))

def recombine(leftArr, rightArr):
    leftIndex = 0
    rightIndex = 0
    mergeArr = [None] * (len(leftArr) + len(rightArr))
    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            rightIndex += 1
            mergeArr[leftIndex + rightIndex] = leftArr[leftIndex]
        else:
            leftIndex += 1
            mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]

    for i in range(rightIndex, len(rightArr)):
        mergeArr[leftIndex + rightIndex] = rightArr[i]
    
    for i in range(leftIndex, len(leftArr)):
        mergeArr[leftIndex + rightIndex] = leftArr[i]

    return mergeArr

arr = rand.random_array([None] * 20)
arr_out = mergeSort(arr)

print(arr_out)

def selection_sort(arr):
    """Selection sort algorithm."""

    n = len(arr)
    arr_copy = arr[:]  # Create a copy

    for i in range(n):
        min_idx = i
        for j in range(i, n):  # Issue: Should be range(i + 1, n)
            if arr_copy[j] < arr_copy[min_idx]:
                min_idx = j

        arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]

    return arr_copy

