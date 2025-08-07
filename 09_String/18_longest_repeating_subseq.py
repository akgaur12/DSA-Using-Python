"""
Problem: Longest Repeating Subsequence (LRS)

Description:
------------
The Longest Repeating Subsequence (LRS) problem is to find the length of the longest subsequence 
of a string that appears at least twice without overlapping the same indices. 
Unlike the Longest Common Subsequence (LCS), here we compare the string with itself 
but ensure that no character is matched with itself (i != j).

Approach:
---------
This solution uses Dynamic Programming (DP) similar to LCS:
1. Create a DP table `dp` of size (n+1) x (n+1), where n is the length of the string.
2. Iterate through the string with two indices `i` and `j`.
3. If characters match (`s[i-1] == s[j-1]`) and indices are not the same (`i != j`), 
   increment `dp[i][j]` by 1 plus the value of the previous diagonal (`dp[i-1][j-1]`).
4. Otherwise, take the maximum of excluding the current character from either index 
   (`max(dp[i-1][j], dp[i][j-1])`).
5. The value at `dp[n][n]` gives the length of the Longest Repeating Subsequence.

Example:
--------
>>> longest_repeating_subsequence("aabb")
2   # "ab"
>>> longest_repeating_subsequence("axxxy")
2   # "xx"
>>> longest_repeating_subsequence("aabebcdd")
3   # "abd"

Time Complexity: O(n²) - Two nested loops for DP table filling.
----------------

Space Complexity: O(n²) - DP table of size (n+1) x (n+1).
-----------------
"""

def longest_repeating_subsequence(s: str) -> int:
    n = len(s)
    # Create DP table
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Build table similar to LCS but avoid matching same index
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == s[j - 1] and i != j:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][n]


# -------------------------------------------------------
# ✅ Example Usage
# -------------------------------------------------------
if __name__ == "__main__":
    print(longest_repeating_subsequence("aabb"))     # Output: 2
    print(longest_repeating_subsequence("axxxy"))    # Output: 2
    print(longest_repeating_subsequence("aabebcdd")) # Output: 3
