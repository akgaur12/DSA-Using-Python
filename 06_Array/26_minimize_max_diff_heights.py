"""
Problem: Minimize the Maximum Difference Between Heights
GFG Link: https://www.geeksforgeeks.org/problems/minimize-the-heights3351/1

Description:
------------
Given an array `arr[]` representing the heights of towers and an integer `k`, 
you can either increase or decrease each height by `k`. The task is to 
**minimize the maximum difference** between the heights after modification.

Constraints:
------------
- Each tower's height should remain non-negative after modification.
- You may either increase or decrease the height of a tower by `k`.

Approach:
---------
1. Sort the array of heights.
2. The initial difference (without any modification) is `arr[n-1] - arr[0]`.
3. For each tower index `i` from 1 to n-1:
    - We assume:
        - All towers from index `0` to `i-1` are increased by `k`.
        - All towers from index `i` to `n-1` are decreased by `k`.
    - Calculate:
        - `minH` = min of modified first and current tower.
        - `maxH` = max of modified previous tower and last tower.
    - Update result if `maxH - minH` is smaller than current result.

Time Complexity: O(n log n) (due to sorting)
Space Complexity: O(1)

Example:
--------
Input  : arr = [12, 6, 4, 15, 17, 10], k = 6  
Output : 11  
Explanation: After modification, the difference between tallest and shortest tower is minimized to 11.
"""

def getMinDiff(arr, k):
    n = len(arr)
    arr.sort()  # Step 1: Sort the array

    # Step 2: Initialize the result with current max difference
    res = arr[n - 1] - arr[0]

    # Step 3: Traverse and try modifying from 0 to i-1 and i to n-1
    for i in range(1, n):
        # Skip if decreasing this height by k results in negative
        if arr[i] - k < 0:
            continue

        # Calculate min and max heights after hypothetical modification
        minH = min(arr[0] + k, arr[i] - k)
        maxH = max(arr[i - 1] + k, arr[n - 1] - k)

        # Update result with smaller difference
        res = min(res, maxH - minH)
    
    return res


# --------- Example Usage ---------
if __name__ == "__main__":
    k = 6
    arr = [12, 6, 4, 15, 17, 10]
    ans = getMinDiff(arr, k)
    print("Minimum possible difference:", ans)  # Output: 11
