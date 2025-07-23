"""
Program: Merge Sort Algorithm

Description:
------------
Merge Sort is a **divide-and-conquer** sorting algorithm that recursively divides the array 
into halves, sorts each half, and then merges the sorted halves back together.

It is known for its **stable** and **efficient** performance with consistent time complexity 
across best, average, and worst cases.

Working Principle:
------------------
1. Divide: Split the array into two halves until each subarray contains only one element.
2. Conquer: Recursively sort the two halves.
3. Combine: Merge the two sorted halves into a single sorted array.

Number of Passes:
-----------------
- Merge Sort divides the array until subarrays of size 1 are obtained.
- For an array of length `n`, it requires approximately `log₂n` passes (levels of recursion).

Time Complexity:
----------------
- Best Case:    O(n log n)
- Average Case: O(n log n)
- Worst Case:   O(n log n)

Merge Sort is O(n log n) because it performs log n levels of splitting, and each level involves merging n elements.

Space Complexity:
-----------------
- O(n), due to the additional space used for temporary arrays during the merge step.

Stability:
----------
- ✅ Merge Sort is **stable**, i.e., it preserves the relative order of equal elements.

Example:
--------
Input : [5, 1, 4, 2, 8]
Output: [1, 2, 4, 5, 8]
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


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge_sorted_arr(left, right)


# --------- Example Usage ---------
if __name__ == "__main__":
    arr = [5, 1, 4, 2, 8, 1, 8, 9, 10, 3]
    print("Original array:", arr)
    sorted_arr = merge_sort(arr)
    print("Sorted array:  ", sorted_arr)  # Output: [1, 1, 2, 3, 4, 5, 8, 8, 9, 10]
