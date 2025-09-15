"""
Problem: Check if a Number is a Power of Two
GFG Link: https://leetcode.com/problems/power-of-two/description/

Description:
------------
Given an integer n, return True if it is a power of two.
Otherwise, return False.

Definition:
-----------
An integer n is a power of two if there exists an integer x such that:
    n == 2^x

Bit Manipulation Approach:
--------------------------
Property:
- A power of two has exactly ONE set bit in its binary representation.
- For such numbers: (n & (n - 1)) == 0

Example:
n = 16 → (10000)₂
n-1=15 → (01111)₂
n & (n-1) = 0  → True (Power of Two)

Steps:
1. Check n > 0 (since negative numbers & zero can't be power of 2).
2. Return (n & (n - 1)) == 0

Time Complexity: O(1)
Space Complexity: O(1)
"""

def isPowerOfTwo(n: int) -> bool:
    """Check if n is a power of two using bit manipulation."""
    return n > 0 and (n & (n - 1)) == 0


# --------------------------
# Example Usage & Testing
# --------------------------
if __name__ == "__main__":
    test_cases = [1, 16, 3, 64, 0, -2]

    for num in test_cases:
        print(f"n = {num}, Power of Two? {isPowerOfTwo(num)}")
