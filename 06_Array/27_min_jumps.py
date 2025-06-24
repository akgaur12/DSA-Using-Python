"""
Problem: Minimum Number of Jumps to Reach End of Array

Description:
-------------
Given an array `arr[]` of N integers where each element represents 
the maximum number of steps that can be jumped forward from that element, 
write a function to return the **minimum number of jumps** to reach 
the end of the array (starting from index 0).

If the end isn't reachable, return -1.

Approach:
---------
This uses a **Greedy Algorithm**:
1. Initialize:
   - `jumps` = 1 (first jump from index 0)
   - `farthest` = arr[0] (farthest index reachable so far)
   - `current_end` = arr[0] (end of current jump range)

2. Traverse the array from index 1 to N-1:
   - If `i > farthest`, return -1 (not reachable).
   - Update `farthest` as the max of current `farthest` and `i + arr[i]`.
   - If `i == current_end`, increase jump count and update `current_end`.

Edge Cases:
-----------
- If the array has only one element, zero jumps are needed.
- If the first element is 0, and length > 1, you can't move — return -1.

Time Complexity: O(n)
Space Complexity: O(1)

Example:
---------
Input: arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]  
Output: 3  
Explanation: Path = 1 → 3 → 8 → 9 (3 jumps)
"""

def min_jumps(arr):
    n = len(arr)
    
    # Edge cases
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1

    # Initialize variables
    jumps = 1
    farthest = arr[0]
    current_end = arr[0]

    for i in range(1, n):
        if i > farthest:
            return -1  # Not reachable

        farthest = max(farthest, i + arr[i])

        if i == current_end and i != n - 1:
            jumps += 1
            current_end = farthest

    return jumps


# -------- Example Usage --------
if __name__ == "__main__":
    arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    print("Minimum number of jumps:", min_jumps(arr))  # Output: 3
