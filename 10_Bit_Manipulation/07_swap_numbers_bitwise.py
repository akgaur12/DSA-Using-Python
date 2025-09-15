"""
Problem: Swap Two Numbers using Bit Manipulation
GFG Link: https://www.geeksforgeeks.org/problems/swap-two-numbers3844/1

Description:
------------
Given two numbers a and b, swap them without using a temporary variable.

Approach:
Use XOR (^) operation:
    a = a ^ b
    b = a ^ b   # now b becomes original a
    a = a ^ b   # now a becomes original b

Time Complexity: O(1)
Space Complexity: O(1)
"""

def swap_using_xor(a: int, b: int) -> tuple[int, int]:
    """Swap two numbers using XOR (bit manipulation)."""
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


# --------------------------
# Example Usage & Testing
# --------------------------
if __name__ == "__main__":
    test_cases = [(13, 9), (15, 8), (0, 5), (7, 7)]

    for a, b in test_cases:
        swapped = swap_using_xor(a, b)
        print(f"Original: a={a}, b={b} --> Swapped: a={swapped[0]}, b={swapped[1]}")
