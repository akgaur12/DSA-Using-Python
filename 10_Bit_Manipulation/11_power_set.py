"""
Problem: Generate All Subsets using Bit Manipulation

Description:
------------
Given an integer array nums of unique elements, return all possible subsets (the power set).

Approach:
- A set of size n has 2^n subsets.
- Use bitmasks from 0 to (1<<n) - 1 to represent each subset.
- For each bit in mask, include the corresponding element if bit is set.

Time Complexity: O(n * 2^n)
Space Complexity: O(2^n) for storing all subsets
"""

def subsets(nums: list[int]) -> list[list[int]]:
    """Return all subsets of nums using bit manipulation."""
    n = len(nums)
    result = []

    for mask in range(1 << n):  # iterate over all 2^n masks
        subset = []
        for j in range(n):
            if mask & (1 << j):  # if j-th bit is set, include nums[j]
                subset.append(nums[j])
        result.append(subset)

    return result


# Example Usage & Testing
if __name__ == "__main__":
    test_cases = [
        [1, 2, 3],          # standard example
        [0],                # single element
        [4, 5],             # two elements
        [10, 20, 30, 40],   # four elements
        [],                 # empty set should return [[]]
        [7, 8, 9, 10, 11]   # larger case (5 elements → 32 subsets)
    ]

    for nums in test_cases:
        result = subsets(nums)
        print(f"nums = {nums}")
        print(f"Total subsets = {len(result)}")
        print(f"Subsets = {result}")
        print("-" * 50)
