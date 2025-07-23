"""
Problem: Subarray with Zero Sum
GFG Link: https://www.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1

Description:
-------------
Given an array of integers, determine whether there exists a **subarray** (contiguous elements)
whose **sum is equal to zero**.

Return `True` if such a subarray exists, otherwise return `False`.

Example:
---------
Input: arr = [4, 2, -3, 1, 6]
Output: True
Explanation: Subarray [2, -3, 1] has a sum of 0.

Input: arr = [1, 2, 3]
Output: False

Approach 1: Brute Force
------------------------
1. For every index `i`, calculate the sum of the subarray starting at `i` and ending at each index `j ≥ i`.
2. If any such subarray has sum 0, return `True`.

Time Complexity: O(N^2)
Space Complexity: O(1)

Approach 2: Prefix Sum with Hashing
------------------------------------
1. Traverse the array and maintain a running sum (prefix sum).
2. If the prefix sum is 0 or the same prefix sum occurs again, it means a subarray with zero sum exists.

Why it works:
- If the same prefix sum is seen twice, the elements between those two indices sum to zero.

Time Complexity: O(N)
Space Complexity: O(N)
"""

# -------------------- Approach 1: Brute Force -------------------- 
def subArrayExists_brute_force(arr, n):
    for i in range(n):
        curr_sum = arr[i]
        if curr_sum == 0:
            return True
        for j in range(i + 1, n):
            curr_sum += arr[j]
            if curr_sum == 0:
                return True
    return False


# -------------------- Approach 2: Prefix Sum with Hashing -------------------- 
def subArrayExists_prefix_sum(arr, n):
    prefix_sum = 0
    seen_sums = set()

    for i in range(n):
        prefix_sum += arr[i]

        # Check if sum is 0 or already exists in set
        if prefix_sum == 0 or prefix_sum in seen_sums:
            return True
        seen_sums.add(prefix_sum)

    return False


# -------------------- Example Usage -------------------- 
if __name__ == "__main__":
    arr1 = [4, 2, -3, 1, 6]
    arr2 = [1, 2, 3]

    print("Brute Force:", subArrayExists_brute_force(arr1, len(arr1)))       # Output: True
    print("Optimized:", subArrayExists_prefix_sum(arr1, len(arr1)))          # Output: True

    print("Brute Force:", subArrayExists_brute_force(arr2, len(arr2)))       # Output: False
    print("Optimized:", subArrayExists_prefix_sum(arr2, len(arr2)))          # Output: False
