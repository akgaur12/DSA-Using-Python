"""
Problem: Longest Valid Parentheses Substring

Description:
------------
Given a string consisting of '(' and ')', find the length of
the longest valid (well-formed) parentheses substring.

Example:
---------
Input:  "(()"
Output: 2
Explanation: Longest valid substring is "()"

Input:  ")()())"
Output: 4
Explanation: Longest valid substring is "()()"

------------------------------------------------------------
Approaches Implemented:
1. Stack-based Approach      (O(n) time, O(n) space)
2. Dynamic Programming       (O(n) time, O(n) space)
3. Two-Pass Counter Scan     (O(n) time, O(1) space)
============================================================
"""

# -----------------------------------------------------
# Approach 1: Stack-based (O(n) time, O(n) space)
# -----------------------------------------------------
def longestValidParentheses_stack(s: str) -> int:
    """
    Uses a stack to keep track of indices of characters.
    - Push -1 initially to handle base case.
    - Push index of '('.
    - On ')', pop stack:
        * If stack is not empty, update max length.
        * Else, push current index as a new base.
    """
    stack = [-1]
    max_len = 0
    
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        else:
            stack.pop()
            if stack:
                max_len = max(max_len, i - stack[-1])
            else:
                stack.append(i)
    
    return max_len


# -----------------------------------------------------
# Approach 2: Dynamic Programming (O(n) time, O(n) space)
# -----------------------------------------------------
def longestValidParentheses_dp(s: str) -> int:
    """
    dp[i] stores the length of longest valid parentheses ending at index i.
    Rules:
      1. If s[i] == ')' and s[i-1] == '(':
            dp[i] = dp[i-2] + 2
      2. If s[i] == ')' and s[i-1] == ')':
            If s[i - dp[i-1] - 1] == '(':
                dp[i] = dp[i-1] + 2 + dp[i - dp[i-1] - 2]
    """
    n = len(s)
    dp = [0] * n
    max_len = 0
    
    for i in range(1, n):
        if s[i] == ')':
            if s[i-1] == '(':
                dp[i] = (dp[i-2] if i >= 2 else 0) + 2
            elif i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(':
                dp[i] = dp[i-1] + (dp[i - dp[i-1] - 2] if i - dp[i-1] >= 2 else 0) + 2
        max_len = max(max_len, dp[i])
    
    return max_len


# -----------------------------------------------------
# Approach 3: Two-Pass Counter (O(n) time, O(1) space)
# -----------------------------------------------------
def longestValidParentheses_two_pass(s: str) -> int:
    """
    Scan twice:
      - Left to Right: Count '(' and ')'
      - Right to Left: Count ')' and '('
    Reset counters when imbalance occurs.
    """
    left = right = max_len = 0
    
    # Left to Right scan
    for ch in s:
        if ch == '(':
            left += 1
        else:
            right += 1
        if left == right:
            max_len = max(max_len, 2 * right)
        elif right > left:
            left = right = 0
    
    left = right = 0
    # Right to Left scan
    for ch in reversed(s):
        if ch == ')':
            right += 1
        else:
            left += 1
        if left == right:
            max_len = max(max_len, 2 * left)
        elif left > right:
            left = right = 0
    
    return max_len


# -----------------------------------------------------
# Driver Code
# -----------------------------------------------------
if __name__ == "__main__":
    test_cases = ["((()", ")()())", "(()", "()(()))", ""]

    for s in test_cases:
        print(f"Input: {s}")
        print("Stack     →", longestValidParentheses_stack(s))
        print("DP        →", longestValidParentheses_dp(s))
        print("Two-Pass  →", longestValidParentheses_two_pass(s))
        print("-" * 40)
