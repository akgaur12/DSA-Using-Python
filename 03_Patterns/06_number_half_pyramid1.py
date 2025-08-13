"""
Pattern Printing: Number-Based Triangular Patterns

Description:
------------
This module prints four different triangular number patterns:

Pattern 1 (Left-Aligned Increasing Triangle):
---------------------------------------------
1
1 2
1 2 3

Pattern 2 (Right-Aligned Increasing Triangle):
---------------------------------------------
    1
  1 2
1 2 3

Pattern 3 (Left-Aligned Decreasing Triangle):
---------------------------------------------
1 2 3
1 2
1

Pattern 4 (Right-Aligned Decreasing Triangle):
---------------------------------------------
1 2 3
  1 2
    1

Each function prints its pattern directly to the console.

Time Complexity: O(n²) for each pattern
Space Complexity: O(1)
"""


# Left-Aligned Increasing Triangle
def pattern1(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
    print()


# Right-Aligned Increasing Triangle
def pattern2(n):
    for i in range(1, n+1):
        print("  " * (n - i), end="")  # Leading spaces
        for j in range(1, i+1):
            print(j, end=" ")
        print()
    print()


# Left-Aligned Decreasing Triangle
def pattern3(n):
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
    print()


# Right-Aligned Decreasing Triangle
def pattern4(n):
    for i in range(n):
        print("  " * i, end="")  # Increasing spaces
        for j in range(1, n - i + 1):
            print(j, end=" ")
        print()
    print()


# Example Usage
if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    pattern1(n)
    pattern2(n)
    pattern3(n)
    pattern4(n)
