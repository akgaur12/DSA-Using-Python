"""
Problem: First Non-Repeating Character in a String
GFG Link: https://www.geeksforgeeks.org/problems/non-repeating-character-1587115620/1

Description:
------------
Given a string, find the first character that does not repeat anywhere in the string.
Return the character if found, else return None.

Example:
--------
Input  : "aabbcdde"
Output : "c"

Approach:
---------
1. Use a dictionary to store the frequency of each character.
2. Iterate through the string a second time to find the first character with frequency 1.

Time Complexity  : O(n)
Space Complexity : O(1) - Since the alphabet size is constant (for ASCII), the space is bounded.
"""


def first_non_repeating_char(s):
    freq = {}

    # First pass: count frequency of each character
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    # Second pass: find the first character with frequency 1
    for char in s:
        if freq[char] == 1:
            return char

    return None  # No non-repeating character found


# Example Usage
if __name__ == "__main__":
    input_str = "aabbcdde"
    result = first_non_repeating_char(input_str)

    if result:
        print(f"First non-repeating character: '{result}'")
    else:
        print("No non-repeating character found.")
