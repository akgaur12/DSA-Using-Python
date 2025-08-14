"""
Pattern Printing: Number-Based Pyramids (Same-Number Triangles)

Description:
------------
This module prints four different triangular patterns using repeated numbers:

Pattern 1 (Left-Aligned Increasing Triangle):
---------------------------------------------
1
2 2
3 3 3
4 4 4 4

Pattern 2 (Right-Aligned Increasing Triangle):
---------------------------------------------
      1
    2 2
  3 3 3
4 4 4 4

Pattern 3 (Right-Aligned Decreasing Triangle):
---------------------------------------------
4 4 4 4
  3 3 3
    2 2
      1

Pattern 4 (Left-Aligned Decreasing Triangle):
---------------------------------------------
4 4 4 4
3 3 3
2 2
1

Each function prints its pattern directly to the console.

Time Complexity: O(n²) for each pattern
Space Complexity: O(1)
"""


# Left-Aligned Increasing Triangle
def pattern1(n):
    for i in range(1, n+1):
        print((str(i) + " ") * i)
    print()


# Right-Aligned Increasing Triangle
def pattern2(n):
    for i in range(1, n+1):
        print("  " * (n - i) + (str(i) + " ") * i)
    print()


#  Right-Aligned Decreasing Triangle
def pattern3(n):
    for i in range(n, 0, -1):
        print("  " * (n - i) + (str(i) + " ") * i)
    print()


# Left-Aligned Decreasing Triangle
def pattern4(n):
    for i in range(n, 0, -1):
        print((str(i) + " ") * i)
    print()


# Example Usage
if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    print("Pattern 1:")
    pattern1(n)
    print("Pattern 2:")
    pattern2(n)
    print("Pattern 3:")
    pattern3(n)
    print("Pattern 4:")
    pattern4(n)
