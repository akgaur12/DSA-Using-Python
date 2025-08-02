"""
Problem: Valid Parentheses Check

Description:
------------
Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

A string is considered valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Approaches:
-----------
1. Using Stack (Efficient O(n) Solution)
2. Without Stack (Using String Replacement)

Time Complexity:
----------------
- Stack Approach: O(n)
- Replacement Approach: O(n^2) (because repeated string replacements take O(n))

Space Complexity:
-----------------
- Stack Approach: O(n)
- Replacement Approach: O(1)
"""

# ----------------------------------------------------------
# ✅ 1. Using Stack (Efficient O(n) Solution)
# ----------------------------------------------------------

def is_valid_parentheses_stack(s: str) -> bool:
    """
    Checks if the given string of brackets is valid using a stack.

    Algorithm:
    ----------
    - Use a stack to store opening brackets.
    - When encountering a closing bracket, check if it matches the last opening bracket.
    - If mismatched or stack is empty at any point, return False.
    - After processing, the stack must be empty.

    Parameters:
    -----------
    s : str
        Input string containing brackets.

    Returns:
    --------
    bool
        True if the string is valid, False otherwise.
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in mapping.values():      # Opening bracket
            stack.append(ch)
        elif ch in mapping:             # Closing bracket
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop()
    return not stack  # True only if all brackets matched


# ----------------------------------------------------------
# ✅ 2. Without Stack (Using String Replacement)
# ----------------------------------------------------------

def is_valid_parentheses_no_stack(s: str) -> bool:
    """
    Checks if the given string of brackets is valid without using a stack.

    Algorithm:
    ----------
    - Repeatedly remove all occurrences of valid pairs "()", "{}", and "[]".
    - Continue until no changes occur in the string.
    - If the final string is empty, it's valid; otherwise, invalid.

    Parameters:
    -----------
    s : str
        Input string containing brackets.

    Returns:
    --------
    bool
        True if the string is valid, False otherwise.
    """
    prev = None
    while prev != s:  # Keep removing until no change
        prev = s
        s = s.replace("()", "").replace("{}", "").replace("[]", "")
    return s == ""


# ----------------------------------------------------------
# ✅ Example Usage / Testing Both Methods
# ----------------------------------------------------------
if __name__ == "__main__":
    test_cases = ["[{()}]", "[()()]{}", "([]", "([{]})"]

    for t in test_cases:
        print(f"Input: {t}")
        print("Using Stack: ", is_valid_parentheses_stack(t))
        print("Without Stack: ", is_valid_parentheses_no_stack(t))
        print("---")
