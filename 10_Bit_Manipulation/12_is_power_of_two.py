"""
Problem: Check if a Number is Power of Two

Description:
------------
Given a non-negative integer n. You have to check if it is a power of 2 or not. 

Approach 1: Bit Manipulation
- A number n is power of 2 if it has only one set bit.
- Trick: n > 0 and (n & (n - 1)) == 0
- Time Complexity: O(1)

Approach 2: Bit Count Method
- Count number of 1's in binary form.
- If exactly one '1', then it's power of 2.
- Trick: bin(n).count("1") == 1
- Time Complexity: O(log n) because of binary conversion

Both methods are implemented below.
"""

def is_power_of_two_bitwise(n: int) -> bool:
    """Check if n is power of 2 using bit manipulation."""
    return n > 0 and (n & (n - 1)) == 0


def is_power_of_two_count(n: int) -> bool:
    """Check if n is power of 2 using bit count method."""
    return n > 0 and bin(n).count("1") == 1


# Example Usage & Testing
if __name__ == "__main__":
    test_cases = [8, 98, 1, 0, 16, 31, 64, 1024]

    print("Using Bit Manipulation Approach:")
    for n in test_cases:
        print(f"n = {n}, is_power_of_two = {is_power_of_two_bitwise(n)}")

    print("\nUsing Bit Count Approach:")
    for n in test_cases:
        print(f"n = {n}, is_power_of_two = {is_power_of_two_count(n)}")
