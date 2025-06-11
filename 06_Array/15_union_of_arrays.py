"""
Problem: Find Union of Two Arrays

Description:
Given two arrays, find their union — the set of all unique elements present in either array.

Approach 1: Using a Set (Order Not Preserved)
- Insert all elements from both arrays into a Python set.
- Since sets automatically discard duplicates, this yields the union.
- Time Complexity: O(n + m), where n and m are lengths of the two arrays.
- Space Complexity: O(n + m) for the set.
- Note: The order of elements in the result is not guaranteed because sets are unordered.

Approach 2: Using a Set While Preserving Order
- Iterate through both arrays sequentially.
- Maintain a set to keep track of elements already added.
- Add an element to the result only if it hasn’t been seen before.
- Time Complexity: O(n + m), where n and m are lengths of the two arrays.
- Space Complexity: O(n + m) for the set and output list.
- This ensures the relative order of elements from the input arrays is preserved.

Example: 
Input:
    a = [1, 2, 3, 4]
    b = [3, 4, 5, 6]

Output:
    Union (order not guaranteed): [1, 2, 3, 4, 5, 6]
    Union (order preserved): [1, 2, 3, 4, 5, 6]
"""


def find_union(a, b):
    union = set()

    for item in a:
        union.add(item)

    for item in b:
        union.add(item)

    return list(union)


def union_preserve_order(arr1, arr2):
    seen = set()
    union = []

    for num in arr1 + arr2:
        if num not in seen:
            seen.add(num)
            union.append(num)

    return union


# Example usage:
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

print("Union (order not guaranteed):", find_union(a, b))
print("Union (order preserved):", union_preserve_order(a, b))

