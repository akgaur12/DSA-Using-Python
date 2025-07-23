"""
Program: Counting Sort Algorithm

Description:
------------
Counting Sort is a **non-comparison-based**, integer sorting algorithm that works best when the range
of input elements is not significantly greater than the number of elements. It works by:
1. Counting the number of occurrences of each distinct element.
2. Computing cumulative counts.
3. Placing elements at their correct positions in the output array based on the counts.

This implementation supports arrays with **non-negative and negative integers** by offsetting the values using the minimum value in the array.

Steps:
------
1. Find the minimum and maximum values in the input array.
2. Create a count array of size (max_val - min_val + 1) initialized to 0.
3. Populate the count array with the frequency of each element.
4. Convert the count array to a cumulative count array.
5. Traverse the original array **in order** and place elements in their sorted positions in the output array.
6. Return the sorted output array.

Time Complexity:
----------------
- Best Case: O(n + k)
- Average Case: O(n + k)
- Worst Case: O(n + k)
Where:
- n = number of elements in input array
- k = range of input (max - min + 1)

Space Complexity:
-----------------
- O(n + k) → extra space for the count array and output array

Stability:
----------
✅ Counting Sort is **stable**, meaning it preserves the relative order of equal elements.

Use Case:
---------
- Works well for integers in a small known range.
- Not suitable for floating-point numbers or large ranges with sparse distribution.

Example:
--------
Input : [4, 2, 2, 8, 3, 3, 1]
Output: [1, 2, 2, 3, 3, 4, 8]
"""


def counting_sort(arr):
    # Handle empty array
    if not arr:
        return []

    # Step 1: Find min and max
    max_val = max(arr)
    min_val = min(arr)

    # Step 2: Initialize count array of size (max - min + 1)
    count_arr = [0] * (max_val - min_val + 1)

    # Step 3: Count occurrences of each number
    for num in arr:
        count_arr[num - min_val] += 1

    # Step 4: Cumulative count
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    # Step 5: Build output array (stable sort)
    out_arr = [0] * len(arr)
    for num in reversed(arr):  # reversed to maintain stability
        index = count_arr[num - min_val] - 1
        out_arr[index] = num
        count_arr[num - min_val] -= 1

    return out_arr


# --------- Example Usage ---------
if __name__ == "__main__":
    arr = [4, 2, 2, 8, 3, 3, 1]
    print("Original array:", arr)
    sorted_arr = counting_sort(arr)
    print("Sorted array:", sorted_arr)  # Output: [1, 2, 2, 3, 3, 4, 8]
