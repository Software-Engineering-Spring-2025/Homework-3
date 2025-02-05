"""
Module: rand
This module provides a function to generate a randomized array.
"""

import secrets

def random_array(arr):
    """
    Generates a random array by replacing each element with a random number.

    Args:
        arr (list): A list to be filled with random numbers.

    Returns:
        list: The modified list with random numbers.
    """
    for i, _ in enumerate(arr):
        arr[i] = secrets.randbelow(20) + 1

    return arr
