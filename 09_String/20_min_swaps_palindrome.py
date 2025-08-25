"""
Problem: Minimum Swaps to Make a String Palindrome

Description:
------------
Given a string `s`, the task is to find the minimum number of adjacent swaps
required to rearrange its characters into a palindrome. 
If it is not possible, return -1.

Key Observations:
-----------------
1. A palindrome has at most one character with an odd frequency.
   - If more than one character has odd frequency → return -1.

2. Use two-pointer approach (i, j):
   - If s[i] == s[j], move both inward.
   - Otherwise, find a matching character for s[i] by searching from the right.
     * If no match found except at i itself → this character must be the middle
       character in the palindrome. Swap it with its neighbor and count it.
     * If a match is found at position k (i < k < j) → perform adjacent swaps 
       to bring s[k] to s[j].

3. Continue until i >= j.

Steps:
------
1. Check if palindrome formation is possible (odd frequency check).
2. Apply two-pointer swap process.
3. Return total swaps.

Example:
--------
>>> min_swaps_to_palindrome("mamad")
3
>>> min_swaps_to_palindrome("asflkj")
-1
>>> min_swaps_to_palindrome("aabb")
2
>>> min_swaps_to_palindrome("ntiin")
1

Time Complexity:
----------------
O(n^2) in the worst case (due to nested search and swaps).

Space Complexity:
-----------------
O(n) for storing string as list + frequency counter.
"""


def min_swaps_to_palindrome(s: str) -> int:
    s = list(s)  # make it mutable
    n = len(s)
    
    # Step 1: Check palindrome possibility
    from collections import Counter
    freq = Counter(s)
    odd_count = sum(1 for v in freq.values() if v % 2)
    if odd_count > 1:
        return -1  # not possible
    
    swaps = 0
    i, j = 0, n - 1
    
    while i < j:
        # If characters already match
        if s[i] == s[j]:
            i += 1
            j -= 1
            continue
        
        # Search from right for matching character of s[i]
        k = j
        while k > i and s[k] != s[i]:
            k -= 1
        
        if k == i:  
            # No matching char found → must be the middle char
            s[i], s[i+1] = s[i+1], s[i]
            swaps += 1
        else:
            # Bring s[k] to s[j] by adjacent swaps
            while k < j:
                s[k], s[k+1] = s[k+1], s[k]
                swaps += 1
                k += 1
            i += 1
            j -= 1
    
    return swaps



# ✅ Example Usage
if __name__ == "__main__":
    print(min_swaps_to_palindrome("mamad"))   # Output: 3
    print(min_swaps_to_palindrome("asflkj"))  # Output: -1
    print(min_swaps_to_palindrome("aabb"))    # Output: 2
    print(min_swaps_to_palindrome("ntiin"))   # Output: 1
