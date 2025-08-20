"""
Pattern Printing: Diamond Pattern

Description:
------------
This function prints a **diamond-shaped pattern** made of asterisks (`*`).

Structure:
----------
- The pattern consists of two symmetrical halves:
  1. The **upper half** is a standard left-aligned triangle with increasing stars.
  2. The **lower half** is an inverted triangle with decreasing stars.
- Each row is center-aligned using leading spaces.

Example (n = 5):
        * 
       * * 
      * * * 
     * * * * 
    * * * * * 
     * * * * 
      * * * 
       * * 
        * 

Time Complexity: O(n²)
    - Each of the 2n - 1 rows has up to n characters.

Space Complexity: O(1)
    - Only loop counters and fixed space used.
"""


def diamond_pattern(n):
    # Upper half of the diamond (including middle row)
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)

    # Lower half of the diamond
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "* " * i)


# Example usage
if __name__ == "__main__":
    n = int(input("Enter the number of rows for the diamond pattern: "))
    diamond_pattern(n)
