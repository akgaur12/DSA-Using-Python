"""
Problem: Smallest Subarray with Sum Greater Than X
Leetcode Link: https://leetcode.com/problems/minimum-size-subarray-sum/description/

Description:
-------------
Given an array of positive integers and a number `x`, 
find the length of the **smallest contiguous subarray** whose sum is strictly **greater than `x`**. 
If no such subarray exists, return 0.

Constraints:
-------------
- All elements in the array are positive integers.
- Time complexity should be better than O(n²), ideally O(n).

Approach: Sliding Window Technique
-----------------------------------
1. Use two pointers (`i` and `j`) to define a window [i, j).
2. Expand the window by moving `j` to the right while the current sum is ≤ `x`.
3. Once the sum exceeds `x`, try shrinking the window from the left by moving `i` to find a smaller window.
4. Keep track of the minimum length that satisfies the condition.

Time Complexity:  O(n)  
Space Complexity: O(1)

Example:
---------
Input:  arr = [1, 4, 45, 6, 10, 19], x = 51  
Output: 3  
Explanation: The subarray [4, 45, 6] has sum = 55 > 51.
"""

def smallestSubWithSum(x, arr):
    i, j = 0, 0
    total = 0
    min_len = float('inf')

    while j < len(arr):
        # Expand the window by moving `j`
        while j < len(arr) and total <= x:
            total += arr[j]
            j += 1

        # Shrink the window by moving `i` while total > x
        while i < j and total > x:
            min_len = min(min_len, j - i)
            total -= arr[i]
            i += 1

    return 0 if min_len == float('inf') else min_len


# Example usage
if __name__ == "__main__":
    arr = [1, 4, 45, 6, 10, 19]
    x = 51
    print(smallestSubWithSum(x, arr))  # Output: 3 (e.g., subarray: [4, 45, 6])
