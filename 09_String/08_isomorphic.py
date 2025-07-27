"""
Problem: Check if Two Strings are Isomorphic

Description:
------------
Two strings str1 and str2 are isomorphic if the characters in str1 can be replaced to get str2,
with the following constraints:
- Each character in str1 must map to exactly one character in str2.
- No two characters may map to the same character, but a character may map to itself.

This function checks if two strings are isomorphic by using two hash maps (dictionaries) to track
the mappings from str1 to str2 and from str2 to str1.

Approach:
---------
- First, check if the strings are of equal length. If not, they cannot be isomorphic.
- Then iterate through both strings character by character:
  - Use two dictionaries to maintain the mapping of characters:
    - `map1`: character from str1 → character from str2
    - `map2`: character from str2 → character from str1
  - If a mapping exists and conflicts with a new character, return False.
  - If mapping doesn't exist, create it.

Time Complexity: O(n)
    - n is the length of the strings (only one pass is needed).

Space Complexity: O(1)
    - The number of distinct characters (mapping size) is limited to constant space (26 or 128 max depending on charset).

Example:
Input: str1 = "paper", str2 = "title"
Output: True (p → t, a → i, e → l, r → e)

Input: str1 = "foo", str2 = "bar"  
Output: False (f → b, o → a, but o cannot map to r)
"""

def are_isomorphic(str1, str2):
    if len(str1) != len(str2):
        return False

    map1 = {}  # Map characters from str1 to str2
    map2 = {}  # Map characters from str2 to str1

    for ch1, ch2 in zip(str1, str2):
        if ch1 in map1:
            if map1[ch1] != ch2:
                return False
        else:
            map1[ch1] = ch2

        if ch2 in map2:
            if map2[ch2] != ch1:
                return False
        else:
            map2[ch2] = ch1

    return True


# Example Usage
if __name__ == "__main__":
    str1 = "paper"
    str2 = "title"

    if are_isomorphic(str1, str2):
        print(f'"{str1}" and "{str2}" are isomorphic')
    else:
        print(f'"{str1}" and "{str2}" are not isomorphic')

    str1 = "foo"
    str2 = "bar"
    if are_isomorphic(str1, str2):
        print(f'"{str1}" and "{str2}" are isomorphic')
    else:
        print(f'"{str1}" and "{str2}" are not isomorphic')
