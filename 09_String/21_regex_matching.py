"""
Problem: Regular Expression Matching

Description:
------------
Implement regular expression matching with support for '.' and '*'.

Rules:
------
1. '.' Matches any single character.
2. '*' Matches zero or more of the preceding element.

Given a text `t` and a pattern `p`, return True if the entire text 
matches the entire pattern.

Approach:
---------
We use Dynamic Programming (DP) with a 2D table `dp`:
- dp[i][j] = whether t[:i] matches p[:j]
  (i.e., first i characters of text match first j characters of pattern).

Steps:
------
1. Initialization:
   - dp[0][0] = True  (empty text matches empty pattern)
   - Handle patterns like "a*", "a*b*", "a*b*c*" that can match empty text.

2. Transition:
   Case 1: If pattern[j-1] == '.' or pattern[j-1] == text[i-1]:
           → Characters match, so:
             dp[i][j] = dp[i-1][j-1]

   Case 2: If pattern[j-1] == '*':
           → Two possibilities:
              a) '*' means zero occurrence of preceding char:
                 dp[i][j] = dp[i][j-2]
              b) '*' means one or more occurrence:
                 If preceding character matches text[i-1],
                 dp[i][j] |= dp[i-1][j]

3. Final answer is dp[n][m].


Complexity:
-----------
Time  : O(n * m)  where n = len(t), m = len(p)
Space : O(n * m)  for DP table

Examples:
---------
>>> isMatch("aaa", "a")
False
>>> isMatch("abb", "a.*")
True
>>> isMatch("", "a*b*")
True
>>> isMatch("mississippi", "mis*is*p*.")
False
>>> isMatch("ab", ".*")
True
"""

def isMatch(t: str, p: str) -> bool:
    n, m = len(t), len(p)
    
    # dp[i][j] = does t[:i] match p[:j]
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    
    dp[0][0] = True  # empty string matches empty pattern
    
    # Handle patterns like a*, a*b*, a*b*c* that can match empty string
    for j in range(2, m + 1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]
    
    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if p[j-1] == '.' or p[j-1] == t[i-1]:
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                # zero occurrence of preceding char
                dp[i][j] = dp[i][j-2]
                
                # one or more occurrence (if match with preceding char)
                if p[j-2] == '.' or p[j-2] == t[i-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j]
    
    return dp[n][m]


# ---- Example Usage ----
if __name__ == "__main__":
    print(isMatch("aaa", "a"))          # False
    print(isMatch("abb", "a.*"))        # True
    print(isMatch("", "a*b*"))          # True
    print(isMatch("mississippi", "mis*is*p*."))  # False
    print(isMatch("ab", ".*"))          # True
