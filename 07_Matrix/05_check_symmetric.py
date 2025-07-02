"""
Problem: Check if a Matrix is Symmetric

Description:
-------------
A matrix is said to be **symmetric** if it is equal to its transpose.
This means that for all valid indices `i` and `j`:
    matrix[i][j] == matrix[j][i]

This function first checks whether the matrix is square (i.e., same number of rows and columns),
and then checks the symmetry property by comparing each element with its transposed counterpart.

Approach:
---------
1. Ensure the matrix is square.
2. Traverse only the upper triangle (excluding diagonal) of the matrix.
3. Compare each element at (i, j) with its counterpart at (j, i).
4. If all such pairs match, the matrix is symmetric.

Time Complexity: O(n²), where n is the number of rows (or columns)
Space Complexity: O(1), constant extra space used
"""

def is_symmetric(matrix):
    n = len(matrix)

    # Check if matrix is square
    if any(len(row) != n for row in matrix):
        return False

    # Check symmetry (only upper triangle to avoid redundant checks)
    for i in range(n):
        for j in range(i, n):
            if matrix[i][j] != matrix[j][i]:
                return False

    return True


# Example matrices
if __name__ == "__main__":
    matrix1 = [
        [1, 2, 3],
        [2, 5, 6],
        [3, 6, 9]
    ]

    matrix2 = [
        [1, 0, 1],
        [0, 1, 0],
        [2, 0, 1]
    ]

    print("Matrix 1 is symmetric:", is_symmetric(matrix1))  # Output: True
    print("Matrix 2 is symmetric:", is_symmetric(matrix2))  # Output: False
