"""
Program: Check if Array is Sorted (Ascending Order)
GFG Link: https://www.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1

Description:
------------
This program checks whether the given list of elements is sorted 
in non-decreasing (ascending) order.

Logic:
------
- Iterate through the list from index 0 to len(arr) - 1.
- Compare each element with its next one.
- If any element is greater than the next, the array is not sorted.

Time Complexity  : O(n), where n is the number of elements in the list.
Space Complexity : O(1), uses constant space.

Returns:
--------
- True  : if the array is sorted in ascending order.
- False : if the array is not sorted.

Examples:
---------
Input : [10, 20, 30, 40, 50]
Output: True

Input : [90, 80, 100, 70, 40, 30]
Output: False
"""

def check_sorted(arr):

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False

    return True


# --------- Main Program ---------
if __name__ == "__main__":
    arr1 = [10, 20, 30, 40, 50]
    print("Is arr1 sorted? ->", check_sorted(arr1))  # Output: True

    arr2 = [90, 80, 100, 70, 40, 30]
    print("Is arr2 sorted? ->", check_sorted(arr2))  # Output: False
