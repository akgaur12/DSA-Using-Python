"""
Program: Reverse an Array Using Recursion

Description:
------------
This program defines a recursive function to reverse the contents of a list (array)
in place, using the two-pointer approach — one starting from the beginning and the
other from the end.

Approach:
---------
- Swap the elements at the `start` and `end` indices.
- Move inward by incrementing `start` and decrementing `end`.
- Base case: When `start` is greater than or equal to `end`, the recursion stops.

Time Complexity:
----------------
- O(n), where n is the length of the array.

Space Complexity:
-----------------
- O(n) due to the recursive call stack.

Example:
--------
Input : [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
"""


def reverse_array(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverse_array(arr, start + 1, end - 1)


# --------- Example Usage ---------
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Original array:", arr)
    reverse_array(arr, 0, len(arr) - 1)
    print("Reversed array:", arr) 
