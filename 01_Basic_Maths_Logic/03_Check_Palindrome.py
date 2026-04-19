"""
Program to checks whether a given integer is a palindrome.

A **palindrome number** is one that reads the same backward as forward.
Examples: 121, 12321, 44 are palindromes.  
          123, 10, 4321 are not.

The script reads multiple test cases and prints True/False for each number,
depending on whether it is a palindrome.

Time Complexity:
---------------
- The number is reversed by processing one digit at a time.
- If the number has `d` digits, the loop runs `d` times.
- So the time complexity is O(d), which is approximately O(log₁₀(n)) ≈ O(log n).

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

👉 That’s why we add +1


Final Takeaway
--------------
- Number of digits grows logarithmically
- Therefore, algorithms processing digits (like reversing a number)
  run in O(log n) time complexity
"""


def checkPalindrome(n):
    num = n         # Keep original number for comparison
    rev_num = 0     # Will store the reversed number

    while num:
        digit = num % 10                # Get the last digit
        rev_num = rev_num * 10 + digit  # Add it to the reversed number
        num //= 10                      # Remove the last digit

    return n == rev_num


# --------- Main Program ---------
try:
    Test_Case = int(input("Enter Number of Test Cases: "))
    while Test_Case:
        n = int(input("Enter a number: "))
        print("Is Palindrome:", checkPalindrome(n))
        Test_Case -= 1
except ValueError:
    print("Invalid input! Please enter an integer.")
