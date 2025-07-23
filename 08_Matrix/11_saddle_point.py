"""
Problem: Saddle Point in a Matrix

Description:
-------------
A saddle point in a matrix is an element that is:
- The **minimum** element in its row, and
- The **maximum** element in its column.

In other words, it "sits" lower than all other elements in its row,
and "rises" above all other elements in its column.

This function searches for such a saddle point in the given matrix
and prints it if found.

Example:
---------
Input:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Output:
Saddle point found: 7 at position (2, 0)

Time Complexity: O(n * m)
- For each row, we find the minimum (O(m)), and then verify it's max in its column (O(n)).
- For an n x m matrix, total complexity is O(n * m).

Space Complexity: O(1)
- No extra space is used except a few variables.
"""

def findSaddlePoint(matrix):
    n = len(matrix)       # Number of rows
    m = len(matrix[0])    # Number of columns

    # Traverse each row to find a saddle point
    for i in range(n):

        # Step 1: Find the minimum element in the current row
        row_min = matrix[i][0]
        col_index = 0  # Column index of row minimum

        for j in range(1, m):
            if matrix[i][j] < row_min:
                row_min = matrix[i][j]
                col_index = j

        # Step 2: Check if this row minimum is the maximum in its column
        is_saddle_point = True
        for k in range(n):
            if matrix[k][col_index] > row_min:
                is_saddle_point = False
                break

        # If saddle point is found
        if is_saddle_point:
            print(f"Saddle point found: {row_min} at position ({i}, {col_index})")
            return

    # If no saddle point found
    print("No saddle point found.")


# Example Usage
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    findSaddlePoint(matrix)
