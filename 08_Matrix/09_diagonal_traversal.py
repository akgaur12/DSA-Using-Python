"""
Problem: Diagonal Traversal of a Matrix

Description:
-------------
Given a matrix `mat` of dimensions n x m, print the matrix in diagonal order.
The diagonal traversal proceeds by printing each diagonal from top-right to bottom-left.

Example:
---------
Input:
mat = [
    [ 1,  2,  3,  4 ],
    [ 5,  6,  7,  8 ],
    [ 9, 10, 11, 12 ],
    [13, 14, 15, 16],
    [17, 18, 19, 20]
]

Output:
1 2 5 3 6 9 4 7 10 13 8 11 14 17 12 15 18 16 19 20

Approach:
----------
- For a matrix of dimensions n x m, there will be (n + m - 1) diagonals.
- Each diagonal can be identified by the line number (starting from 1 to n + m - 1).
- For each diagonal:
  - Calculate the starting column using `max(0, line - n)`.
  - Calculate the number of elements to be processed in this diagonal.
  - For each element in the diagonal:
    - Row = (min(n, line) - 1) - j
    - Column = startCol + j

Time Complexity: O(n * m)
- Every element is visited exactly once.

Space Complexity: O(n * m)
- For storing the result in a new list.

"""

def diagonalOrder(mat):
    res = []
    n = len(mat)
    m = len(mat[0])

    # Total diagonals: n + m - 1
    for line in range(1, n + m):

        # Calculate the starting column of the current diagonal
        startCol = max(0, line - n)

        # Count of elements in this diagonal
        count = min(line, m - startCol, n)

        # Process elements of this diagonal
        for j in range(count):

            # Calculate row and column indices for each element in the diagonal
            row = min(n, line) - j - 1
            col = startCol + j
            res.append(mat[row][col])

    return res


# Example usage
if __name__ == "__main__":
    mat = [
        [ 1, 2, 3, 4 ],
        [ 5, 6, 7, 8 ],
        [ 9, 10, 11, 12 ],
        [ 13, 14, 15, 16 ],
        [ 17, 18, 19, 20 ]
    ]
    result = diagonalOrder(mat)
    print("Diagonal Order Traversal:", end=" ")
    print(" ".join(map(str, result)))
