"""
Problem: Longest Substring Without Repeating Characters

Description:
------------
Given a string `s`, find:
1. The length of the longest substring without repeating characters.
2. The longest substring itself that does not contain any repeated characters.

Approach:
---------
Both solutions use the **Sliding Window Technique**:
- Maintain a window defined by two pointers (`left` and `right`).
- Use a data structure (`set` or `dict`) to track characters in the current window.
- Expand the window by moving `right` and shrink it by moving `left` when duplicates are found.

Functions:
----------
1. length_of_longest_substring(s):
   - Returns the length of the longest substring without repeating characters.
   - Uses a `set` to store current window characters.
   - Removes characters from the set while duplicates exist.

2. longest_unique_substring(s):
   - Returns the actual longest substring without repeating characters.
   - Uses a dictionary `seen` to store the last seen index of characters.
   - Adjusts the `left` pointer to ensure uniqueness in the current window.

Parameters:
-----------
s : str
    Input string to analyze.

Returns:
--------
For `length_of_longest_substring`:
    int - Length of the longest substring without repeating characters.
For `longest_unique_substring`:
    str - The longest substring itself.

Example:
--------
>>> length_of_longest_substring("abcabcbb")
3
>>> longest_unique_substring("abcabcbb")
'abc'

Time Complexity: O(n)  
    - Each character is visited at most twice.  
Space Complexity: O(min(n, a))  
    - Where `a` is the alphabet size (limited to characters in the input string).
"""


# Finds the length of the longest substring without repeating characters.
def length_of_longest_substring(s: str) -> int:
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


# Finds the actual longest substring without repeating characters.
def longest_unique_substring(s: str) -> str:
    seen = {}
    left = 0
    max_len = 0
    start = 0

    for right, char in enumerate(s):
        # If character already seen in current window, move left pointer
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right

        # Update maximum length and start index
        if right - left + 1 > max_len:
            max_len = right - left + 1
            start = left

    return s[start:start + max_len]


# -------------------------------------------------------
# ✅ Example Usage
# -------------------------------------------------------
if __name__ == "__main__":
    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwkew"

    print("Length of longest substring (no repeat):", length_of_longest_substring(s1))  # 3
    print("Longest unique substring:", longest_unique_substring(s1))  # "abc"

    print("Length of longest substring (no repeat):", length_of_longest_substring(s2))  # 1
    print("Longest unique substring:", longest_unique_substring(s2))  # "b"

    print("Length of longest substring (no repeat):", length_of_longest_substring(s3))  # 3
    print("Longest unique substring:", longest_unique_substring(s3))  # "wke"
