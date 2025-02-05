'''
uses two different algorithms to sort the random array
'''
import rand

def bubble_sort(arr):
    ''' 
    bubble sort pushes the max (in this case) element to the end in each iteration
    '''
    for i, _ in enumerate(arr):
        for j, _  in enumerate(arr):
            if j < len(arr) - i - 1 and arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def merge_sort(arr):
    ''' 
    a divide and conquer approach that splits the array in middle, sorts and merges it back
    '''
    if len(arr) <= 1:
        return arr
    half = len(arr)//2
    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))

def recombine(left_arr, right_arr):
    ''' 
    recombine is used by merge sort to facilitate the ordering of the split array
    '''
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    merge_index = 0
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[merge_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[merge_index] = right_arr[right_index]
            right_index += 1
        merge_index+=1
    for index, value in enumerate(right_arr[right_index:]):
        merge_arr[merge_index] = value
        merge_index+=1
    for index, value in enumerate(left_arr[left_index:]):
        merge_arr[merge_index] = value
        merge_index+=1
    for index, value in enumerate(left_arr):
        left_arr[index] = merge_arr[index]
    for index, value in enumerate(right_arr):
        right_arr[index] = merge_arr[len(left_arr)]
    return merge_arr

random_array = rand.random_array([None] * 20)
print(random_array)
merge_sorted_array = merge_sort(random_array)
sorted_array = bubble_sort(random_array)
print(sorted_array)
print(merge_sorted_array)
