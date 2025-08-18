"""
Function: binary_triangle(n)

Description:
------------
Prints a triangle of 1s and 0s in a binary pattern with `n` rows.
The pattern alternates between 1 and 0 such that:
- Element at position (i, j) is (i + j) % 2.

Example:
--------
>>> binary_triangle(5)
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1

Time Complexity: O(n^2)
    - Loops through each element in the triangle, total elements = n(n+1)/2.
    
Space Complexity: O(1)
    - No additional space used aside from loop variables.
"""


def binary_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print((i + j) % 2, end=" ")
        print()


# Example Usage
if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    binary_triangle(n)
