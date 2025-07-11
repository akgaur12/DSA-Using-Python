"""
Problem: Search in a Row-wise and Column-wise Sorted Matrix

Description:
-------------
Given a matrix in which:
- Each row is sorted in increasing order from left to right.
- Each column is sorted in increasing order from top to bottom.

The task is to search for a target value in the matrix efficiently.

Constraints:
-------------
- The matrix must not be empty.
- Each row and each column is individually sorted in ascending order.
- The target is an integer.

Approach:
----------
- Start from the **top-right corner** of the matrix.
- At each step:
    - If the current element equals the target, return its position.
    - If the current element is greater than the target, move **left**.
    - If the current element is less than the target, move **down**.

This works because going left reduces values in a row, and going down increases values in a column.

Time Complexity: O(n + m)
    - Worst-case: traverse one full row and one full column.

Space Complexity: O(1)
    - No extra space is used.

"""


def search_sorted_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return -1, -1  # Handle empty matrix

    n = len(matrix)
    m = len(matrix[0])

    row = 0
    col = m - 1  # Start from top-right corner

    while row < n and col >= 0:
        current = matrix[row][col]

        if current == target:
            return row, col  # Target found
        elif current > target:
            col -= 1  # Move left
        else:
            row += 1  # Move down

    return -1, -1  # Target not found



# Example Usage
if __name__ == "__main__":
    mat = [
        [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50]
    ]

    key = 29

    result = search_sorted_matrix(mat, key)
    if result != (-1, -1):
        print(f"Element {key} found at position {result}")
    else:
        print(f"Element {key} not found in matrix.")
