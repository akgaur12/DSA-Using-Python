"""
Problem: Integer to Roman Numeral Conversion

Description:
------------
This script converts a given integer (between 1 and 3999) into its Roman numeral representation.
Roman numerals are composed using the following symbols and values:

Symbol   Value
----------------
M        1000
CM       900
D        500
CD       400
C        100
XC       90
L        50
XL       40
X        10
IX       9
V        5
IV       4
I        1

The function uses a greedy approach to subtract the largest possible Roman value at each step.

Constraints:
------------
- 1 ≤ num ≤ 3999

Time Complexity: O(1)
    - Constant time due to a fixed number of Roman numeral mappings.
Space Complexity: O(1)
    - Only a few variables used, no dynamic data structures.

Function:
---------
"""

def integer_to_roman(num):
    if not (1 <= num <= 3999):
        return "Input out of range (1 - 3999)"

    value_map = [
        (1000, 'M'), (900, 'CM'),
        (500, 'D'),  (400, 'CD'),
        (100, 'C'),  (90, 'XC'),
        (50, 'L'),   (40, 'XL'),
        (10, 'X'),   (9, 'IX'),
        (5, 'V'),    (4, 'IV'),
        (1, 'I')
    ]

    result = ""
    for val, symbol in value_map:
        while num >= val:
            result += symbol
            num -= val

    return result


# Example usage
if __name__ == "__main__":
    try:
        num_input = int(input("Enter integer (1 - 3999): "))
        roman_numeral = integer_to_roman(num_input)
        print("Roman numeral:", roman_numeral)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
