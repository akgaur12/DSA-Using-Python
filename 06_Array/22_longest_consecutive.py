"""
Problem: Longest Consecutive Subsequence
GFG Link: https://www.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1

Description:
-------------
Given an unsorted array of integers, find the length of the longest
consecutive elements sequence.

A consecutive sequence is a sequence where the elements can be arranged
in increasing order such that each element appears exactly once and the
difference between adjacent elements is 1.

Examples:
----------
Input:  [2, 6, 1, 9, 4, 5, 3]
Output: 6  # Sequence: [1, 2, 3, 4, 5, 6]

Constraints:
-------------
- Time complexity should ideally be O(n).
- The array can contain duplicates.


Approach 1: Sorting Based
-------------------------
1. Sort the array.
2. Traverse the sorted array, skipping duplicates.
3. If the current number is 1 greater than the previous, increase count.
4. Else, reset count to 1.
5. Keep track of the maximum count.

Time Complexity: O(n log n) due to sorting.
Space Complexity: O(1) extra space (ignoring sort space).


Approach 2: HashSet Based (Optimal)
-----------------------------------
1. Insert all elements into a set.
2. For each element, check if it's the start of a sequence (val - 1 not in set).
3. If it is, count the length of the sequence and remove visited elements.
4. Update the result with the maximum length found.

Time Complexity: O(n)
Space Complexity: O(n)

Why we remove visited elements:
- To avoid recomputation.
- Ensures each element is processed only once.

"""

def longestConsecutive_sorting(arr):
    if not arr:
        return 0

    arr.sort()
    res = 1
    cnt = 1

    for i in range(1, len(arr)): 
        if arr[i] == arr[i - 1]:
            continue
        elif arr[i] == arr[i - 1] + 1:
            cnt += 1
        else:
            cnt = 1
        res = max(res, cnt)

    return res


def longestConsecutive_hashset(arr):
    st = set(arr)
    res = 0

    for val in arr:
        if val - 1 not in st:  # Start of a sequence
            cur = val
            cnt = 0
            while cur in st:
                st.remove(cur)
                cur += 1
                cnt += 1
            res = max(res, cnt)

    return res


# Example usage
if __name__ == "__main__":
    arr = [2, 6, 1, 9, 4, 5, 3]
    print("Sorting Approach:", longestConsecutive_sorting(arr))      # Output: 6
    print("HashSet Approach:", longestConsecutive_hashset(arr))      # Output: 6
