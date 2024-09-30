"""
This code demonstrates the merge sort algorithm.

The merge_sort function recursively splits the array into halves 
and uses the recombine function to merge and sort the arrays back together.
"""
import rand


def merge_sort(arr):
    """
    Performs merge sort on the input array.

    Parameters:
    arr (list): The list to be sorted.

    Returns:
    list: The sorted list.
    """

    # This condition handles the recursion and case when input array is empty
    if len(arr) == 1 or len(arr) == 0:
        return arr

    half = len(arr)//2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    """
    Recombines two sorted arrays into a single sorted array.

    Parameters:
    left_arr (list): The left array.
    right_arr (list): The right array.

    Returns:
    list: The merged and sorted array.
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

    # adding all remaining elements of right array
    for i in range(right_index, len(right_arr)):
        merge_arr.append(right_arr[i])
    # adding all remaining elements of left array
    for i in range(left_index, len(left_arr)):
        merge_arr.append(left_arr[i])

    return merge_arr


input_arr = rand.random_array([None] * 20)
print(input_arr)
arr_out = merge_sort(input_arr)
print(arr_out)
