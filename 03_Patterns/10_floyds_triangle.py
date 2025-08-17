"""
Function: floyds_triangle(n)

Description:
------------
Prints Floyd's Triangle of height `n`. Floyd's Triangle is a right-angled triangular array of natural numbers,
used in number pattern problems and algorithms. Numbers are printed in row-wise fashion.

Example:
--------
>>> floyds_triangle(5)
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

Time Complexity: O(n^2)
    - Total numbers printed are 1 + 2 + 3 + ... + n = n(n+1)/2
    
Space Complexity: O(1)
    - Only constant space used for counter.
"""

def floyds_triangle(n):
    count = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(count, end=" ")
            count += 1
        print()


# Example Usage
if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    floyds_triangle(n)
