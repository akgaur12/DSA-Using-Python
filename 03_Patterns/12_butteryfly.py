"""
Function: butterfly(n)

Description:
------------
Prints a butterfly pattern of stars (*) with `2n` total rows. The pattern is symmetric
horizontally, consisting of two mirrored triangles (upper and lower wings) separated
by increasing/decreasing spaces in between.

Structure:
- First half (rows 1 to n): Increasing stars with decreasing middle spaces.
- Second half (rows n to 1): Decreasing stars with increasing middle spaces.

Each line has:
- i stars
- (2 * (n - i)) spaces (2 spaces per unit for visual alignment)
- i stars

Example:
--------
>>> butterfly(4)
*             *
* *         * *
* * *     * * *
* * * * * * * *
* * * * * * * *
* * *     * * *
* *         * *
*             *

Time Complexity: O(n^2)
    - Two nested loops are used to generate the pattern.
    
Space Complexity: O(1)
    - No extra space is used beyond loop counters.
"""


def butterfly(n):
    for i in range(1, n + 1):
        print("* " * i + "  " * (2 * (n - i)) + "* " * i)
    for i in range(n, 0, -1):
        print("* " * i + "  " * (2 * (n - i)) + "* " * i)


# Example Usage
if __name__ == "__main__":
    n = int(input("Enter the number of rows: "))
    butterfly(n)
