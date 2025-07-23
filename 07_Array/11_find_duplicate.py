"""
Problem: Find the Duplicate Number
Leetcode Link: https://leetcode.com/problems/find-the-duplicate-number/description/

Description:
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums. Return this repeated number.

Approach 1: Using a Hash Map
Time Complexity: O(n), Space Complexity: O(n)

Approach 2: Floyd's Tortoise and Hare (Cycle Detection)
Time Complexity: O(n), Space Complexity: O(1)

Example 1:
Input: nums = [3, 1, 3, 4, 2]
Output: 3

Example 2:
Input: nums = [3, 3, 3, 3, 3]
Output: 3
"""


from typing import List

def findDuplicate_hash(nums: List[int]) -> int:
    freq_map = {}
    for n in nums:
        freq_map[n] = freq_map.get(n, 0) + 1

    for num in freq_map:
        if freq_map[num] > 1:
            return num


def findDuplicate_floyd(nums: List[int]) -> int:
    # Phase 1: Detect the cycle
    slow = nums[0]
    fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Phase 2: Find the entry point of the cycle (duplicate number)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow



# Test function
if __name__ == "__main__":
    nums1 = [3, 1, 3, 4, 2]
    nums2 = [3, 3, 3, 3, 3]

    print("Using Hash Map:")
    print("Duplicate in nums1:", findDuplicate_hash(nums1))  # Output: 3
    print("Duplicate in nums2:", findDuplicate_hash(nums2))  # Output: 3

    print("\nUsing Floyd's Cycle Detection:")
    print("Duplicate in nums1:", findDuplicate_floyd(nums1))  # Output: 3
    print("Duplicate in nums2:", findDuplicate_floyd(nums2))  # Output: 3
