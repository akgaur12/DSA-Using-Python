"""
Program to finds all the **factors** of a given positive integer.

A **factor** of a number `n` is any number that divides `n` exactly (no remainder).
For example:
    - Factors of 6: [1, 2, 3, 6]
    - Factors of 10: [1, 2, 5, 10]

This script handles multiple test cases and prints the list of all factors for each input.

Time Complexity:
---------------
- The loop checks up to n/2, so the time complexity is O(n)
- (Optimizations possible with O(√n), but this version uses O(n) approach)
"""


def factors(n):
    f = []
    
    # Check all numbers from 1 to n//2
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            f.append(i)  # i is a factor

    f.append(n)  # n is always a factor of itself
    return f



# --------- Main Program ---------
try:
    Test_Case = int(input("Enter Number of Test Cases: "))

    while Test_Case:
        n = int(input("Enter a number: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            print("Factors:", factors(n))
        Test_Case -= 1

except ValueError:
    print("Invalid input! Please enter an integer.")
