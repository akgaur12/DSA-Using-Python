"""
Program: Interpolation Search in a Sorted List

Description:
------------
This program implements the **interpolation search algorithm**, which is an improved
variant of binary search. It works best when the values in the array are **uniformly distributed**.
Instead of always probing the middle element like binary search, it estimates the position
of the target based on its value relative to the low and high ends of the array.

Note:
-----
- The array must be sorted in ascending order.
- If the array is not sorted, the result will be incorrect.
- Works best with uniformly distributed data.

Approach:
---------
1. Initialize two pointers: `low` (start of array) and `high` (end of array).
2. While `target` is between `arr[low]` and `arr[high]`:
    - Estimate position using the interpolation formula:
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
    - If `arr[pos] == target` → return pos.
    - If `arr[pos] < target`  → move `low` to `pos + 1`.
    - If `arr[pos] > target`  → move `high` to `pos - 1`.
3. If not found, return -1.

Time Complexity:
----------------
- Best Case: O(1)
- Average Case: O(log log n) — for uniformly distributed data
- Worst Case: O(n) — for non-uniform distributions or skewed data

Space Complexity:
-----------------
- O(1), as it is an iterative approach.

Example:
--------
Input : arr = [10, 20, 30, 40, 50], target = 30  
Output: 2 (30 is at index 2)
"""


def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        # Avoid division by zero
        if arr[high] == arr[low]:
            if arr[low] == target:
                return low
            else:
                return -1

        # Estimate the probable position of the target
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))

        # Check if estimated position is within bounds
        if pos >= len(arr):
            return -1

        if arr[pos] == target:
            return pos
        elif target > arr[pos]:
            low = pos + 1
        else:
            high = pos - 1

    return -1


# --------- Example Usage ---------
if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    target = 30
    index = interpolation_search(arr, target)
    if index != -1:
        print(f"Target found at index {index}")
    else:
        print("Target not found in the list")
