"""
Pattern Printing: Solid and Hollow Rectangle

Description:
------------
This module provides two functions:
1. `solid_rectangle(r, c)`: Prints a solid rectangle made of asterisks (*) with `r` rows and `c` columns.
2. `hollow_rectangle(r, c)`: Prints a hollow rectangle where only the border is made of asterisks, and the inside is empty.

Each function directly prints the desired pattern to the console.

Examples:
---------
>>> solid_rectangle(3, 5)
* * * * * 
* * * * * 
* * * * * 

>>> hollow_rectangle(4, 5)
* * * * * 
*       * 
*       * 
* * * * * 

Time Complexity: O(r × c)
    - Both functions iterate over each of the `r` rows and `c` columns to build the pattern.

Space Complexity: O(1)
    - Only loop variables and control structures are used. No extra space required.

Note: Each asterisk is followed by a space for better visual clarity in pattern alignment.
"""


def solid_rectangle(r, c):
    for i in range(r):
        print("* " * c)


def hollow_rectangle(r, c):
    for i in range(r):
        for j in range(c):
            if i == 0 or i == r - 1 or j == 0 or j == c - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


# Example Usage
if __name__ == "__main__":
    r = int(input("Enter number of rows: "))
    c = int(input("Enter number of columns: "))
    
    print("\nSolid Rectangle:")
    solid_rectangle(r, c)

    print("\nHollow Rectangle:")
    hollow_rectangle(r, c)
