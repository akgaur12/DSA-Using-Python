"""
Problem: Print Matrix in Row-Major Order

Description:
------------
Given a 2D matrix, the task is to print its elements in row-major order.
In row-major order, all elements of a row are printed before moving to the next row.

Approach:
---------
- Use two nested loops:
    - The outer loop iterates over each row.
    - The inner loop iterates over each column of the current row.
- Print each element followed by a space on the same line.

Time Complexity: O(n * m)
    Where n = number of rows, m = number of columns.

Space Complexity: O(1)
    No extra space is used except loop variables.
"""

def print_row_major(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end=' ')
    print()  # newline after printing the matrix


# Example usage
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Matrix in Row-Major Order:")
    print_row_major(matrix)
