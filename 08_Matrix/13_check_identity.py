"""
Problem: Check if a Matrix is an Identity Matrix

Description:
-------------
An **identity matrix** is a special square matrix in which:
- All elements on the main diagonal are 1.
- All other elements are 0.

This function verifies whether the given matrix satisfies the above properties.

Constraints:
-------------
- The input must be a 2D **square** matrix (same number of rows and columns).
- The elements must be integers (either 0 or 1 ideally, though other types won't raise errors).

Approach:
----------
1. First, check if the matrix is square.
2. Then iterate through all elements:
    - If it's a diagonal element (i == j), check if it's 1.
    - Otherwise, check if it's 0.

Time Complexity: O(n²)
    - You must visit every element in the matrix.

Space Complexity: O(1)
    - No additional space is used apart from input.
"""


def is_identity_matrix(matrix):
    n = len(matrix)

    # Check if the matrix is square
    if any(len(row) != n for row in matrix):
        return False

    # Check identity matrix properties
    for i in range(n):
        for j in range(n):
            if i == j:
                if matrix[i][j] != 1:
                    return False
            else:
                if matrix[i][j] != 0:
                    return False

    return True



# Example Usage
if __name__ == "__main__":
    matrix1 = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]

    matrix2 = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]

    print("Matrix 1 is identity:", is_identity_matrix(matrix1))  # Output: True
    print("Matrix 2 is identity:", is_identity_matrix(matrix2))  # Output: False
