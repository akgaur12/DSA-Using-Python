"""
Problem: Check if a Number is Even or Odd using Bit Manipulation
--------

Description:
------------
Given a positive integer n, determine whether it is odd or even.
Return:
- True  → if the number is even
- False → if the number is odd

Bit Manipulation Approach:
--------------------------
Observation:
- In binary, EVEN numbers always end with '0'
  Examples:
    2  = (10)₂
    4  = (100)₂
    44 = (101100)₂

- In binary, ODD numbers always end with '1'
  Examples:
    1  = (1)₂
    3  = (11)₂
    15 = (1111)₂

So, we only need to check the **Least Significant Bit (LSB)**:
- If LSB = 0 → Number is EVEN
- If LSB = 1 → Number is ODD

How to check LSB?
- Perform (n & 1)
    → If result == 0 → LSB is 0 → Even
    → If result == 1 → LSB is 1 → Odd

This avoids division/modulo and directly inspects the binary representation.

Time Complexity: O(1)
Space Complexity: O(1)
"""

def isEven_bitwise(n: int) -> bool:
    """
    Check if a number is even using bitwise AND (&).
    
    Parameters:
    n (int): Positive integer to check
    
    Returns:
    bool: True if even, False if odd
    """
    return (n & 1) == 0


# --------------------------
# Example Usage & Testing
# --------------------------
if __name__ == "__main__":
    test_cases = [15, 44, 7, 100, 1, 2]

    for num in test_cases:
        print(f"n = {num}, Even? {isEven_bitwise(num)}")
