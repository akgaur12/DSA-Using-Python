"""
Problem: Find Second Largest Element in Array
GFG Link: https://www.geeksforgeeks.org/problems/second-largest3735/1

Description:
------------
Write a function to find the **second largest** distinct element in an array of integers.

Constraints:
- If the array contains fewer than two distinct elements, return -1.

Approach:
---------
1. Initialize `first` and `second` to negative infinity (`float('-inf')`), which ensures any element in the array will be larger during comparison.
2. Traverse the array:
   - If the current number is greater than `first`, update `second = first` and `first = num`.
   - Else if the current number is distinct and lies between `first` and `second` (i.e., `first > num > second`), update `second = num`.
3. After traversal, if `second` remains negative infinity, it means no valid second largest distinct element was found; return -1.

Reason for initializing with `float('-inf')`:
---------------------------------------------
We use `float('-inf')` to represent the smallest possible starting value because:
- It allows the code to correctly handle arrays containing negative numbers and any range of integers.
- It ensures that any number in the array will be greater than this initial value, so `first` and `second` get properly updated.
- Using the first element of the array for initialization can cause incorrect results, especially when all elements are equal or when the array contains only one unique element.

Time Complexity  : O(n), where n is the number of elements in the array.
Space Complexity : O(1), constant space.

Example:
--------
Input : [12, 35, 1, 10, 34, 1]
Output: 34
"""


def getSecondLargest(arr):
    if len(arr) < 2:
        return -1  # Not enough elements for second largest

    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    return second if second != float('-inf') else -1


# --------- Main Program ---------
if __name__ == "__main__":
    arr1 = [12, 35, 1, 10, 34, 1]
    print("Second Largest:", getSecondLargest(arr1))  # Output: 34

    arr2 = [10]
    print("Second Largest:", getSecondLargest(arr2))  # Output: -1

    arr3 = [5, 5, 5]
    print("Second Largest:", getSecondLargest(arr3))  # Output: -1

    arr4 = [-10, -20, -30]
    print("Second Largest:", getSecondLargest(arr4))  # Output -20
