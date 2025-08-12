"""
Problem: Print an inverted right-aligned half pyramid of asterisks (*) with n rows.

Description:
------------
This function prints an inverted right-aligned half-pyramid using asterisks:
- The number of asterisks starts from `n` in the first row and decreases to 1.
- Each row is right-aligned using leading spaces.
- Each asterisk is followed by a space for visual clarity.

The pattern is printed directly to the console.

Example:
--------
>>> inverted_right_half_pyramid(5)
* * * * * 
  * * * * 
    * * * 
      * * 
        * 

Time Complexity: O(n²)
    - Each of the n rows may print up to n characters.
Space Complexity: O(1)
    - Only loop counters are used.
"""


def inverted_right_half_pyramid(n):
    for i in range(n, 0, -1):
        print("  " * (n - i) + "* " * i)


# Example Usage
if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    inverted_right_half_pyramid(n)
