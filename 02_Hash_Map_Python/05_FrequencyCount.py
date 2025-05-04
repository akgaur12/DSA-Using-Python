"""
Problem: Frequencies in a Limited Array
--------
You are given an array arr[] containing positive integers. 
The elements in the array arr[] range from 1 to n (where n is the size of the array), 
and some numbers may be repeated or absent. 

Your task is to count the frequency of all numbers in the range 1 to n and return 
an array of size n such that result[i] represents the frequency of the number (i+1)

GFG Problem Link: https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/0

Example:
--------
Input:  arr = [2, 3, 2, 3, 5]
Output: [0, 2, 2, 0, 1]
Explanation: 
- 1 occurs 0 times
- 2 occurs 2 times
- 3 occurs 2 times
- 4 occurs 0 times
- 5 occurs 1 time

Time Complexity:
----------------
- O(n), where n is the length of the array
"""


def frequencyCount(arr):
    n = len(arr)
    
    # Initialize all frequencies to 0
    freq_map = {i: 0 for i in range(1, n + 1)} 

    # Count frequency only for numbers in range 1 to n
    for i in arr:
        freq_map[i] = freq_map.get(i, 0) + 1

    # Prepare the result in order from 1 to n
    ans = [freq_map[i] for i in freq_map]

    return ans


# --------- Example Usage ---------
arr = [2, 3, 2, 3, 5]
print("Frequency Count:", frequencyCount(arr))
