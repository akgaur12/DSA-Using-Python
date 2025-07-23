"""
Problem: Given an array, rotate it to the right by `k` steps, where `k` is non-negative.
LeetCode Link: https://leetcode.com/problems/rotate-array/description/

Description:
------------
You are given an array `nums` and an integer `k`. Your task is to rotate the array to the right by `k` steps.
This operation should be done **in-place**, meaning that no extra space should be used (O(1) space complexity).

Approach:
---------
The solution uses the **three-step reverse algorithm**, which allows in-place rotation:
1. Reverse the entire array.
2. Reverse the first `k` elements.
3. Reverse the remaining `n-k` elements.

Example:
--------
Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3  
Output: [5, 6, 7, 1, 2, 3, 4]

Explanation:
After rotating right by 3 steps, the array becomes [5, 6, 7, 1, 2, 3, 4].
"""

def right_rotate_k(nums, k):
    if not nums:
        return

    k %= len(nums)  # Handle cases where k > len(nums)

    def reverse(start: int, end: int) -> None:
        """Helper function to reverse elements in-place from start to end."""
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Step 1: Reverse the entire array
    reverse(0, len(nums) - 1)
    # Step 2: Reverse the first k elements
    reverse(0, k - 1)
    # Step 3: Reverse the remaining n - k elements
    reverse(k, len(nums) - 1)


# --------- Main Program ---------
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    right_rotate_k(nums, k)
    print("Rotated array:", nums)  # Output: [5, 6, 7, 1, 2, 3, 4]
