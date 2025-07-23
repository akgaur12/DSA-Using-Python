"""
Program: Bubble Sort Algorithm

Description:
------------
Bubble Sort is a simple comparison-based sorting algorithm. It repeatedly steps through 
the list, compares adjacent elements, and swaps them if they are in the wrong order. 
This process continues until the list is sorted.

Working Principle:
------------------
- The algorithm works by "bubbling up" the largest unsorted element to its correct position 
  at the end of the list during each iteration.
- In each pass through the list, the next-largest value is placed into its final position.
- The algorithm continues to iterate through the list until no swaps are made, 
  which means the list is sorted.

Optimized Version:
------------------
- This implementation includes an optimization: if no swaps are made in a pass, 
  the algorithm terminates early (i.e., the list is already sorted).

Number of Passes:
-----------------
- Bubble Sort requires **at most (n - 1) passes** to sort an array of size n in the worst case.
- After each pass, the largest unsorted element moves to its correct position.
- In the best case (when the array is already sorted), only **1 pass** is needed due to the optimization that stops the algorithm early if no swaps are made.

Time Complexity:
----------------
- Best Case: O(n)       → when the list is already sorted (no swaps needed)
- Average Case: O(n²)
- Worst Case: O(n²)

Space Complexity:
-----------------
- O(1), because the sorting is done in-place.

Stable Sort:
------------
Yes, bubble sort maintains the relative order of equal elements.

Example:
--------
Input : [5, 1, 4, 2, 8]
Output: [1, 2, 4, 5, 8]
"""


def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n):
        swapped = False
        # Traverse the unsorted part of the list
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap adjacent elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps occurred, the array is already sorted
        if not swapped:
            break
    return arr


# --------- Example Usage ---------
if __name__ == "__main__":
    sample = [5, 1, 4, 2, 8]
    sorted_arr = bubble_sort(sample)
    print("Sorted array:", sorted_arr)  # Output: [1, 2, 4, 5, 8]
