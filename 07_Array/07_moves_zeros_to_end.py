"""
Problem: Move Zeroes to End (In-place)
LeetCode Link: https://leetcode.com/problems/move-zeroes/description/

Description:
------------
Given an integer array `nums`, move all `0`s to the end while maintaining the relative order of the non-zero elements.
This must be done in-place without making a copy of the array.

Approach:
---------
The algorithm uses a two-pointer technique:
1. Pointer `j` tracks the index where the next non-zero element should go.
2. Iterate through the array, placing all non-zero elements at the start (compact the array).
3. After placing all non-zero elements, fill the remaining positions with `0`.

Time Complexity: O(n)
Space Complexity: O(1) (in-place operation)

Example:
--------
Input:  nums = [0, 1, 0, 3, 12]  
Output: [1, 3, 12, 0, 0]
"""

from typing import List

def moveZeroes(nums: List[int]) -> None:
    j = 0  # Index to place the next non-zero element

    # Move all non-zero elements to the front
    for n in nums:
        if n != 0:
            nums[j] = n
            j += 1

    # Fill remaining elements with zero
    for i in range(j, len(nums)):
        nums[i] = 0


# --------- Main Program ---------
if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12, -8]
    moveZeroes(nums)
    print("After moving zeroes:", nums)  # Output: [1, 3, 12, 0, 0]
