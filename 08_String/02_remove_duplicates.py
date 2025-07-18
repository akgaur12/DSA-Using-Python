"""
Problem: Remove Duplicate Characters from a String

Description:
------------
Given a string `s`, remove all duplicate characters **while preserving the original order**
of characters.

Example:
--------
Input : "programming"  
Output: "progamin"

Approach:
---------
- Use a dictionary (`char_map`) to keep track of characters that have already been seen.
- Iterate through the string:
    - If a character hasn't been seen before, append it to the result and mark it as seen.
- Return the result as a joined string.

Time Complexity : O(n)  
    (where n is the length of the string; each character is visited once)

Space Complexity : O(k)  
    (where k is the number of unique characters in the string; due to the hashmap and result list)
"""


def remove_duplicates(s):
    char_map = {}       # Dictionary to track seen characters
    result = []         # List to store characters without duplicates

    for char in s:
        if char not in char_map:
            char_map[char] = True
            result.append(char)
    
    return ''.join(result)  # Convert list back to string


# Example Usage
if __name__ == "__main__":
    input_str = "programming"
    output_str = remove_duplicates(input_str)
    print("Original string:", input_str)
    print("After removing duplicates:", output_str)
