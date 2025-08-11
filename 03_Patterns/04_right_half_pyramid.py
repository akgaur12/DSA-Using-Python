"""
Problem: Print a right-aligned half pyramid of asterisks (*) with n rows.

Description:
------------
This function prints a right-aligned half-pyramid pattern using asterisks:
- Each row contains leading spaces to align the stars to the right.
- The number of asterisks per row increases from 1 to n.
- Each asterisk is followed by a space for clear formatting.

The pattern is printed directly to the console.

Example:
--------
>>> right_half_pyramid(5)
        * 
      * * 
    * * * 
  * * * * 
* * * * * 

Time Complexity: O(n²)
    - Nested structure due to printing increasing number of characters per row.
Space Complexity: O(1)
    - Only loop counters are used.
"""


def right_half_pyramid(n):
    for i in range(1, n+1):
        print("  " * (n - i) + "* " * i)


# Example Usage
if __name__ == "__main__":
    n = int(input("Enter the number of rows: "))
    right_half_pyramid(n)
