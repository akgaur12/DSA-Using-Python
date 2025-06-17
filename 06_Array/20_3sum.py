"""
Problem: Find the Triplet that Sum to a Given Value

Description:
-------------
Given an array of integers `arr` and an integer `target`, determine whether there exists a **triplet (i, j, k)**
such that `arr[i] + arr[j] + arr[k] == target`.

Return `True` if such a triplet exists, otherwise return `False`.

Examples:
---------
Input: arr = [12, 3, 4, 1, 6, 9], target = 24
Output: True
Explanation: There is a triplet (12, 3, 9) which adds to 24

Input: arr = [1, 2, 3, 4, 5], target = 50
Output: False

Approach 1: Brute Force (Three Nested Loops)
--------------------------------------------
- Check every possible triplet (i, j, k) where i < j < k and see if their sum is equal to the target.

Time Complexity: O(N^3)
Space Complexity: O(1)


Approach 2: Sorting + Two Pointers
------------------------------------
- Sort the array.
- Fix one element (arr[i]) and use two pointers to find if a pair exists in the remaining array that sums to (target - arr[i]).

Time Complexity: O(N^2) for loop and two-pointer traversal
Space Complexity: O(1)
"""

# -------------------- Approach 1: Brute Force -------------------- 
def hasTripletSum_brute_force(arr, target):
    n = len(arr)
    
    # Try all combinations of three elements
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == target:
                    return True
    return False


# -------------------- Approach 2: Sorting + Two Pointers -------------------- 
def hasTripletSum_two_pointers(arr, target):
    n = len(arr)
    arr.sort()
    
    for i in range(n - 2):
        # Initialize two pointers
        l, r = i + 1, n - 1
        requiredSum = target - arr[i]
        
        while l < r:
            curr_sum = arr[l] + arr[r]
            if curr_sum == requiredSum:
                return True
            elif curr_sum < requiredSum:
                l += 1
            else:
                r -= 1
    return False


# -------------------- Example Usage -------------------- #
if __name__ == "__main__":
    arr = [12, 3, 4, 1, 6, 9]
    target = 24

    print("Brute Force:", hasTripletSum_brute_force(arr, target))   # True
    print("Two Pointers:", hasTripletSum_two_pointers(arr, target)) # True

    arr2 = [1, 2, 3, 4, 5]
    target2 = 50
    print("Brute Force:", hasTripletSum_brute_force(arr2, target2))   # False
    print("Two Pointers:", hasTripletSum_two_pointers(arr2, target2)) # False
