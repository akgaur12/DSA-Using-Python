"""
Problem: Merge Two Sorted Arrays (Using Extra Space)

Description:
Given two sorted arrays, merge them into a single sorted array using extra space.
This is the classic merge step used in Merge Sort.

Example:
Input:
    left_arr = [1, 3, 5]
    right_arr = [2, 4, 6]
Output:
    [1, 2, 3, 4, 5, 6]

Time Complexity: O(n + m), where n and m are the lengths of the two arrays.
Space Complexity: O(n + m), for storing the merged result.
"""

def merge_sorted_arr(left_arr, right_arr):
    n, m = len(left_arr), len(right_arr)
    i, j = 0, 0
    arr = []

    # Merge the arrays while comparing elements
    while i < n and j < m:
        if left_arr[i] <= right_arr[j]:
            arr.append(left_arr[i])
            i += 1
        else:
            arr.append(right_arr[j])
            j += 1

    # Append remaining elements (if any)
    while i < n:
        arr.append(left_arr[i])
        i += 1

    while j < m:
        arr.append(right_arr[j])
        j += 1

    return arr


if __name__ == "__main__":
    left_arr = [1, 3, 5, 7]
    right_arr = [2, 4, 6, 8]
    result = merge_sorted_arr(left_arr, right_arr)
    print("Merged Sorted Array:", result)
