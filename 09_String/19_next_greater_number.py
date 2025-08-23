"""
Problem: Next Greater Number with Same Set of Digits

Description:
------------
Given a number as a string, the task is to find the next greater number 
formed by rearranging its digits. If no such arrangement exists 
(i.e., the number is the highest permutation of its digits), 
return "Not Possible".

Approach (Similar to Next Permutation algorithm):
-------------------------------------------------
1. Traverse the digits from right to left and find the first index `i` 
   where digits[i] < digits[i+1]. 
   - If no such index is found, the digits are in descending order, 
     so no larger number is possible.

2. Find the smallest digit on the right side of index `i` which is greater 
   than digits[i]. Call its index `j`.

3. Swap digits[i] and digits[j].

4. Reverse the sequence after index `i` (i+1 to end) 
   to get the smallest possible arrangement of those digits.

This guarantees the next greater number with the same set of digits.

Example:
--------
>>> nextGreaterNumber("218765")
'251678'

>>> nextGreaterNumber("1234")
'1243'

>>> nextGreaterNumber("4321")
'Not Possible'

>>> nextGreaterNumber("534976")
'536479'

Time Complexity:
----------------
O(n) - Single traversal and reversal.

Space Complexity:
-----------------
O(n) - For storing digits as a list.
"""

def nextGreaterNumber(num: str) -> str:
    digits = list(num)
    n = len(digits)

    # Step 1: Find first index 'i' from right such that digits[i] < digits[i+1]
    i = n - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1

    # If no such index found, number is highest permutation
    if i == -1:
        return "Not Possible"

    # Step 2: Find smallest digit on right side of i which is greater than digits[i]
    j = n - 1
    while digits[j] <= digits[i]:
        j -= 1

    # Step 3: Swap digits[i] and digits[j]
    digits[i], digits[j] = digits[j], digits[i]

    # Step 4: Reverse the part after index i
    digits[i + 1:] = reversed(digits[i + 1:])

    return "".join(digits)



# ✅ Example Usage
if __name__ == "__main__":
    print(nextGreaterNumber("218765"))  # Output: 251678
    print(nextGreaterNumber("1234"))    # Output: 1243
    print(nextGreaterNumber("4321"))    # Output: Not Possible
    print(nextGreaterNumber("534976"))  # Output: 536479
