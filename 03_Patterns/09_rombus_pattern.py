"""
Pattern Printing: Rhombus Variants

Description:
------------
This script demonstrates the printing of various rhombus-shaped patterns using loops.

Rhombus Pattern Overview:
-------------------------
A **rhombus** is a parallelogram with all sides equal in length. In pattern printing,
it visually resembles a tilted square with equal-width rows, indented to form a symmetric shape.

Types of Rhombus Patterns in this Script:
-----------------------------------------
1. Solid Rhombus:
   - A full rhombus made entirely of asterisks (*).
   - All positions are filled.
   - Example (n = 4):
         * * * * 
        * * * * 
       * * * * 
      * * * * 

2. Hollow Rhombus:
   - Only borders of the rhombus are filled with asterisks.
   - Inside is hollow.
   - Example (n = 4):
         * * * * 
        *     * 
       *     * 
      * * * * 

3. Number Rhombus:
   - Each row contains numbers from 1 to n, spaced and aligned to form a rhombus.
   - Example (n = 4):
         1 2 3 4 
        1 2 3 4 
       1 2 3 4 
      1 2 3 4 

Each function takes a single integer `n` which determines the number of rows (and width) of the rhombus.

Time Complexity: O(n²) for each pattern
Space Complexity: O(1)
"""

def solid_rhombus(n):
    for i in range(n):
        print(" " * (n - i - 1) + "* " * n)


def hollow_rhombus(n):
    for i in range(n):
        print(" " * (n - i - 1), end="")
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def number_rhombus(n):
    for i in range(n):
        print(" " * (n - i - 1), end="")
        for j in range(1, n + 1):
            print(j, end=" ")
        print()


# Example Usage
if __name__ == "__main__":
    n = int(input("Enter the number of rows for rhombus pattern: "))

    print("\nSolid Rhombus:")
    solid_rhombus(n)

    print("\nHollow Rhombus:")
    hollow_rhombus(n)

    print("\nNumber Rhombus:")
    number_rhombus(n)
