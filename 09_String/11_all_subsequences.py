"""
Problem: Print All Subsequences of a String

Description:
------------
A subsequence is a sequence derived from another sequence by deleting some or no elements
without changing the order of the remaining elements.

This program implements two methods to find all subsequences of a given string:
1. Recursive Approach
2. Iterative Bitmasking Approach

Both methods return a list of all possible subsequences (including the empty string).

1. Recursive Approach (Backtracking)
-----------------------------------------
- At each step, the function decides to either include or exclude the current character.
- Uses recursion with backtracking to explore all 2^n possibilities.

Time Complexity: O(2^n): Each character has two choices: include or exclude.
Space Complexity: O(2^n * n): There are 2^n subsequences and each can be up to length n.

    
# 2. Iterative Approach (Bitmasking)
# -----------------------------------------
- Each bit in the binary representation of numbers from 0 to 2^n - 1 represents
  whether to include the character at that position.
- This results in 2^n combinations/subsequences.

Time Complexity: O(2^n * n): 2^n combinations, each requiring O(n) to construct.
Space Complexity: O(2^n * n): Stores all subsequences.
"""


def get_subsequences(s, index=0, current="", result=None):
    if result is None:
        result = []

    if index == len(s):
        result.append(current)
        return result

    # Include current character
    get_subsequences(s, index + 1, current + s[index], result)

    # Exclude current character
    get_subsequences(s, index + 1, current, result)

    return result


def get_subsequences_iterative(s):
    n = len(s)
    total = 1 << n  # Total subsequences = 2^n
    result = []

    for i in range(total):
        subseq = ""
        for j in range(n):
            if i & (1 << j):
                subseq += s[j]
        result.append(subseq)

    return result


# Example usage
s = "abc"
print("Recursive Approach - All Subsequences:")
print(get_subsequences(s))
print("\nIterative Bitmasking Approach - All Subsequences:")
print(get_subsequences_iterative(s))
