"""
Problem: Longest Common Prefix using Sorting

Description:
------------
Given an array of strings, the task is to find the longest common prefix (LCP) among them.
If there is no common prefix, return an empty string `""`.

Approach:
---------
1. Sort the list of strings lexicographically.
2. After sorting, the first and last strings will have the minimum and maximum difference.
3. Compare characters of the first and last strings until they differ.
4. The common prefix found during this comparison will be the LCP for the entire array.

Why this works:
---------------
Sorting places strings with similar prefixes next to each other.
Hence, the first and last strings in the sorted list will reflect the maximum possible difference,
and their common prefix will be the prefix common to all strings.

Time Complexity: O(N log N + M)
    - O(N log N) for sorting the list (N is the number of strings).
    - O(M) to compare the first and last strings (M is the length of the shortest string).

Space Complexity: O(1)
    - No extra space apart from a few variables.

Example:
Input: ["flower", "flow", "flight"]
Output: "fl"
"""


def longest_common_prefix(strs):
    if not strs:
        return ""

    # Step 1: Sort the array of strings
    strs.sort()

    # Step 2: Take the first and last strings after sorting
    first = strs[0]
    last = strs[-1]
    prefix = ""

    # Step 3: Compare characters of first and last strings
    for i in range(min(len(first), len(last))):
        if first[i] == last[i]:
            prefix += first[i]
        else:
            break

    return prefix


# Example Usage
if __name__ == "__main__":
    words = ["flower", "flow", "flight"]
    print("Longest Common Prefix:", longest_common_prefix(words))

    words2 = ["dog", "racecar", "car"]
    print("Longest Common Prefix:", longest_common_prefix(words2))

    words3 = ["aeroplane", "aerospace", "aerodynamics"]
    print("Longest Common Prefix:", longest_common_prefix(words3))
