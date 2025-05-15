"""
Program: Linear Search (Sequential Search) in a List

Description:
------------
The linear search algorithm checks each element of the list sequentially until the target is found or the end of the list is reached.

Approach:
---------
- Iterate through the list from index 0 to len(arr) - 1.
- Compare each element with the target.
- If a match is found, return the current index.
- If the end is reached without a match, return -1.

Time Complexity:
----------------
- Best Case: O(1)    → Target is at the beginning.
- Worst Case: O(n)   → Target is at the end or not present.
- Average Case: O(n)

Space Complexity:
-----------------
- O(1), as no extra space is used.

Example:
--------
Input : arr = [4, 2, 7, 1, 9], target = 7  
Output: 2  (7 is at index 2)
"""


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# --------- Example Usage ---------
if __name__ == "__main__":
    arr = [4, 2, 7, 1, 9]
    target = 7
    index = linear_search(arr, target)

    if index != -1:
        print(f"Target found at index {index}")
    else:
        print("Target not found in the list")
