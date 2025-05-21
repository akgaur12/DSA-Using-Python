"""
Program: Selection Sort Algorithm

Description:
------------
Selection Sort is a simple comparison-based sorting algorithm. It divides the input list
into two parts: the sorted part at the front and the unsorted part at the back. Initially,
the sorted part is empty and the unsorted part is the entire list.

Working Principle:
------------------
- The algorithm repeatedly selects the smallest (or largest, depending on sorting order) 
  element from the unsorted part of the list.
- It then swaps this minimum element with the first element of the unsorted part.
- This process moves the boundary between the sorted and unsorted parts one element forward.
- The steps are repeated until the entire list is sorted.

Number of Passes:
-----------------
- Selection Sort always requires exactly **n - 1 passes** to sort an array of size n.
- Each pass selects the minimum element from the unsorted portion and places it at the current position.

Time Complexity:
----------------
- Best, Average, and Worst Case: O(n²), because it always scans the unsorted portion to find the minimum element.

Space Complexity:
-----------------
- O(1), since sorting is done in-place without extra space.

Stability:
----------
- Selection sort is **not stable** because it may swap non-adjacent elements.

Example:
--------
Input : [64, 25, 12, 22, 11]
Output: [11, 12, 22, 25, 64]
"""


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Assume the minimum element is at the current position
        min_idx = i
        # Find the minimum element in remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


# --------- Example Usage ---------
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    sorted_arr = selection_sort(arr)
    print("Sorted array:", sorted_arr)  # Output: [11, 12, 22, 25, 64]
