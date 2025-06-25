"""
Problem: Maximum Product Subarray
LeetCode Link: https://leetcode.com/problems/maximum-product-subarray/description/

Description:
------------
Given an array that contains both positive and negative integers, 
the task is to find the contiguous subarray (containing at least one number) 
which has the largest product and return the product.

Example:
---------
Input: arr = [-2, 6, -3, -10, 0, 2]
Output: 180  (Subarray: [6, -3, -10])

Approach 1: Brute Force (Nested Loops)
--------------------------------------
- Traverse all possible subarrays and compute the product of each.
- Keep updating the maximum product found.

Time Complexity: O(n²)
Space Complexity: O(1)

Approach 2: Optimized (Kadane-like for Product)
-----------------------------------------------
- Maintain two variables: `currMax` and `currMin`, because a negative number 
  can flip min to max and vice versa.
- At every step, compute the maximum and minimum product ending at that index.
- Update the global max product accordingly.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# ----------------- Approach 1: Brute Force ----------------- #
def maxProduct_brute_force(arr):
    n = len(arr)
    result = arr[0]

    for i in range(n):
        mul = 1
        for j in range(i, n):
            mul *= arr[j]
            result = max(result, mul)

    return result


# ----------------- Approach 2: Optimized ----------------- 
def maxProduct_optimized(arr):
    n = len(arr)
    currMax = arr[0]
    currMin = arr[0]
    maxProd = arr[0]

    for i in range(1, n):
        # Save current max to temp before it is updated
        temp = max(arr[i], arr[i] * currMax, arr[i] * currMin)
        currMin = min(arr[i], arr[i] * currMax, arr[i] * currMin)
        currMax = temp
        maxProd = max(maxProd, currMax)

    return maxProd


# ----------------- Example Usage ----------------- 
if __name__ == "__main__":
    arr = [-2, 6, -3, -10, 0, 2]
    print("Brute Force Max Product:", maxProduct_brute_force(arr))   # Output: 180
    print("Optimized Max Product:", maxProduct_optimized(arr))       # Output: 180
