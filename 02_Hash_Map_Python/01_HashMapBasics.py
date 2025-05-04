"""
Program to count the **frequency of each element** in a given list using Hash Maps (dictionaries).

Hash Map in Python:
-------------------
- Python's built-in `dict` is a **hash map**, which allows **average O(1)** time complexity for insert, lookup, and update.
- It stores data in key-value pairs using a hashing mechanism.
- Perfect for frequency counting or grouping similar values efficiently.

This script demonstrates:
1. Frequency counting using basic dictionary checks
2. Frequency counting using `dict.get()`
3. Sorting frequency dictionary by:
   a. Key (element)
   b. Value (frequency)

Time Complexity:
----------------
- Frequency counting: O(n)
- Sorting by key or value: O(k log k), where k is the number of unique elements
"""


def frequency_map(arr):
    """Counts frequency using basic dictionary syntax."""
    freq_map = {}
    for i in arr:
        if i in freq_map:
            freq_map[i] += 1
        else:
            freq_map[i] = 1
    return freq_map


def frequency_map2(arr):
    """Counts frequency using dict.get()."""
    freq_map = {}
    for i in arr:
        freq_map[i] = freq_map.get(i, 0) + 1
    return freq_map


def sort_by_key(freq_map):
    """Sorts frequency dictionary by keys (element values)."""
    return dict(sorted(freq_map.items()))


def sort_by_value(freq_map):
    """Sorts frequency dictionary by values (frequencies)."""
    return dict(sorted(freq_map.items(), key=lambda x: x[1]))



# --------- Example Usage ---------
arr = [1, 2, 5, 8, 9, 1, 5, 6, 7, 9, 3, 4, 6, 4, 7, 1, 2, 5, 7]

freq = frequency_map2(arr)
print("Frequency Map:", freq)
print("Sorted by Key:", sort_by_key(freq))
print("Sorted by Value:", sort_by_value(freq))
