"""
Problem: Rotate a Square Matrix by 90 Degrees Clockwise (In-Place)

Description:
-------------
Given an **n x n square matrix**, rotate it **by 90 degrees clockwise** without using any extra space.

Approach:
---------
The rotation can be done in two main steps:
1. **Transpose the matrix**:
   Swap matrix[i][j] with matrix[j][i] for all i < j.
2. **Reverse each row**:
   Reversing each row of the transposed matrix results in a 90-degree clockwise rotation.

Time Complexity: O(n^2)  
    - Every element is visited once during transpose and once during reversal.

Space Complexity: O(1)  
    - The operation is done in-place without using extra space.

Example:
---------
Input:
[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

Output:
[
  [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]
]
"""

def rotate_matrix_inplace(mat):
    n = len(mat)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        mat[i].reverse()


# Example Usage
if __name__ == "__main__":
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rotate_matrix_inplace(mat)

    print("Rotated matrix:")
    for row in mat:
        print(row)
