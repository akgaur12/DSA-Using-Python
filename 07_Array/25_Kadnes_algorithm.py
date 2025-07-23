"""
Problem: Maximum Subarray Sum (Kadane's Algorithm)
GFG Link: https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1

Description:
-------------
Given an integer array `arr`, find the **maximum sum of a contiguous subarray** (containing at least one number).

This is a classic problem commonly solved using Kadane's Algorithm.

Approach: Kadane’s Algorithm
-----------------------------
1. Initialize two variables:
   - `res`: stores the overall maximum subarray sum found so far.
   - `maxEnding`: stores the maximum sum of subarray ending at the current index.

2. Iterate through the array starting from the second element.
   At each index `i`:
   - Update `maxEnding` as the maximum of `arr[i]` and `maxEnding + arr[i]`.
   - Update `res` if `maxEnding` is greater than `res`.

3. Return `res` as the result.

Time Complexity: O(n)  
Space Complexity: O(1)

Example:
---------
Input : arr = [2, 3, -8, 7, -1, 2, 3]  
Output: 11  
Explanation: The subarray [7, -1, 2, 3] has the maximum sum 11.
"""

def maxSubarraySum(arr):
    # Initialize result and current max sum with first element
    res = arr[0]
    maxEnding = arr[0]

    for i in range(1, len(arr)):
        # Choose between extending the previous subarray or starting new
        maxEnding = max(maxEnding + arr[i], arr[i])
        res = max(res, maxEnding)

    return res


# --------- Example Usage ---------
if __name__ == "__main__":
    arr = [2, 3, -8, 7, -1, 2, 3]
    print("Maximum Subarray Sum:", maxSubarraySum(arr))  # Output: 11
