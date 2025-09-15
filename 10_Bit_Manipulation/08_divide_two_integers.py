"""
Problem: Divide Two Integers without using *, /, or %
LeetCode Link: https://leetcode.com/problems/divide-two-integers/description/

Description:
------------
Given two integers dividend and divisor, return the quotient after dividing dividend by divisor.
Truncate toward zero. Handle 32-bit signed integer overflow.

Approach:
- Use bit manipulation (left shift) to speed up repeated subtraction.
- For each step, shift divisor until it's <= dividend, subtract it, and increase quotient.
- Apply sign at the end.
- Clamp to [-2^31, 2^31 - 1].

Time Complexity: O(log |dividend|)
Space Complexity: O(1)
"""

INT_MAX = 2**31 - 1
INT_MIN = -2**31

def divide(dividend: int, divisor: int) -> int:
    # Handle overflow case
    if dividend == INT_MIN and divisor == -1:
        return INT_MAX
    
    # Determine sign of result
    negative = (dividend < 0) ^ (divisor < 0)
    
    # Work with absolute values
    dividend, divisor = abs(dividend), abs(divisor)
    
    quotient = 0
    
    # Subtract divisor multiples using bit shifts
    while dividend >= divisor:
        temp, multiple = divisor, 1
        while dividend >= (temp << 1):
            temp <<= 1
            multiple <<= 1
        dividend -= temp
        quotient += multiple
    
    # Apply sign
    if negative:
        quotient = -quotient
    
    # Clamp result within 32-bit range
    return max(min(quotient, INT_MAX), INT_MIN)


# --------------------------
# Example Usage & Testing
# --------------------------
if __name__ == "__main__":
    test_cases = [(10, 3), (7, -3), (-15, 2), (1, 1), (-2**31, -1)]

    for dividend, divisor in test_cases:
        result = divide(dividend, divisor)
        print(f"divide({dividend}, {divisor}) = {result}")
