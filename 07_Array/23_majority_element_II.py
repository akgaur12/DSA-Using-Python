"""
Problem: Find All Elements That Appear More Than n/3 Times
Leetcode Link: https://leetcode.com/problems/majority-element-ii/

Description:
-------------
Given an integer array `nums`, return all elements that appear more than ⌊ n/3 ⌋ times.
You may return the answer in **any order**.

Constraints:
-------------
- The array can contain negative or positive integers.
- It is guaranteed that the answer exists and is unique only if such numbers occur more than n//3 times.
- At most two elements can satisfy the condition (since 3*k > n implies k <= 2).

Example:
---------
Input:  nums = [3, 2, 3]
Output: [3]

Input: nums = [1, 1, 1, 3, 3, 2, 2, 2]
Output: [1, 2]

Approach:
---------
1. Use a dictionary (hash map) to count the frequency of each element.
2. Iterate through the frequency map and select elements whose count is greater than ⌊ n/3 ⌋.
3. Return those elements as a list.

Time Complexity:  O(n) — One pass to build the frequency map, another to collect results.
Space Complexity: O(n) — For storing the frequency of each number.
"""

def majorityElement(nums):
    freq_map = {}
    result = []

    # Step 1: Count frequency of each element
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    # Step 2: Collect elements that appear more than n/3 times
    for num in freq_map:
        if freq_map[num] > len(nums) // 3:
            result.append(num)
    
    return result


# Alternate version: using more Pythonic style with .items()
def majorityElement_alt(nums): 
    counter = {}
    results = []
    for num in nums:
        counter[num] = counter.get(num, 0) + 1

    # results = [key for key, value in counter.items() if value > len(nums) // 3]
    for key, value in counter.items():
            if value > len(nums) // 3:
                results.append(key)

    return results


# Example usage
if __name__ == "__main__":
    nums1 = [3, 2, 3]
    nums2 = [1, 1, 1, 3, 3, 2, 2, 2]

    print(majorityElement(nums1))       # Output: [3]
    print(majorityElement(nums2))       # Output: [1, 2]
    print(majorityElement_alt(nums2))   # Output: [1, 2]
