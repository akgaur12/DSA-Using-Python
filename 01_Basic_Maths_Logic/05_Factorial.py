"""
Program to calculates the factorial of a given non-negative integer.

The factorial of a number `n` (written as `n!`) is the product of all
positive integers from 1 to `n`.
Examples:
    5! = 5 × 4 × 3 × 2 × 1 = 120
    0! = 1 (by definition)

Time Complexity:
---------------
- The loop runs `n` times.
- So the time complexity is: O(n)
"""


def factorial(n):
    fact = 1

    # Multiply numbers from n down to 1
    while n:
        fact *= n
        n -= 1

    return fact



# --------- Main Program ---------
try:
    Test_Case = int(input("Enter Number of Test Cases: "))

    while Test_Case:
        n = int(input("Enter a number: "))
        if n < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print("Factorial:", factorial(n))
        Test_Case -= 1

except ValueError:
    print("Invalid input! Please enter an integer.")
