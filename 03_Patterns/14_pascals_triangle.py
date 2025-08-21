"""
Pascal's Triangle - Two Approaches (Factorial-based & Iterative)

Description:
------------
This module provides two methods to print Pascal's Triangle:

1. `pascals_triangle()`:
   Uses the mathematical formula for combinations (nCr) and factorial calculation.
   nCr = n! / (r! * (n - r)!)

2. `pascal_triangle_iterative()`:
   Efficiently generates Pascal's Triangle row-by-row using previously computed rows (no factorials).

Each function prints Pascal's Triangle with formatted alignment.

Time Complexity:
----------------
- pascals_triangle: O(n² * n) due to factorial computation inside combination
- pascal_triangle_iterative: O(n²)

Space Complexity:
-----------------
- Both approaches use O(n) extra space for row storage or recursion stack.

Example Output (for n = 5):
          1
        1   1
      1   2   1
    1   3   3   1
  1   4   6   4   1
"""

def factorial(n):
    """Calculates the factorial of a number n."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def combination(n, r):
    """ Calculates nCr = n! / (r! * (n - r)!)"""
    return factorial(n) // (factorial(r) * factorial(n - r))


def pascals_triangle(rows):
    """Prints Pascal’s Triangle using the factorial-based nCr formula."""
    for i in range(rows):
        print("  " * (rows - i - 1), end="")  # Center alignment
        for j in range(i + 1):
            print(combination(i, j), end="   ")
        print()
    print()


def pascal_triangle_iterative(n):
    """Prints Pascal’s Triangle using iterative row-by-row generation."""
    row = [1]
    for i in range(n):
        print("  " * (n - i - 1), end="")
        for num in row:
            print(num, end="   ")
        print()
        # Generate next row
        new_row = [1]
        for j in range(1, len(row)):
            new_row.append(row[j - 1] + row[j])
        new_row.append(1)
        row = new_row


# Example usage
if __name__ == "__main__":
    rows = int(input("Enter number of rows for Pascal’s Triangle: "))
    print("Pascal’s Triangle using nCr formula (Factorial-based):")
    pascals_triangle(rows)
    print("Pascal’s Triangle using Iterative row generation:")
    pascal_triangle_iterative(rows)
