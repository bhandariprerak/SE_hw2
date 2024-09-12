"""
This code generates random integers for input array
"""
import subprocess


def random_array(arr):
    """
    This function generates 20 random integers to return as input array
    """
    shuffled_num = None
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["gshuf", "-i", "1-20", "-n", "1"], capture_output=True, check=False)
        arr[i] = int(shuffled_num.stdout)
    return arr
