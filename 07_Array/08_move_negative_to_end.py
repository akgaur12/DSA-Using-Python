"""
Problem: Move all negative elements to end
GFG Link: https://www.geeksforgeeks.org/problems/move-all-negative-elements-to-end1813/1

Description:
------------
Given an array `arr` of integers, the goal is to rearrange its elements such that
all **positive** numbers appear **before** all **negative** numbers,
while **preserving the relative order** of the elements.

This must be done by modifying the input array in-place using a temporary array.

Approach:
---------
1. Create a temporary array `temp` of the same size.
2. Traverse the input array and copy all non-negative (positive or zero) elements into `temp`.
3. Traverse the array again to copy all negative elements into `temp`, preserving their order.
4. Copy the elements from `temp` back to the original array `arr`.

Time Complexity: O(n)  
Space Complexity: O(n) – due to usage of a temporary array

Example:
--------
Input:  arr = [1, -2, 3, -4, 5], n = 5  
Output: [1, 3, 5, -2, -4]  # Positives first, negatives after; order maintained.
"""

def segregateElements(arr, n):
    if n == 0 or n == 1:
        return  # No rearrangement needed for 0 or 1 element

    # Step 1: Create a temporary array
    temp = [0 for _ in range(n)]
    j = 0

    # Step 2: Copy all non-negative numbers
    for i in range(n):
        if arr[i] >= 0:
            temp[j] = arr[i]
            j += 1

    # Step 3: Copy all negative numbers
    for i in range(n):
        if arr[i] < 0:
            temp[j] = arr[i]
            j += 1

    # Step 4: Copy back to original array
    for k in range(n):
        arr[k] = temp[k]



# --------- Main Program (Sample Usage) ---------
if __name__ == "__main__":
    arr = [1, -2, 3, -4, 5]
    n = len(arr)

    segregateElements(arr, n)
    print("Rearranged Array:", arr)
