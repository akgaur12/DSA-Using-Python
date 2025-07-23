"""
Problem: Set Matrix Zeroes

Description:
-------------
Given an `n x m` matrix, if any cell contains `0`, set its entire row and column to 0.
The operation must be done **in-place**, i.e., without using extra space proportional to matrix size.

Constraints:
-------------
- Matrix can contain any integers.
- Must be modified in-place.
- Extra space is allowed only in constant amount.

Approach:
----------
1. **Initial Scan**:
    - Check if the first row and/or first column has any zeros, to remember whether they need to be zeroed later.
2. **Use First Row & First Column as Markers**:
    - Traverse the matrix starting from index (1, 1).
    - For any zero found, mark its row and column by setting `mat[i][0] = 0` and `mat[0][j] = 0`.
3. **Second Pass**:
    - Based on the markers (first row and column), set the required cells to 0.
4. **Final Step**:
    - Zero out the first row and column separately, if required.

Time Complexity: O(n × m)  
Space Complexity: O(1) – Only a few boolean flags and index variables are used.
"""


def set_matrix_zeroes(mat):
    if not mat or not mat[0]:
        return

    n = len(mat)
    m = len(mat[0])

    # Flags to determine if first row or column needs to be zeroed
    first_row_zero = any(mat[0][j] == 0 for j in range(m))
    first_col_zero = any(mat[i][0] == 0 for i in range(n))

    # Step 1: Mark zeroes in first row/column for rest of matrix
    for i in range(1, n):
        for j in range(1, m):
            if mat[i][j] == 0:
                mat[i][0] = 0
                mat[0][j] = 0

    # Step 2: Use markers to set zeroes
    for i in range(1, n):
        for j in range(1, m):
            if mat[i][0] == 0 or mat[0][j] == 0:
                mat[i][j] = 0

    # Step 3: Zero out the first row if needed
    if first_row_zero:
        for j in range(m):
            mat[0][j] = 0

    # Step 4: Zero out the first column if needed
    if first_col_zero:
        for i in range(n):
            mat[i][0] = 0


# Example Usage
if __name__ == "__main__":
    mat = [
        [1, 2, 3, 2],
        [4, 0, 6, 0],
        [7, 8, 9, 1]
    ]

    set_matrix_zeroes(mat)

    for row in mat:
        print(row)
