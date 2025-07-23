"""
Problem: Print Matrix in Column-Major Order

Description:
------------
Given a 2D matrix, print its elements in column-major order.
In column-major order, all elements of a column are printed before moving to the next column.

Approach:
---------
- Use two nested loops:
    - The outer loop iterates over columns.
    - The inner loop iterates over rows for the current column.
- Print each element followed by a space on the same line.

Time Complexity: O(n * m)
    Where n = number of rows, m = number of columns.

Space Complexity: O(1)
    No extra space is used except loop variables.
"""

def print_column_major(matrix):
    if not matrix:
        return

    rows = len(matrix)
    cols = len(matrix[0])

    for j in range(cols):       # Traverse column-wise
        for i in range(rows):   # Then row-wise inside
            print(matrix[i][j], end=' ')
    print()  # Newline after printing all elements


# Example usage
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Matrix in Column-Major Order:")
    print_column_major(matrix)
