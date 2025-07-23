"""
Problem: Common Elements in Three Sorted Arrays
GFG Link: https://www.geeksforgeeks.org/problems/common-elements1132/1

Description:
------------
Given three sorted arrays, the task is to find all common elements 
present in all three arrays. The result should not contain duplicates.

Approach:
---------
- Use three pointers `i`, `j`, and `k` to traverse through arr1, arr2, and arr3.
- If all three elements at pointers match, add to the result.
- Skip duplicate values to avoid repeated entries.
- Increment the pointer of the array that has the smallest current value
  to align the sequences.

Time Complexity: O(n1 + n2 + n3)
    - Where n1, n2, n3 are the lengths of the three arrays.
    - We are traversing each array at most once.

Space Complexity: O(1) extra (excluding the result list)

"""

def commonElements(arr1, arr2, arr3):
    i, j, k = 0, 0, 0
    common = []

    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        # If all three elements are equal, add to result
        if arr1[i] == arr2[j] == arr3[k]:
            common.append(arr1[i])
            i += 1
            j += 1
            k += 1

            # Skip duplicates in all arrays
            while i < len(arr1) and arr1[i] == arr1[i - 1]:
                i += 1
            while j < len(arr2) and arr2[j] == arr2[j - 1]:
                j += 1
            while k < len(arr3) and arr3[k] == arr3[k - 1]:
                k += 1

        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1

    return common


# Example usage
if __name__ == "__main__":
    arr1 = [1, 5, 10, 20, 30]
    arr2 = [5, 13, 15, 20]
    arr3 = [5, 20]

    common = commonElements(arr1, arr2, arr3)
    if len(common) == 0:
        print(-1)
    else:
        print("Common elements:", *common)
