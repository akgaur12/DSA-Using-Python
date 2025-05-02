"""
Program to reverses a positive integer.

It handles:
- Positive integers
- The reversal is performed digit by digit using arithmetic (no string operations)

The core logic extracts the last digit using modulo, and builds the reversed number
by multiplying the accumulator by 10 and adding the digit.

Time Complexity:
---------------
- For each input number with `d` digits, the loop runs `d` times.
- Time complexity is therefore O(d), which is approximately O(log n)
  where `n` is the input number.
"""

def reverseNumber(num):
    if num <= 9:
        return n
    
    rev_num = 0
    
    while num:
        digit = num % 10                 # Get the last digit
        rev_num = rev_num * 10 + digit   # Append it to the reversed number
        num //= 10                       # Remove the last digit

    return rev_num
        

# --------- Main Program ---------
try:
    Test_Case = int(input("Enter Number of Test Case: "))
    while Test_Case:
        n = int(input("Enter a number: "))
        print("Reversed number:", reverseNumber(n))
        Test_Case -= 1
except ValueError:
    print("Invalid input! Please enter an integer.")