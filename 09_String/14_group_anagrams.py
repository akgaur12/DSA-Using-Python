"""
Problem: Group Anagrams Together Using Character Frequency Hashing

Description:
------------
Given an array of strings, the task is to group all anagrams together.

An anagram is a word formed by rearranging the letters of another word,
e.g., "act" and "cat" are anagrams.

This implementation uses a frequency-based hash to efficiently group
anagrams.

Approach:
---------
1. For each word, generate a frequency hash representing the count of
   each character (a-z) in the word.
2. Use this frequency hash as a key in a dictionary to group words.
3. The words sharing the same frequency hash belong to the same group.

Functions:
----------
1. getHash(s):
   - Generates a unique hash string based on the frequency of characters in `s`.
   - Uses an array of size 26 (for lowercase English letters) and constructs a
     string with counts separated by '$'.

2. anagrams(arr):
   - Iterates through each word in the input list `arr`.
   - Computes the frequency hash using `getHash`.
   - Groups words with the same hash together in the result.

Parameters:
-----------
arr : list of str
    The list of words to group.

Returns:
--------
list of list of str
    Groups of anagrams, where each group is a list of words.

Example:
--------
Input:
    arr = ["act", "god", "cat", "dog", "tac"]

Output:
    Groups of anagrams:
    act cat tac 
    god dog 

Time Complexity: O(N * M)  
    - N = number of words  
    - M = length of each word  
    - For each word, computing frequency takes O(M), and hashing takes O(26).

Space Complexity: O(N * M)
    - Space required for the hashmap and the result list.
"""

MAX_CHAR = 26


def getHash(s):
    """
    Generates a frequency hash for the given string.

    Parameters:
    -----------
    s : str
        Input word consisting of lowercase English letters.

    Returns:
    --------
    str
        A unique string representing the frequency of characters.
    """
    hashList = []
    freq = [0] * MAX_CHAR

    # Count frequency of each character
    for ch in s:
        freq[ord(ch) - ord('a')] += 1

    # Build the hash string with separators
    for i in range(MAX_CHAR):
        hashList.append(str(freq[i]))
        hashList.append("$")

    return ''.join(hashList)


def anagrams(arr):
    """
    Groups anagrams together using frequency hash as a key.

    Parameters:
    -----------
    arr : list of str
        List of words to group.

    Returns:
    --------
    list of list of str
        List of groups where each group contains anagrams.
    """
    res = []
    mp = {}

    for word in arr:
        key = getHash(word)

        # If this hash is not already in the map, create a new group
        if key not in mp:
            mp[key] = len(res)
            res.append([])

        # Append word to the correct group
        res[mp[key]].append(word)

    return res


# -------------------------------------------------------
# ✅ Example Usage
# -------------------------------------------------------
if __name__ == "__main__":
    arr = ["act", "god", "cat", "dog", "tac"]
    result = anagrams(arr)

    print("Grouped Anagrams:")
    for group in result:
        print(" ".join(group))
