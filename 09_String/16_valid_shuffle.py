"""
Problem: Check if a String is a Valid Shuffle of Two Other Strings

Description:
------------
A string `shuffle` is considered a valid shuffle of two strings `str1` and `str2` if:
1. `shuffle` contains all characters from `str1` and `str2` exactly once.
2. The order of characters in `shuffle` does not necessarily need to match that in `str1` or `str2`.

This program checks whether the given `shuffle` is a valid shuffle of `str1` and `str2`.

Approach:
---------
1. Verify if the length of `shuffle` equals the sum of lengths of `str1` and `str2`.
2. Use two frequency arrays (of size 256 to cover all ASCII characters) to count character occurrences:
   - `freq_original` counts characters from `str1` and `str2`.
   - `freq_shuffle` counts characters from `shuffle`.
3. Compare both frequency arrays:
   - If they match, return "YES".
   - Otherwise, return "NO".

Parameters:
-----------
str1 : str
    The first input string.
str2 : str
    The second input string.
shuffle : str
    The string to validate as a shuffle.

Returns:
--------
str
    "YES" if `shuffle` is a valid shuffle of `str1` and `str2`, otherwise "NO".

Example:
--------
>>> is_valid_shuffle("BA", "XY", "XYAB")
'YES'
>>> is_valid_shuffle("BA", "XY", "XUMB")
'NO'
>>> is_valid_shuffle("ABC", "ZYS", "YBAZSC")
'YES'

Time Complexity: O(n)  
    - Where `n` is the length of `shuffle`, as we traverse characters once and compare arrays.  
Space Complexity: O(1)  
    - Fixed space (256 integers) used for frequency arrays.
"""

def is_valid_shuffle(str1, str2, shuffle):
    # Step 1: Check length of shuffle
    if len(shuffle) != len(str1) + len(str2):
        return "NO"

    # Step 2: Initialize frequency arrays for ASCII characters
    freq_original = [0] * 256
    freq_shuffle = [0] * 256

    # Count frequencies of characters from str1 and str2
    for ch in str1:
        freq_original[ord(ch)] += 1
    for ch in str2:
        freq_original[ord(ch)] += 1

    # Count frequencies of characters in shuffle
    for ch in shuffle:
        freq_shuffle[ord(ch)] += 1

    # Step 3: Compare frequency arrays
    for i in range(256):
        if freq_original[i] != freq_shuffle[i]:
            return "NO"

    return "YES"


# -------------------------------------------------------
# ✅ Example Usage
# -------------------------------------------------------
if __name__ == "__main__":
    print(is_valid_shuffle("BA", "XY", "XYAB"))     # YES
    print(is_valid_shuffle("BA", "XY", "XUMB"))     # NO
    print(is_valid_shuffle("ABC", "ZYS", "YBAZSC")) # YES
    print(is_valid_shuffle("AB", "CD", "ACBD"))     # YES
    print(is_valid_shuffle("AB", "CD", "ACBDE"))    # NO
