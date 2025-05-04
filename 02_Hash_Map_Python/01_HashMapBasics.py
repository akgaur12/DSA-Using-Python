"""
Program to count the **frequency of each element** in a given list.

It demonstrates two different methods:
1. Using standard dictionary check (`in` and assignment)
2. Using `dict.get()` for cleaner code

Example:
--------
Input:  [1, 2, 1, 3, 2, 1]
Output: {1: 3, 2: 2, 3: 1}

Time Complexity:
----------------
Both methods run in O(n), where n is the length of the list.
"""


def frequency_map(arr):
    freq_map = {}

    for i in arr:
        if i in freq_map:
            freq_map[i] += 1
        else:
            freq_map[i] = 1

    return freq_map


def frequency_map2(arr):
    freq_map = {}

    for i in arr:
        freq_map[i] = freq_map.get(i, 0) + 1
        
    return freq_map


# --------- Example Usage ---------
arr = [1, 2, 5, 8, 9, 1, 5, 6, 7, 9, 3, 4, 6, 4, 7, 1, 2, 5, 7]

print("Frequency Count (Method 1):", frequency_map(arr))
print("Frequency Count (Method 2):", frequency_map2(arr))
