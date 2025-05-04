"""
Problem: Unique Number I
--------
Given an unsorted array arr[] of positive integers, where:
- All numbers occur exactly twice **except one** number, which occurs only once.
Your task is to find and return the number that occurs only once.

GFG Problem Link: https://www.geeksforgeeks.org/problems/find-unique-number/1

Example:
--------
Input:  arr = [1, 2, 1, 5, 5]
Output: 2
Explanation: Since 2 occurs once, while other numbers occur twice, 2 is the answer.

Time Complexity:
----------------
- O(n), where n is the length of the array (due to a single pass to build frequency map)

Space Complexity:
-----------------
- O(n), for storing frequencies in a dictionary
"""


def findUnique(arr):
    freq_map = {}

    for num in arr:
        freq_map[num] = freq_map.get(num, 0) + 1

    for num in freq_map:
        if freq_map[num] == 1:
            return num


# --------- Example Usage ---------
arr = [1, 2, 1, 5, 5]
print("Unique Element:", findUnique(arr))
