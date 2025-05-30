"""
Problem: Remove Duplicates from Sorted Array
LeetCode Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Description:
------------
Given a sorted array `nums`, remove duplicates **in-place** such that each element appears only once.
Return the number of unique elements, `k`, and modify the input array such that the first `k` elements are the unique elements.

Constraints:
- Do not allocate extra space for another array.
- Modify the input array in-place with O(1) extra memory.
- The order of unique elements should be maintained.

Example:
--------
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5
Modified Array: [0, 1, 2, 3, 4, _, _, _, _, _]
"""

def removeDuplicate(nums):
    if not nums:
        return 0  # Empty list, no unique elements

    # Initialize the slow-runner pointer `i`
    i = 0

    # Fast-runner `j` starts from 1
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    # `i + 1` is the count of unique elements
    return i + 1


# --------- Main Program ---------
if __name__ == "__main__":
    arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = removeDuplicate(arr)
    print("Number of unique elements:", k)
    print("Modified array:", arr[:k])  # Output: [0, 1, 2, 3, 4]
