"""
This code generates random integers for input array
"""
import random


def random_array(arr):
    """
    This function generates 20 random integers to return as input array
    """
    for i, _ in enumerate(arr):
        arr[i] = random.randint(1, 20)
    return arr
