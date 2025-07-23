"""
Problem: Merge Two Sorted Arrays Without Extra Space
GFG Link: https://www.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1

Description:
-------------
Given two sorted arrays `arr1` and `arr2`, merge them so that the final result is also sorted.
Do not use extra space (i.e., modify the arrays in-place).

Approach: Gap Method (Shell Sort Style)
----------------------------------------
1. Use a gap (initially (n + m) / 2) to compare elements that are far apart.
2. Gradually reduce the gap and perform comparisons/swaps:
   - Compare elements within `arr1`.
   - Compare elements across `arr1` and `arr2`.
   - Compare elements within `arr2`.
3. Stop when the gap reduces to 0.

This approach avoids using extra space and still manages to rearrange both arrays in sorted order.

Time Complexity: O((n + m) log(n + m)) — due to repeated gap passes
Space Complexity: O(1) — in-place

Example:
---------
Input: 
  arr1 = [1, 4, 7, 8, 10]
  arr2 = [2, 3, 9]

Output: 
  arr1 = [1, 2, 3, 4, 7]
  arr2 = [8, 9, 10]
"""


def next_gap(gap: int) -> int:
    if gap <= 1:
        return 0
    return (gap // 2) + (gap % 2)


def merge_in_place(arr1: list, arr2: list) -> None:
    n1, n2 = len(arr1), len(arr2)
    gap = next_gap(n1 + n2)

    while gap > 0:
        # Compare elements in arr1
        i = 0
        while i + gap < n1:
            if arr1[i] > arr1[i + gap]:
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
            i += 1

        # Compare elements in arr1 and arr2
        j = gap - n1 if gap > n1 else 0
        while i < n1 and j < n2:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1

        # Compare elements in arr2
        if j < n2:
            j = 0
            while j + gap < n2:
                if arr2[j] > arr2[j + gap]:
                    arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]
                j += 1

        gap = next_gap(gap)


# Example usage
if __name__ == "__main__":
    arr1 = [1, 4, 7, 8, 10]
    arr2 = [2, 3, 9]

    merge_in_place(arr1, arr2)

    print("Merged arr1:", arr1)  # Output: [1, 2, 3, 4, 7]
    print("Merged arr2:", arr2)  # Output: [8, 9, 10]
