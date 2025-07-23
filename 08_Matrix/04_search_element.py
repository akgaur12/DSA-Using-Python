"""
Problem: Search Element in a Matrix

Description:
------------
Given a 2D matrix and a target value, find the position (row, column)
of the target element. If the element is not found, return -1.

This approach performs a brute-force search by checking every element
in the matrix.

Approach:
---------
- Iterate over each row using index `i`.
- For each row, iterate over each column using index `j`.
- If `matrix[i][j] == target`, return the coordinates (i, j).
- If not found after full traversal, return -1.

Time Complexity: O(n * m)
    - Where n = number of rows, m = number of columns
    - Every element may need to be checked in the worst case.

Space Complexity: O(1)
    - Constant space is used regardless of input size.
"""

def search_matrix(matrix, target):

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == target:
                return (i, j)  # Found target
    return -1  # Target not found


# Example Usage
if __name__ == "__main__":
    matrix = [
        [5, 1, 3],
        [9, 6, 2],
        [7, 4, 8]
    ]

    print(search_matrix(matrix, 6))   # Output: (1, 1)
    print(search_matrix(matrix, 10))  # Output: -1
