"""
Program: Quick Sort Algorithm

Description:
------------
Quick Sort is a highly efficient **divide-and-conquer** sorting algorithm. It works by selecting
a **pivot** element and partitioning the array such that:
- All elements less than or equal to the pivot go to the left,
- All elements greater than the pivot go to the right.

Then, the process is recursively applied to the subarrays on the left and right of the pivot.

Partitioning Logic:
-------------------
- This implementation uses the **Lomuto partition scheme** (variant) where the pivot is the
  first element (`arr[Low]`).
- Two pointers `i` (starting from Low) and `j` (starting from High) are used to scan the array.
- Elements are swapped to ensure correct placement relative to the pivot.
- Finally, the pivot is placed in its correct sorted position.

Time Complexity:
----------------
- Best Case:    O(n log n)  → when the pivot divides the array into equal halves.
- Average Case: O(n log n)
- Worst Case:   O(n²)       → when the pivot is the smallest/largest element each time (e.g., already sorted array).

Space Complexity:
-----------------
- O(log n) for recursion stack (in-place sort, no extra array used).

Stability:
----------
- ❌ Quick Sort is **not stable**, i.e., it may change the relative order of equal elements.

Number of Passes:
-----------------
- Quick Sort can require up to `log₂n` levels of recursion (on average), and each level processes all `n` elements.

Example:
--------
Input : [4, 1, 7, 6, 3, 2, 8]  
Output: [1, 2, 3, 4, 6, 7, 8]
"""


def partition(arr, Low, High):
    """
    Partition the array around a pivot such that:
    - Elements <= pivot are to its left
    - Elements > pivot are to its right

    Parameters:
        arr (list): The array to be partitioned.
        Low (int): The starting index of the subarray.
        High (int): The ending index of the subarray.

    Returns:
        int: The final position (index) of the pivot.
    """
    i, j = Low, High
    pivot = arr[Low]

    while i < j:
        # Move i to the right while arr[i] <= pivot
        while i <= High - 1 and arr[i] <= pivot:
            i += 1

        # Move j to the left while arr[j] >= pivot
        while j >= Low + 1 and arr[j] >= pivot:
            j -= 1

        # Swap if needed
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot at the correct position
    arr[Low], arr[j] = arr[j], arr[Low]
    return j


def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot)       # Sort left partition
        quick_sort(arr, pivot + 1, high)  # Sort right partition


# --------- Example Usage ---------
if __name__ == "__main__":
    arr = [4, 1, 7, 6, 3, 2, 8]
    print("Original array:", arr)
    quick_sort(arr, 0, len(arr) - 1)
    print("Sorted array:  ", arr)  # Output: [1, 2, 3, 4, 6, 7, 8]
