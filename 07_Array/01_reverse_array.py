"""
Program: Reverse an Array

Description:
------------
This program reverses the given array using the **two-pointer approach**, 
which swaps elements from both ends of the array moving toward the center.

Functions:
----------
1. reverse_array(arr):
   - Reverses the array in-place using a two-pointer technique.
   - Time Complexity : O(n)
   - Space Complexity: O(1) (in-place)

2. Alternative Approach:
You can also reverse the array using Python's slicing feature:
    arr[::-1]
This creates a **new reversed list**, rather than modifying the original.

Example:
--------
Input : [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
"""

def reverse_array(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


def reverse_array_slicing(arr):
    return arr[::-1]


# --------- Main Program ---------
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Original Array:", arr)
    print("Reversed (Two-Pointer):", reverse_array(arr.copy()))
    print("Reversed (Slicing):", reverse_array_slicing(arr))
