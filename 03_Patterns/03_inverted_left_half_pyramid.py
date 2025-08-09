"""
Problem: Print an inverted left-aligned half pyramid of asterisks (*) with n rows.

Description:
------------
This function prints an inverted half-pyramid pattern of asterisks where:
- The first row contains n asterisks.
- The second row contains n-1 asterisks.
- ...
- The nth row contains 1 asterisk.
Each asterisk is followed by a space for consistent formatting.
The pattern is printed directly to the console.

Example:
--------
>>> inverted_half_pyramid(4)
* * * * 
* * * 
* * 
* 

Time Complexity: O(n²)
    - For n rows, the total number of asterisks printed is n(n+1)/2.
Space Complexity: O(1)
    - Only loop counters are used.
"""


def inverted_half_pyramid(n):
    for i in range(n, 0, -1):
        print("* " * i)


# Example Usage
if __name__ == "__main__":
    n = int(input("Enter the number of rows: "))
    inverted_half_pyramid(n)
