"""
Problem: Intersection of Two Arrays
Leetcode Link: https://leetcode.com/problems/intersection-of-two-arrays/description/

Description:
Given two arrays, return their intersection—that is, elements common to both arrays.
Each element in the result should appear only once (no duplicates).
The order of elements in the output corresponds to the order they appear in the second array.

Approach:
- Convert the first array into a set for O(1) membership checks.
- Iterate through the second array and for each element:
    - If it is present in the set, add it to the result and remove it from the set to avoid duplicates.
- Return the list of common elements.

Time Complexity:
- Converting arr1 to a set takes O(n) time, where n is the length of arr1.
- Iterating through arr2 takes O(m) time, where m is the length of arr2.
- Each membership check and removal in a set is O(1) on average.
- Overall time complexity: O(n + m)

Space Complexity:
- The set created from arr1 requires O(n) extra space.
- The output list requires O(min(n, m)) space in the worst case.
- Overall space complexity: O(n)

Example:
arr1 = [1, 2, 2, 3, 4, 5]
arr2 = [2, 3, 5, 6]
Output: [2, 3, 5]
"""

def intersection(arr1, arr2):
    ans = []
    arr1_set = set(arr1)  # Convert arr1 to set for efficient lookups
    
    for num in arr2:
        if num in arr1_set:
            ans.append(num)      # Add to result if present in arr1_set
            arr1_set.remove(num) # Remove to prevent duplicates in result

    return ans


# Example usage
arr1 = [1, 2, 2, 3, 4, 5]
arr2 = [2, 3, 5, 6]

print(intersection(arr1, arr2))  # Output: [2, 3, 5]
