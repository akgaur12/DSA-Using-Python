"""

Problem: Minimum Bit Flips to Convert Number
LeetCode Link: https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/

Description:
------------
Given two integers start and goal, return the minimum number of bit flips to convert start to goal.

Approach:
1. Compute XOR = start ^ goal
   - XOR result has 1's at positions where start and goal differ.
2. Count the number of set bits in XOR (Hamming distance).
   - This gives the minimum number of flips needed.

Methods to count set bits:
- Brian Kernighan's algorithm (efficient).
- Built-in bin(x).count("1") for quick check (not allowed in low-level bit manipulation).

Time Complexity: O(log(max(start, goal)))
Space Complexity: O(1)
"""

# ---------- Approach: XOR + Brian Kernighan ---------- #
def min_bit_flips(start: int, goal: int) -> int:
    """Return minimum bit flips needed to convert start to goal."""
    xor_val = start ^ goal
    count = 0
    while xor_val:
        xor_val &= (xor_val - 1)  # remove the rightmost set bit
        count += 1
    return count


# --------------------------
# Example Usage & Testing
# --------------------------
if __name__ == "__main__":
    test_cases = [(10, 7), (3, 4), (0, 0), (1, 2), (15, 0), (29, 15)]

    for start, goal in test_cases:
        result = min_bit_flips(start, goal)
        print(f"min_bit_flips({start}, {goal}) = {result}")
