"""
Problem: Count the number of vowels, consonants, digits, and special characters in a given string.

Approach 1: Using Built-in Functions
------------------------------------
- Use string methods like:
    - isalpha(): to check if character is an alphabet
    - isdigit(): to check if character is a digit
    - isspace(): to skip spaces
- Use a predefined set of vowels for easy checking.

Approach 2: Using ASCII Values
------------------------------
- Use ASCII ranges to manually classify characters:
    - Uppercase letters: 65–90
    - Lowercase letters: 97–122
    - Digits: 48–57
    - Space: 32 (ignored)
    - Anything else: considered a special character

Time Complexity: O(n) for both
Space Complexity: O(1) (only counters are used)
"""


# Approach 1: Using built-in methods
def count_characters_builtin(string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    digit_count = 0
    special_count = 0

    for char in string:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
        elif char.isdigit():
            digit_count += 1
        elif not char.isspace():  # skip whitespace
            special_count += 1

    print("[Built-in Approach]")
    print("Vowels:", vowel_count)
    print("Consonants:", consonant_count)
    print("Digits:", digit_count)
    print("Special characters:", special_count)



# Approach 2: Using ASCII values
def count_characters_ascii(string):
    vowels_list = ['a', 'e', 'i', 'o', 'u',
                   'A', 'E', 'I', 'O', 'U']

    vowel_count = 0
    consonant_count = 0
    digit_count = 0
    special_count = 0

    for char in string:
        ascii_val = ord(char)

        if (65 <= ascii_val <= 90) or (97 <= ascii_val <= 122):  # A-Z or a-z
            if char in vowels_list:
                vowel_count += 1
            else:
                consonant_count += 1
        elif 48 <= ascii_val <= 57:  # 0-9
            digit_count += 1
        elif ascii_val != 32:  # not space
            special_count += 1

    print("[ASCII Approach]")
    print("Vowels:", vowel_count)
    print("Consonants:", consonant_count)
    print("Digits:", digit_count)
    print("Special characters:", special_count)


# Example usage
input_str = "Hello World! 123"
print("Input string:", input_str)
count_characters_builtin(input_str)
print()
count_characters_ascii(input_str)
