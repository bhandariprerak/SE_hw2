"""
This file tests the merge_sort function
"""
import hw2_debugging

def test_merge_sort():
    """
    This function tests the merge_sort function from hw2_debugging.py
    It gives array of 20 integers to sort and compares them with the expected output
    """
    assert hw2_debugging.merge_sort([19, 19, 17, 18, 19, 5, 19, 18, 4, 15, 7, 19, 15, 1, 17, 9, 9, 12, 8, 1]) == [1, 1, 4, 5, 7, 8, 9, 9, 12, 15, 15, 17, 17, 18, 18, 19, 19, 19, 19, 19]
    assert hw2_debugging.merge_sort([2, 10, 13, 14, 9, 20, 12, 9, 14, 19, 1, 19, 13, 19, 8, 19, 14, 17, 1, 6]) == [1, 1, 2, 6, 8, 9, 9, 10, 12, 13, 13, 14, 14, 14, 17, 19, 19, 19, 19, 20]
    assert hw2_debugging.merge_sort([15, 20, 10, 5, 20, 2, 12, 9, 1, 7, 20, 18, 10, 15, 17, 7, 19, 15, 7, 18]) == [1, 2, 5, 7, 7, 7, 9, 10, 10, 12, 15, 15, 15, 17, 18, 18, 19, 20, 20, 20]