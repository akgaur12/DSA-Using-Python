"""
Problem: Print a left-aligned half pyramid of asterisks (*) with n rows.

Description:
------------
This function prints a simple half-pyramid pattern of asterisks where:
- The first row contains 1 asterisk.
- The second row contains 2 asterisks.
- ...
- The nth row contains n asterisks.
Each asterisk is followed by a space for clear formatting.
The pattern is printed directly to the console.

Example:
--------
>>> half_pyramid(4)
* 
* * 
* * * 
* * * * 

Time Complexity: O(n²)
    - For n rows, a total of 1 + 2 + ... + n = n(n+1)/2 print operations.

Space Complexity: O(1)
    - Only loop counters are used.
"""


def half_pyramid(n):
    for i in range(1, n + 1):
        print("* " * i)


# Example Usage
if __name__ == "__main__":
    n = int(input("Enter the number of rows: "))
    half_pyramid(n)
