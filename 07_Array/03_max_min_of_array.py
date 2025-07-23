"""
Problem: Maximum and Minimum Element in an Array

GFG Link2: https://www.geeksforgeeks.org/problems/largest-element-in-array4009/0
GFG Link1: https://www.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array/1

Description:
------------
Write functions to find the minimum and maximum element in a given array.

Approach:
---------
- Initialize both `min_val` and `max_val` to the first element.
- Traverse the array:
    - For max: Compare each element with `max_val`, update if greater.
    - For min: Compare each element with `min_val`, update if smaller.

Time Complexity  : O(n), where n is the size of the array.
Space Complexity : O(1), no extra space used.

Example:
--------
Input : [90, 80, 100, 70, 40, 30]
Output: Min = 30, Max = 100
"""

def find_min(arr):
    min_val = arr[0]

    for num in arr:
        if num < min_val:
            min_val = num

    return min_val


def find_max(arr):
    max_val = arr[0]

    for num in arr:
        if num > max_val:
            max_val = num

    return max_val


# --------- Main Program ---------
if __name__ == "__main__":
    arr = [90, 80, 100, 70, 40, 30]
    print("Minimum value in array:", find_min(arr))  # Output: 30
    print("Maximum value in array:", find_max(arr))  # Output: 100
