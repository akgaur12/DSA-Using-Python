"""
Problem: Unique Number II
--------
Given an array `arr[]` containing 2*n + 2 positive integers, where:
- 2*n numbers exist in pairs (i.e., occur exactly twice),
- and 2 numbers occur **only once** and are **distinct**.

Your task is to find the two numbers that occur only once, and return them in **increasing order**.

GFG Problem Link: https://www.geeksforgeeks.org/problems/finding-the-numbers0215/1

Examples:
---------
Input:  arr = [1, 2, 3, 2, 1, 4]
Output: [3, 4]
Explanation: Only 3 and 4 appear once.

Input:  arr = [2, 1, 3, 2]
Output: [1, 3]
Explanation: Only 1 and 3 appear once.

Time Complexity:
----------------
- O(n), where n is the length of the array (for building the frequency map)

Space Complexity:
-----------------
- O(n), for the dictionary storing element counts
"""


def singleNum(arr):
    freq_map = {}
    result = []

    # Count frequency of each element
    for num in arr:
        freq_map[num] = freq_map.get(num, 0) + 1

    # Collect the numbers that occurred only once
    for num in freq_map:
        if freq_map[num] == 1:
            result.append(num)

    # Sort result to maintain increasing order
    if result[0] > result[1]:
        result[0], result[1] = result[1], result[0]

    return result


# --------- Example Usage ---------
arr = [1, 2, 3, 2, 1, 4]
print("Unique Elements:", singleNum(arr))
