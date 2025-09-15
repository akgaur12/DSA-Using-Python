"""
Problem: Count Set Bits from 1 to n
GFG Link: https://www.geeksforgeeks.org/problems/count-total-set-bits-1587115620/1

Description:
------------
You are given a number n. Find the total count of set bits for all numbers from 1 to n (inclusive).

Examples:
---------
Input: n = 4
Output: 5
Explanation:
    1 → 001 → 1 set bit
    2 → 010 → 1 set bit
    3 → 011 → 2 set bits
    4 → 100 → 1 set bit
    Total = 5

Input: n = 17
Output: 35

Approaches:
-----------
1. Naive (O(n log n)):
   - Loop through all numbers from 1..n
   - Count set bits in each using Kernighan’s Algorithm (x & (x-1))

2. Efficient (O(log n)):
   - Count set bits per bit position using repeating bit patterns
   - Uses formula:
        cycle_len = 2^(i+1)
        full_cycles = (n+1) // cycle_len
        remainder   = (n+1) % cycle_len
        count_i = full_cycles * 2^i + max(0, remainder - 2^i)
   - Sum for all i
"""

# ---------------- Naive Approach ---------------- #
def countSetBits_naive(n: int) -> int:
    """Naive O(n log n) approach using Kernighan’s Algorithm."""

    def countBits(x: int) -> int:
        count = 0
        while x:
            x &= (x - 1)   # remove the lowest set bit
            count += 1
        return count

    total = 0
    for i in range(1, n + 1):
        total += countBits(i)
    return total


# ---------------- Efficient Approach ---------------- #
def countSetBits(n: int) -> int:
    """Efficient O(log n) approach using bit pattern observation."""
    total = 0
    i = 0

    while (1 << i) <= n:
        cycle_len = 1 << (i + 1)   # 2^(i+1)
        full_cycles = (n + 1) // cycle_len
        remainder = (n + 1) % cycle_len

        total += full_cycles * (1 << i) + max(0, remainder - (1 << i))
        i += 1

    return total


# ---------------- Testing ---------------- #
if __name__ == "__main__":
    test_cases = [4, 17, 7, 10]

    for num in test_cases:
        print(f"n = {num}")
        print(f"Naive Count     = {countSetBits_naive(num)}")
        print(f"Efficient Count = {countSetBits(num)}")
        print("-" * 40)
