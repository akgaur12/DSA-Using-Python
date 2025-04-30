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
"""

def countDigits(n):
    if n == 0:
        return 1

    num = abs(n)
    count = 0

    while num:            # Loop until the number becomes 0
        count += 1        # Increment the digit count
        num //= 10        # Remove the last digit

    return count


# --------- Main Program ---------
try:
    Test_Case = int(input("Enter Number of Test Case: "))
    while Test_Case:
        n = int(input("Enter a number: "))
        print("Number of digits:", countDigits(n))
        Test_Case -= 1
except ValueError:
    print("Invalid input! Please enter an integer.")
