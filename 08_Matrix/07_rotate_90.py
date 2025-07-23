"""
Problem: Rotate Matrix 90 Degrees

Description:
-------------
Given an `n x n` 2D matrix, rotate the matrix in-place by 90 degrees:
- `clockwise` rotation: top becomes right, right becomes bottom, etc.
- `anti-clockwise` rotation: top becomes left, left becomes bottom, etc.

Approach:
---------
Both approaches follow two common steps:
1. **Transpose the matrix**: swap matrix[i][j] with matrix[j][i].
2. Then either:
    - For clockwise: reverse each row.
    - For anti-clockwise: reverse each column.

Time Complexity: O(n²)
Space Complexity: O(1) – in-place rotation without extra matrix.
"""

def rotate_matrix_90_clockwise(matrix):
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()

    return matrix


def rotate_matrix_90_anticlockwise(matrix):
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each column
    for j in range(n):
        for i in range(n // 2):
            matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]

    return matrix


# Example usage
if __name__ == "__main__":
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Original:")
    for row in mat:
        print(row)

    print("\nClockwise 90°:")
    rotated_cw = rotate_matrix_90_clockwise([row[:] for row in mat])  # deep copy
    for row in rotated_cw:
        print(row)

    print("\nAnti-Clockwise 90°:")
    rotated_acw = rotate_matrix_90_anticlockwise([row[:] for row in mat])  # deep copy
    for row in rotated_acw:
        print(row)
