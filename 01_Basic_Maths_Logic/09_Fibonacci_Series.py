"""
Program to generate the **Fibonacci series** up to `n` terms (starting from 0 and 1).

The **Fibonacci series** is a sequence of numbers in which each number is the sum of the two preceding ones.
The series starts as: 0, 1, 1, 2, 3, 5, 8, ...

This program:
- Accepts multiple test cases.
- Prints the series with (n + 2) terms (starts from 0 and 1, and includes n additional terms).
- Handles invalid and negative input.

Examples:
    Input: n = 3
    Output: [0, 1, 1, 2, 3]

Time Complexity:
---------------
- O(n) — iterates n times to generate the sequence
"""


def fibonacci(n: int):
    first = 0
    second = 1
    fib = [0, 1]

    while n:
        next = first + second
        fib.append(next)
        first = second
        second = next
        n -= 1

    return fib


# --------- Main Program ---------
try:
    Test_Case = int(input("Enter Number of Test Cases: "))

    while Test_Case:
        n = int(input("Enter a number: "))
        if n < 0:
            print("Please enter a non-negative number.")
        else:
            print("Fibonacci Series:", fibonacci(n))
        Test_Case -= 1

except ValueError:
    print("Invalid input! Please enter an integer.")
