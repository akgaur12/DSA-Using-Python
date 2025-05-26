"""
Program: Radix Sort Algorithm (with Counting Sort as a subroutine)

Description:
------------
Radix Sort is a **non-comparison-based** sorting algorithm that sorts integers by processing individual digits.
It works by sorting the numbers digit-by-digit starting from the **least significant digit (LSD)** to the **most significant digit (MSD)**,
using a **stable** sorting algorithm — typically **Counting Sort** — at each digit position.

Steps:
------
1. Find the maximum value in the input to determine the number of digits.
2. Use a stable sort (here, Counting Sort) to sort the input array by each digit (starting from units, tens, hundreds...).
3. Repeat until all digit places are processed.

Functions:
----------
1. `counting_sort_exp(arr, exp)`: Performs Counting Sort on the digit at place value `exp`.
2. `radix_sort(arr)`: Driver function to perform Radix Sort using counting_sort_exp.

Time Complexity:
----------------
- Best Case: O(n * k)
- Average Case: O(n * k)
- Worst Case: O(n * k)
Where:
- n = number of elements
- k = number of digits in the maximum number (≈ log₁₀(max_val))

Space Complexity:
-----------------
- O(n + k), due to output and count arrays.

Stability:
----------
✅ **Radix Sort is stable** when the underlying digit sort (Counting Sort) is stable.
This is essential to ensure the correctness of the digit-wise accumulation.

Use Case:
---------
- Efficient for sorting numbers with limited digit length.
- Not suitable for floating-point numbers or negative values unless adapted.

Example:
--------
Input : [170, 45, 75, 90, 802, 24, 2, 66]
Output: [2, 24, 45, 66, 75, 90, 170, 802]
"""


def counting_sort_exp(arr, exp):
    n = len(arr)
    output = [0] * n          # Output array for sorted elements
    count = [0] * 10          # Count array for digits (0-9)

    # Count occurrences of digits at current place value
    for i in arr:
        index = (i // exp) % 10
        count[index] += 1

    # Cumulative count to determine positions
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array (traverse input array in reverse for stability)
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy output back into original array
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    if not arr:
        return

    max_val = max(arr)
    exp = 1  # Starting with least significant digit
    while max_val // exp > 0:
        counting_sort_exp(arr, exp)
        exp *= 10


# --------- Example Usage ---------
if __name__ == "__main__":
    lst = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Original list:", lst)
    radix_sort(lst)
    print("Sorted list:  ", lst)  # Output: [2, 24, 45, 66, 75, 90, 170, 802]
