"""
Problem: Row with Maximum Number of 1s in a Row-wise Sorted Binary Matrix

Description:
-------------
Given a binary matrix where each row is **sorted in non-decreasing order** (i.e., all 0s appear before 1s),
the task is to find the index of the row with the maximum number of 1s.

Approach:
---------
- Start from the **top-right corner** of the matrix.
- Move **left** if you encounter a 1 (this means this row has more 1s than the previous max).
- Move **down** if you encounter a 0 (since all rows are sorted, no 1s exist to the left).
- Keep track of the row index as long as you move left.

Time Complexity: O(n + m)  
    - Each row and column is traversed at most once.

Space Complexity: O(1)  
    - No extra space used except variables.

Returns:
--------
- Index (0-based) of the row with the maximum number of 1s.
- Returns -1 if no 1 is present in any row.
"""

def row_with_max_1s(mat):
    n = len(mat)
    m = len(mat[0]) if n > 0 else 0

    max_row_index = -1
    j = m - 1  # Start from top-right

    for i in range(n):
        while j >= 0 and mat[i][j] == 1:
            j -= 1
            max_row_index = i  # Update row index whenever we move left

    return max_row_index


# Example Usage
if __name__ == "__main__":
    mat = [
        [0, 0, 0, 1],
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 0, 0, 0]
    ]

    result = row_with_max_1s(mat)
    print(f"Row index with maximum 1s: {result}")
