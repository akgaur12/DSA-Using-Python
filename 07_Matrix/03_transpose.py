"""
Problem: Transpose of a Matrix

Description:
------------
Given a 2D matrix, return its transpose.
The transpose of a matrix is obtained by swapping its rows with columns.

For a matrix A of size m x n, its transpose AT will be of size n x m,
where AT[j][i] = A[i][j].

Approach:
---------
- Loop through each column index `j` (from 0 to number of columns).
- For each column `j`, create a new row by collecting all `matrix[i][j]` for all rows `i`.
- Append this new row to the result.

Time Complexity: O(n * m)
    Where n = number of rows, m = number of columns.

Space Complexity: O(n * m)
    A new matrix of the same size is created for the transpose.
"""

def transpose(matrix):
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)

    return result


# Example Usage
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    transposed = transpose(matrix)

    print("Original Matrix:")
    for row in matrix:
        print(row)

    print("\nTransposed Matrix:")
    for row in transposed:
        print(row)
