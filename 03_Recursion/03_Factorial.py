"""
Program to calculates the factorial of a given non-negative integer.

The factorial of a number `n` (denoted as `n!`) is the product of all
positive integers from 1 to `n`.

Examples:
    5! = 5 × 4 × 3 × 2 × 1 = 120
    0! = 1 (by definition)

Time Complexity:
---------------
- Iterative Method: O(n)
- Recursive Method: O(n) (but has function call overhead)
"""

# Calculates factorial using an iterative approach.
def factorial_iterative(n):
    fact = 1
    while n:
        fact *= n
        n -= 1
    return fact


# Calculates factorial using a recursive approach.
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


# --------- Main Program ---------
if __name__ == "__main__":
    try:
        test_cases = int(input("Enter number of test cases: "))
        
        while test_cases:
            n = int(input("Enter a number: "))
            if n < 0:
                print("Factorial is not defined for negative numbers.")
            else:
                # print("Factorial:", factorial_iterative(n))
                print("Factorial:", factorial_recursive(n))
            test_cases -= 1

    except ValueError:
        print("Invalid input! Please enter an integer.")
