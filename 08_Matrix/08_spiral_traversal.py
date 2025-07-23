"""
Problem: Spiral Order Traversal of a Matrix

Description:
-------------
Given a 2D matrix, return all elements of the matrix in spiral order 
(clockwise starting from the top-left element).

Approach:
---------
Use four pointers to define the current bounds of the matrix:
- `top`: initially the first row
- `bottom`: initially the last row
- `left`: initially the first column
- `right`: initially the last column

Iteratively:
1. Traverse from `left` to `right` on the top row.
2. Traverse from `top` to `bottom` on the rightmost column.
3. Traverse from `right` to `left` on the bottom row (if still valid).
4. Traverse from `bottom` to `top` on the leftmost column (if still valid).

After each traversal, move the boundary inward.

Time Complexity:
----------------
- O(m * n), where m is the number of rows and n is the number of columns.

Space Complexity:
-----------------
- O(1) extra space (excluding the output list).

Example:
--------
Input:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
"""

def spiral_order_traversal(matrix):
    result = []
    if not matrix:
        return result

    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse from Left to Right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Traverse from Top to Bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # Traverse from Right to Left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # Traverse from Bottom to Top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result


# Example usage
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Spiral order:", spiral_order_traversal(matrix))
