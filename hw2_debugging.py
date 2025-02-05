"""Module containing debugging code."""

import rand

def merge_sort(array):
    """Function for merge sort."""
    if len(array) == 1:
        return array

    half = len(array)//2

    return recombine(merge_sort(array[:half]), merge_sort(array[half:]))

def recombine(left_arr, right_arr):
    """Function for recombining"""
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            right_index += 1
            merge_arr[left_index + right_index] = left_arr[left_index]
        else:
            left_index += 1
            merge_arr[left_index + right_index] = right_arr[right_index]

    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + right_index] = right_arr[i]

    for i in range(left_index, len(left_arr)):
        merge_arr[left_index + right_index] = left_arr[i]

    return merge_arr

arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)

print(arr_out)

def selection_sort(arr1):
    """Selection sort algorithm."""

    n = len(arr1)
    arr_copy = arr1[:]  # Create a copy

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):  # Issue: Should be range(i + 1, n)
            if arr_copy[j] < arr_copy[min_idx]:
                min_idx = j

        arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]

    return arr_copy
