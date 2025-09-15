"""
Problem: Check K-th Bit in a Number
GFG Link: https://www.geeksforgeeks.org/problems/check-whether-k-th-bit-is-set-or-not-1587115620/1

Description:
------------
Given two positive integers n and k, check if the k-th index bit of n is set (1) or not (0).

Note:
- Bits are counted from the Least Significant Bit (LSB) starting at index 0.
- A bit is said to be "set" if it is 1.

We will implement two approaches:
1. Using LEFT SHIFT operator (<<)
2. Using RIGHT SHIFT operator (>>)

Examples:
---------
Input: n = 4, k = 0
Binary: 100
Output: False  (0th bit is 0)

Input: n = 4, k = 2
Binary: 100
Output: True   (2nd bit is 1)

Input: n = 500, k = 3
Binary: 111110100
Output: False  (3rd bit is 0)
"""

def isKthBitSet_leftShift(n: int, k: int) -> bool:
    """
    Check K-th bit using LEFT SHIFT.

    Idea:
    - Shift 1 by k positions to create a mask with only the k-th bit set.
      Example: For k = 2 -> mask = 1 << 2 = 100 (binary)
    - Perform bitwise AND with n. If result != 0, the k-th bit is set.

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    mask = 1 << k
    return (n & mask) != 0


def isKthBitSet_rightShift(n: int, k: int) -> bool:
    """
    Check K-th bit using RIGHT SHIFT.

    Idea:
    - Right shift n by k positions.
    - Check the least significant bit (LSB) of the result.
    - If (n >> k) & 1 == 1, then k-th bit is set.

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    return ((n >> k) & 1) == 1


# --------------------------
# Example Usage & Testing
# --------------------------
if __name__ == "__main__":
    test_cases = [
        (4, 0),   # Expected False
        (4, 2),   # Expected True
        (500, 3)  # Expected False
    ]

    for n, k in test_cases:
        print(f"n = {n}, k = {k}")
        print(f"Using Left Shift: {isKthBitSet_leftShift(n, k)}")
        print(f"Using Right Shift: {isKthBitSet_rightShift(n, k)}")
        print("-" * 40)
