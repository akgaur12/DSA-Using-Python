"""
Problem: Check if one array is a subset of another
GFG Link: https://www.geeksforgeeks.org/problems/array-subset-of-another-array2317/1

Description:
------------
Given two arrays `arr1` and `arr2`, determine whether `arr2` is a subset of `arr1`.
That is, check if every element of `arr2` appears in `arr1`.

Example:
--------
arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 3]      -> Output: Yes
arr3 = [2, 6]      -> Output: No
"""

# --- Approach 1: Brute-force with nested loops ---
def is_subset_brute_force(arr1, arr2):
    """
    Check if arr2 is a subset of arr1 using nested loops.
    Time Complexity: O(m * n)
    Space Complexity: O(1)
    where n = len(arr1), m = len(arr2)
    """
    for i in range(len(arr2)):
        found = False
        for j in range(len(arr1)):
            if arr2[i] == arr1[j]:
                found = True
                break
        if not found:
            return False
    return True


# --- Approach 2: Using Python's 'in' keyword ---
def is_subset_in_operator(arr1, arr2):
    """
    Check if arr2 is a subset of arr1 using 'in' keyword.
    Time Complexity: O(m * n)
    Space Complexity: O(1)
    Note: Internally performs a linear search for each element.
    """
    for item in arr2:
        if item not in arr1:
            return False
    return True


# --- Approach 3: Using Hash Set ---
def is_subset_hashset(arr1, arr2):
    """
    Check if arr2 is a subset of arr1 using a hash set.
    Time Complexity: O(n + m)
    Space Complexity: O(n)
    where n = len(arr1), m = len(arr2)

    This is the most efficient approach among the three.
    """
    hash_set = set(arr1)

    for num in arr2:
        if num not in hash_set:
            return False
    return True


# --- Example Usage ---
if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 3]
    arr3 = [2, 6]

    print("Brute Force:", is_subset_brute_force(arr1, arr2))   # True
    print("In Operator:", is_subset_in_operator(arr1, arr2))   # True
    print("HashSet:", is_subset_hashset(arr1, arr2))           # True

    print("Brute Force:", is_subset_brute_force(arr1, arr3))   # False
    print("In Operator:", is_subset_in_operator(arr1, arr3))   # False
    print("HashSet:", is_subset_hashset(arr1, arr3))           # False
