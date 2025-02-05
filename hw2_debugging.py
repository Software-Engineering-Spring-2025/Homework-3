"""
Module: hw2_debugging
This module implements merge sort and insertion sort algorithms.
"""
import secrets


def merge_sort(array):
    """
    Sorts an array using the merge sort algorithm.

    Args:
        array (list): The list to be sorted.

    Returns:
        list: A sorted list.
    """

    if len(array) == 1:
        return array

    half = len(array) // 2

    return recombine(merge_sort(array[:half]), merge_sort(array[half:]))


def recombine(left_arr, right_arr):
    """
    Merges two sorted arrays into a single sorted array.

    Args:
        left_arr (list): Left half of a sorted list.
        right_arr (list): Right half of a sorted list.

    Returns:
        list: A merged and sorted list.
    """

    left_index = 0
    right_index = 0
    merge_arr = []
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merge_arr.append(right_arr[right_index])
            right_index += 1

    merge_arr.extend(left_arr[left_index:])
    merge_arr.extend(right_arr[right_index:])

    return merge_arr


arr = [secrets.randbelow(101) for _ in range(20)]
arr_out = merge_sort(arr)
print("Sorted Array (Merge Sort):", arr_out)


def insertion_sort(input_list):
    """
    Sorts an array using insertion sort.

    Args:
        input_list (list): The list to be sorted.

    Returns:
        list: A sorted list.
    """

    n = len(input_list)
    for i in range(1, n):
        itm = input_list[i]
        j = i - 1
        while j >= 0 and input_list[j] > itm:
            input_list[j + 1] = input_list[j]  # Corrected shifting logic
            j -= 1
        input_list[j + 1] = itm  # Corrected placement of key
    return input_list

