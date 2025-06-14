"""
Problem: Kth Max Min

Description:
-------------
Given an array of integers and an integer k, find the kth **maximum** and kth **minimum** elements in the array.

Constraints:
-------------
- 1 ≤ k ≤ len(arr)
- The array may contain duplicate or unique values.

Approach 1: Sorting
-------------------
1. Sort the array in ascending order.
2. The kth minimum is at index `k - 1`.
3. The kth maximum is at index `-k`.

Time Complexity: O(n log n), due to sorting.
Space Complexity: O(1), if sorting is done in-place.

Approach 2: Heap (Min-Heap & Max-Heap)
--------------------------------------
1. Use a **Min-Heap** to find the kth minimum.
   - Build a heap from the array and pop `k-1` elements.
   - The kth popped element is the kth minimum.

2. Use a **Max-Heap** to find the kth maximum.
   - Convert the array to negative values and use `heapq` (Python's min-heap).
   - Pop `k-1` elements and return the negated value of the kth.

Time Complexity: O(n + k log n), due to heap creation and popping.
Space Complexity: O(n), for storing heaps.

Example:
---------
Input: arr = [7, 10, 4, 3, 20, 15], k = 3
Output:
    3rd Minimum: 7
    3rd Maximum: 10
"""

import heapq

def kth_max_min(arr, k):
    if k < 1 or k > len(arr):
        return None, None

    arr.sort()
    kth_min = arr[k - 1]
    kth_max = arr[-k]
    return kth_min, kth_max


def kth_max_min_heap(arr, k):
    if k < 1 or k > len(arr):
        return None, None

    # Kth Minimum using Min-Heap
    min_heap = arr[:]
    heapq.heapify(min_heap)
    for _ in range(k - 1):
        heapq.heappop(min_heap)
    kth_min = heapq.heappop(min_heap)

    # Kth Maximum using Max-Heap (by negating values)
    max_heap = [-x for x in arr]
    heapq.heapify(max_heap)
    for _ in range(k - 1):
        heapq.heappop(max_heap)
    kth_max = -heapq.heappop(max_heap)

    return kth_min, kth_max


# Example usage
if __name__ == "__main__":
    arr = [7, 10, 4, 3, 20, 15]
    k = 3

    print("Using Sorting:")
    min_val, max_val = kth_max_min(arr[:], k)
    print(f"{k}th Minimum: {min_val}")
    print(f"{k}th Maximum: {max_val}")

    print("\nUsing Heap:")
    min_val, max_val = kth_max_min_heap(arr, k)
    print(f"{k}th Minimum: {min_val}")
    print(f"{k}th Maximum: {max_val}")
