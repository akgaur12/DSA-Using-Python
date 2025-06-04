"""
Problem: Missing Number
LeetCode Link: https://leetcode.com/problems/missing-number/

Description:
Given an array `nums` containing `n` distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

Example:
Input: nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
Output: 8

There are three popular approaches to solve this problem:
1. Using a Hash Map (O(n) time, O(n) space)
2. Using the Sum Formula (O(n) time, O(1) space)
3. Using XOR Property (O(n) time, O(1) space)
"""

from typing import List

# -------------------------
# Approach 1: Using Hash Map
# -------------------------
def missingNumber_hash(nums: List[int]) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Uses a hash map to track all elements. Then iterates from 0 to n
    to find the missing number.
    """
    freq_map = {}
    for num in nums:
        freq_map[num] = 1

    for num in range(len(nums) + 1):
        if num not in freq_map:
            return num


# -------------------------------
# Approach 2: Using Sum Formula
# -------------------------------
def missingNumber_sum(nums: List[int]) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Computes the expected sum of 0 to n using formula and subtracts
    the actual sum of the array to find the missing number.
    """
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


# -------------------------
# Approach 3: Using XOR
# -------------------------
def missingNumber_xor(nums: List[int]) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    XOR all the indices and the array elements together.
    All paired numbers cancel out and leave the missing number.
    """
    n = len(nums)
    missing = n
    for i in range(n):
        missing ^= i ^ nums[i]
    return missing



# Example usage
if __name__ == "__main__":
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print("Missing (Hash Map):", missingNumber_hash(nums))
    print("Missing (Sum Formula):", missingNumber_sum(nums))
    print("Missing (XOR):", missingNumber_xor(nums))
