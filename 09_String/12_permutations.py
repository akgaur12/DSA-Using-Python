"""
Problem: Print All Permutations of a String

Description:
------------
Given a string `s`, this program generates all possible permutations of its characters.
Each permutation is a unique arrangement of the characters.

Approach:
---------
- Uses recursive backtracking to generate all permutations.
- At each recursion level, it swaps the current index with every index after it (including itself),
  and continues to the next level.
- After exploring a branch, it backtracks (undoes the swap) to restore the original state.

Time Complexity: O(n x n!)
    - There are n! permutations of a string of length n.
    - Each permutation takes O(n) time to construct.

Space Complexity: O(n!) for storing all permutations in a list.

Example:
Input: s = "abc"
Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
"""


def get_permutations(s):
    result = []

    def backtrack(start, chars):
        # Base Case: If we've reached the end, add the permutation to result
        if start == len(chars):
            result.append("".join(chars))
            return
        for i in range(start, len(chars)):
            # Swap current index with i
            chars[start], chars[i] = chars[i], chars[start]
            backtrack(start + 1, chars)  # Recurse
            chars[start], chars[i] = chars[i], chars[start]  # Backtrack

    # Start the backtracking
    backtrack(0, list(s))
    return result


# Example usage
if __name__ == "__main__":
    s = "abc"
    perms = get_permutations(s)
    print("All Permutations:", perms)