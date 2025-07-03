"""
Problem: Sum of Matrix Elements

Description:
-------------
This function calculates the **sum of all elements** in a 2D matrix (list of lists).

Approach:
---------
1. Traverse each row of the matrix.
2. For each row, iterate through all elements and keep adding to a running total.
3. Return the final sum.

Time Complexity: O(n × m), where n is the number of rows and m is the number of columns.
Space Complexity: O(1), since we use only a constant amount of space.
"""

def sum_matrix(matrix):

    total = 0
    for row in matrix:
        for val in row:
            total += val
    return total


# Example usage
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Sum of matrix elements:", sum_matrix(matrix))  # Output: 45
