"""
Problem: Single Number (Bit Manipulation)
LeetCode Link: https://leetcode.com/problems/single-number/description/

Description:
------------
Given an array of integers where every element appears twice except one,
find the element that appears only once.

Approach:
- Use XOR to cancel out duplicates.
- Since a ^ a = 0 and a ^ 0 = a, only the unique number remains.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def single_number(nums: list[int]) -> int:
    """Find the single number using XOR."""
    result = 0
    for num in nums:
        result ^= num  # cancel out duplicates
    return result


# --------------------------
# Example Usage & Testing
# --------------------------
if __name__ == "__main__":
    test_cases = [
        [2, 2, 1],
        [4, 1, 2, 1, 2],
        [1],
        [7, 3, 5, 3, 7]
    ]

    for nums in test_cases:
        print(f"nums = {nums} -> Single Number = {single_number(nums)}")
