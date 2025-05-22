"""
Program: Insertion Sort Algorithm

Description:
------------
Insertion Sort is a simple comparison-based sorting algorithm that builds the final sorted 
array one element at a time. It is much like sorting playing cards in your hands: we take 
one card at a time and insert it into its correct position relative to the already sorted cards.

Working Principle:
------------------
- Start from the second element (index 1) and compare it with the elements before it.
- Shift elements of the sorted part that are greater than the key to one position ahead.
- Insert the key into the correct position.
- Repeat for all elements until the list is sorted.

Number of Passes:
-----------------
- Insertion Sort requires exactly **(n - 1) passes** to sort an array of size n.
- Each pass inserts one element into its correct position in the sorted portion of the list.

Time Complexity:
----------------
- Best Case: O(n)       → when the array is already sorted
- Average Case: O(n²)
- Worst Case: O(n²)     → when the array is sorted in reverse order

Space Complexity:
-----------------
- O(1), since it sorts the list in-place

Stability:
----------
- Insertion Sort is **stable**, as it maintains the relative order of equal elements.

Example:
--------
Input : [12, 11, 13, 5, 6]
Output: [5, 6, 11, 12, 13]
"""


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1] that are greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # Place key after the element just smaller than it
        arr[j + 1] = key

    return arr


# --------- Example Usage ---------
if __name__ == "__main__":
    sample = [12, 11, 13, 5, 6]
    sorted_arr = insertion_sort(sample)
    print("Sorted array:", sorted_arr)  # Output: [5, 6, 11, 12, 13]
