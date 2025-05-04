"""
Problem: Unique Number III
--------
Given an array `arr[]` of integers where every element appears **thrice** except for one, which appears **once**.
Your task is to find and return the element that appears only once.

GFG Problem Link: https://www.geeksforgeeks.org/problems/find-element-occuring-once-when-all-other-are-present-thrice/1

Examples:
---------
Input:  arr = [1, 10, 1, 1]
Output: 10
Explanation: 10 occurs once, all others (1) occur three times.

Input:  arr = [3, 2, 1, 34, 34, 1, 2, 34, 2, 1]
Output: 3
Explanation: Every element except 3 appears three times.

Time Complexity:
----------------
- O(n), where n is the length of the array.

Space Complexity:
-----------------
- O(n), for storing frequencies in a dictionary.
"""


def getSingle(arr):
    freq_map = {}

    # Count frequency of each element
    for num in arr:
        freq_map[num] = freq_map.get(num, 0) + 1

    # Find the element with frequency 1
    for num in freq_map:
        if freq_map[num] == 1:
            return num



# --------- Example Usage ---------
arr = [3, 2, 1, 34, 34, 1, 2, 34, 2, 1]
print("Single Occurrence Element:", getSingle(arr))
