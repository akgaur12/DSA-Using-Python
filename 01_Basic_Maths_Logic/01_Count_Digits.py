"""
Program to counts the number of digits in a given integer.

It handles:
- Positive numbers
- Negative numbers (ignores the minus sign)
- Zero (correctly returns 1 digit)

The core logic divides the number by 10 repeatedly to strip off digits
until the number becomes 0, incrementing a counter along the way.

Time Complexity:
---------------
- The function performs one iteration per digit.
- If the input number has `d` digits, it runs in O(d) time.
- Since `d` is approximately log₁₀(n), the time complexity is:
    O(log₁₀(n))  ≈  O(log n)

Number of Digits (Key Idea)
--------------------------
If a number is n, the number of digits in it is:

    d = ⌊log10(n)⌋ + 1

Examples:
    n = 12345 → d = 5
    n = 999   → d = 3


Intuition (Most Important Part)
-------------------------------
- log10(n) tells how many times you can divide n by 10
- Each division removes one digit
- So, log10(n) ≈ number of digits − 1

👉 That's why we add +1


Final Takeaway
--------------
- Number of digits grows logarithmically
- Therefore, algorithms processing digits (like reversing a number)
  run in O(log n) time complexity
"""
import math


# Iterative Approach
def countDigits(n):
    """
    Counts the number of digits in an integer using iteration.
    Time Complexity: O(log n) - logarithmic time
    Space Complexity: O(1) - constant space
    """
    if n == 0:
        return 1

    num = abs(n)
    count = 0

    while num:            # Loop until the number becomes 0
        count += 1        # Increment the digit count
        num //= 10        # Remove the last digit

    return count


# Using Logarithm Approach (math-based, fast)
def count_digits_log(n):
    """
    Counts the number of digits in an integer using logarithm.
    Time Complexity: O(1) - constant time
    Space Complexity: O(1) - constant space
    """
    if n == 0:
        return 1
    return int(math.log10(abs(n))) + 1


# Recursive Approach
def count_digits_rec(n):
    """
    Counts the number of digits in an integer using recursion.
    Time Complexity: O(log n) - logarithmic time
    Space Complexity: O(log n) - logarithmic space (due to recursion stack)
    """
    n = abs(n)
    if n < 10:
        return 1
    return 1 + count_digits_rec(n // 10)


# --------- Main Program ---------
try:
    Test_Case = int(input("Enter Number of Test Case: "))
    while Test_Case:
        n = int(input("Enter a number: "))
        print("Number of digits (Iterative):", countDigits(n))
        print("Number of digits (Logarithm):", count_digits_log(n))
        print("Number of digits (Recursive):", count_digits_rec(n))
        Test_Case -= 1
except ValueError:
    print("Invalid input! Please enter an integer.")
