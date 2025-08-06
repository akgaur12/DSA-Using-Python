"""
Problem: Rabin-Karp Pattern Matching Algorithm

Description:
------------
The Rabin-Karp algorithm is used to find all occurrences of a pattern in a given text efficiently 
using a hashing technique. Instead of comparing the pattern with every substring of the text directly, 
it uses a rolling hash to quickly skip over non-matching substrings.

How It Works:
-------------
1. Compute the hash of the pattern and the first window (substring) of the text with the same length.
2. Slide the window one character at a time:
   - Update the hash efficiently (rolling hash).
   - If the hash matches the pattern hash, compare the substring to confirm (to avoid hash collisions).
3. Repeat until the end of the text.

Parameters:
-----------
text : str
    The main text where the pattern needs to be searched.
pattern : str
    The pattern to search for in the text.
prime : int
    A prime number used for the hash modulus to reduce collisions (default: 101).

Returns:
--------
list[int]
    A list of starting indices where the pattern is found in the text.

Example:
--------
>>> rabin_karp("ABCCDDAEFG", "CDD")
[2]
>>> rabin_karp("GEEKS FOR GEEKS", "GEEK")
[0, 10]

Time Complexity:
----------------
- Average and Best Case: O(n + m)  (n: length of text, m: length of pattern)
- Worst Case: O(nm)  (due to hash collisions requiring extra comparisons)

Space Complexity:
-----------------
O(1) - Only a few integer variables are used.
"""

def rabin_karp(text, pattern, prime=101):
    n = len(text)
    m = len(pattern)
    if m > n:
        return []

    d = 256  # Number of characters in the input alphabet
    h = pow(d, m - 1) % prime
    p_hash = 0   # Hash value for pattern
    t_hash = 0   # Hash value for current window in text
    result = []

    # Step 1: Calculate initial hash for pattern and first window of text
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % prime
        t_hash = (d * t_hash + ord(text[i])) % prime

    # Step 2: Slide the pattern over text one by one
    for i in range(n - m + 1):
        # If hash values match, check characters one by one
        if p_hash == t_hash:
            if text[i:i + m] == pattern:
                result.append(i)

        # Step 3: Compute hash for the next window
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % prime

            # In case of negative hash value
            if t_hash < 0:
                t_hash += prime

    return result


# -------------------------------------------------------
# ✅ Example Usage
# -------------------------------------------------------
if __name__ == "__main__":
    print("Matches found at indices:", rabin_karp("ABCCDDAEFG", "CDD"))
    print("Matches found at indices:", rabin_karp("GEEKS FOR GEEKS", "GEEK"))
