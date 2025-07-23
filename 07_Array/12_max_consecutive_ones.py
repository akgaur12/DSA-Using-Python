"""
Problem: Max Consecutive Ones
Leetcode Link: https://leetcode.com/problems/max-consecutive-ones/description/

Description:
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example:
Input: nums = [1,1,0,1,1,1]
Output: 3
"""

from typing import List

def max_consecutive_ones(nums: List[int]) -> int:
    count = 0          # Counter for current streak of 1s
    max_count = 0      # Stores the maximum streak found

    for num in nums:
        if num == 1:
            count += 1
        else:
            count = 0  # Reset the current count if 0 is encountered
        
        max_count = max(max_count, count)

    return max_count


if __name__ == "__main__":
    arr = [1, 1, 0, 1, 1, 1]
    print("Maximum consecutive 1s:", max_consecutive_ones(arr))
