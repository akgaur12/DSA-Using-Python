"""
Problem: Set the Rightmost Unset Bit

Description:
------------
Given a non-negative number n, set the rightmost unset bit in its binary representation.

Approach 1: (Bit Trick)
- Use (n | (n + 1))
- Adding 1 flips the rightmost 0 to 1, OR keeps other bits intact.

Approach 2: (Manual Bit Manipulation)
- Traverse bits from LSB
- When we find the first 0, set it with OR (n | (1 << pos))

Time Complexity: O(log n) in manual method, O(1) in bit trick
Space Complexity: O(1)
"""

# ---------- Approach 1: Bit Trick ---------- #
def setRightmostUnsetBit_trick(n: int) -> int:
    """Set rightmost unset bit using n | (n+1)."""
    return n | (n + 1)


# ---------- Approach 2: Manual Bit Manipulation ---------- #
def setRightmostUnsetBit_manual(n: int) -> int:
    """Set rightmost unset bit using shifting & masking."""
    pos = 0
    while (n & (1 << pos)):  # skip until we find first 0
        pos += 1
    return n | (1 << pos)


# --------------------------
# Example Usage & Testing
# --------------------------
if __name__ == "__main__":
    test_cases = [6, 15, 8, 0]

    for num in test_cases:
        print(f"n = {num}")
        print(f" Trick Method : {setRightmostUnsetBit_trick(num)}")
        print(f" Manual Method: {setRightmostUnsetBit_manual(num)}")
        print("-" * 40)
