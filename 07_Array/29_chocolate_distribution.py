"""
Problem: Chocolate Distribution Problem
GFG Link: https://www.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1

Description:
------------
Given an array `arr[]` of `n` integers where each value represents 
the number of chocolates in a packet. Each packet can have a different 
number of chocolates. There are `m` students, and the task is to 
distribute chocolate packets such that:

- Each student gets exactly one packet.
- The difference between the number of chocolates in the packet 
  with the maximum chocolates and the packet with the minimum chocolates 
  given to the students is minimized.

Approach: Sliding Window after Sorting
---------------------------------------
1. Sort the array of chocolates.
2. Use a window of size `m` (number of students).
3. Find the minimum difference between the maximum and minimum of each window.

Time Complexity: O(n log n) — due to sorting.
Space Complexity: O(1) — no extra space used.

Example:
---------
Input: arr = [7, 3, 2, 4, 9, 12, 56], m = 3  
Output: 2  
Explanation: The minimum difference is between packets with 3, 4, and 5 chocolates.
"""

def findMinDiff(arr, m):
    """
    Find the minimum difference between the maximum and minimum number of 
    chocolates among any subset of size `m`.

    Args:
        arr (List[int]): List of integers where each value represents chocolates in a packet.
        m (int): Number of students.

    Returns:
        int: Minimum difference between max and min chocolates distributed.
    """
    n = len(arr)
    if m == 0 or n == 0 or m > n:
        return 0

    # Step 1: Sort the given array
    arr.sort()

    minDiff = float('inf')

    # Step 2: Find the subarray of size m with the minimum difference
    for i in range(n - m + 1):
        diff = arr[i + m - 1] - arr[i]
        minDiff = min(minDiff, diff)

    return minDiff


# Example usage
if __name__ == "__main__":
    arr = [7, 3, 2, 4, 9, 12, 56]
    m = 3
    print("Minimum difference is:", findMinDiff(arr, m))  # Output: 2
