"""
Program: Reverse a String Using Recursion

Description:
------------
This program defines a recursive function that reverses a given string `s`.
The function works by recursively removing the first character and appending
it to the end of the reversed substring until the string is empty.

Approach:
---------
- Base Case: If the string is empty (len(s) == 0), return the empty string.
- Recursive Case: Reverse the substring starting from index 1 and append the first character at the end.

Time Complexity:
----------------
- O(n), where n is the length of the string, as each character is processed once.

Space Complexity:
-----------------
- O(n), due to the recursive call stack and string concatenation.

Example:
--------
Input: s = "hello"
Output: "olleh"
Explanation: The string is reversed recursively: "hello" → "olleh"

"""


def reverse_string(s):
    if len(s) <= 1: 
        return s
    return reverse_string(s[1:]) + s[0] 



# --------- Main Program ---------
if __name__ == "__main__":
    try:
        test_cases = int(input("Enter number of test cases: "))
        
        while test_cases:
            s = input("Enter a string: ")
            reversed_s = reverse_string(s)
            print(f"Reversed string: {reversed_s}")
            test_cases -= 1

    except ValueError:
        print("Invalid input! Please enter a valid number of test cases.")
