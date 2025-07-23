"""
Problem: Check if two strings are anagrams of each other.

Definition:
-----------
Two strings are anagrams if they contain the same characters 
in the same frequency but possibly in different order.

Approach:
---------
1. First, check if the lengths of the strings are different.
   - If yes, they can't be anagrams.
2. Use a hash map (dictionary) to count the frequency of each character in the first string.
3. Traverse the second string:
   - For each character, decrement its count in the hash map.
   - If a character in str2 doesn’t exist in the hash map, return False.
4. After processing both strings, verify that all frequency values are zero.

Time Complexity: O(n)
- n = length of the strings (since they are equal length).
- One pass through each string and a final pass through the map.

Space Complexity: O(1)
- At most 26 characters (if only lowercase English), so constant space.

Args:
-----
str1 (str): First string
str2 (str): Second string

Returns:
--------
bool: True if the strings are anagrams, False otherwise.
"""


def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    freq_map = {}

    # Count frequency of each character in str1
    for ch in str1:
        if ch in freq_map:
            freq_map[ch] += 1
        else:
            freq_map[ch] = 1

    # Subtract frequency using str2
    for ch in str2:
        if ch in freq_map:
            freq_map[ch] -= 1
        else:
            return False  # Extra character found in str2

    # Check if all counts are zero
    for count in freq_map.values():
        if count != 0:
            return False

    return True



# Example Usage
if __name__ == "__main__":
    s1 = "listen"
    s2 = "silent"

    if are_anagrams(s1, s2):
        print("Strings are anagrams")
    else:
        print("Strings are not anagrams")
