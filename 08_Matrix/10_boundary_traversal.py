"""
Problem: Boundary Traversal of a Matrix

Description:
-------------
Given a 2D matrix, print its boundary elements in a clockwise direction.
Boundary elements include the outermost elements of the matrix:
- Top row (left to right)
- Last column (top to bottom)
- Bottom row (right to left)
- First column (bottom to top)

Note: The matrix should have at least one row and one column.

Example:
---------
Input:
mat = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12]
]

Output:
1 2 3 4 8 12 11 10 9 5

Approach:
---------
1. Traverse the top row from left to right.
2. Traverse the last column from second row to last.
3. Traverse the bottom row from second-last column to first.
4. Traverse the first column from second-last row to second row (bottom to top).
   This avoids repeating the corners already visited.

Time Complexity: O(n + m)
- Where n is the number of rows and m is the number of columns.
- Each boundary element is visited exactly once.

Space Complexity: O(1)
- Apart from output storage, no extra space is used.
"""

def boundaryTraversal(mat):
    n = len(mat)
    m = len(mat[0])
    res = []

    # Top row (left to right)
    for j in range(m):
        res.append(mat[0][j])

    # Last column (top to bottom, excluding the first row)
    for i in range(1, n):
        res.append(mat[i][m - 1])

    # Bottom row (right to left, excluding last column)
    if n > 1:
        for j in range(m - 2, -1, -1):
            res.append(mat[n - 1][j])

    # First column (bottom to top, excluding first and last rows)
    if m > 1:
        for i in range(n - 2, 0, -1):
            res.append(mat[i][0])

    return res


# Example usage
if __name__ == "__main__":
    mat = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    result = boundaryTraversal(mat)
    print("Boundary Traversal:", end=" ")
    print(" ".join(map(str, result)))
