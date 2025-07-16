"""
Problem: Check if a String is a Palindrome

Description:
-------------
A palindrome is a string that reads the same forwards and backwards,
ignoring spaces and case differences.

Examples:
---------
- Input: "Madam"       → Output: True (palindrome)
- Input: "Step on no pets" → Output: True (palindrome)
- Input: "Hello"       → Output: False (not a palindrome)

Approach 1: Using String Reversal
---------------------------------
1. Remove all spaces.
2. Convert the string to lowercase.
3. Compare the string to its reverse.

Time Complexity: O(n)
Space Complexity: O(n) (due to string reversal)
"""

def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()
    
    # Compare string with its reverse
    return s == s[::-1]


# Example usage
string = "Madam"
if is_palindrome(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")


"""
Approach 2: Two-Pointer Technique
---------------------------------
1. Remove spaces and convert to lowercase.
2. Use two pointers from left and right ends of the string.
3. Compare characters and move inward.
4. If all corresponding characters match, the string is a palindrome.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def is_palindrome_two_pointer(s):
    # Preprocess: Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    
    left = 0
    right = len(s) - 1

    # Compare characters from both ends
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


# Example usage
string = "Madam"
if is_palindrome_two_pointer(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")
