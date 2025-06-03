"""
Problem: Sort 0s, 1s and 2s  
GFG Link: https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1

Description:
Given an array consisting of only 0s, 1s, and 2s, sort the array in-place without using any sorting algorithm.

This is a variation of the Dutch National Flag problem.

Approach:
1. Count the number of 0s, 1s, and 2s in the array.
2. Overwrite the original array by placing all 0s first, followed by 1s, and then 2s.

Time Complexity: O(n)  
Space Complexity: O(1) — No extra space used apart from a few integer variables.
"""

def sort_012(arr):
    count0, count1, count2 = 0, 0, 0
    
    # Step 1: Count 0s, 1s, and 2s
    for n in arr:
        if n == 0:
            count0 += 1
        elif n == 1:
            count1 += 1
        else:
            count2 += 1
    
    # Step 2: Overwrite the original array with sorted 0s, 1s, and 2s
    i = 0
    while count0 > 0:
        arr[i] = 0
        i += 1
        count0 -= 1
        
    while count1 > 0:
        arr[i] = 1
        i += 1
        count1 -= 1
    
    while count2 > 0:
        arr[i] = 2
        i += 1
        count2 -= 1


# --------- Main Program ---------
if __name__ == "__main__":
    arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    sort_012(arr)
    print("Sorted array:", arr)
