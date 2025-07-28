"""
Problem: Roman to Integer Conversion

Description:
------------
This function converts a Roman numeral string (e.g., "XIV") into its corresponding integer value (e.g., 14).

Roman numerals are based on these symbol-value pairs:
    I = 1,    V = 5,    X = 10,   L = 50,   C = 100,  D = 500,  M = 1000

Some combinations involve subtraction:
    IV = 4 (5 - 1), IX = 9 (10 - 1), XL = 40 (50 - 10),
    XC = 90 (100 - 10), CD = 400 (500 - 100), CM = 900 (1000 - 100)

The algorithm iterates over the string from left to right.
- If the current value is less than the next one, it is subtracted.
- Otherwise, it is added.

Time Complexity:
----------------
O(n), where n is the length of the Roman numeral string.

Space Complexity:
-----------------
O(1), constant space.

"""

def roman_to_integer(s):
    try:
        roman_map = {
            'I': 1,   'V': 5,    'X': 10,
            'L': 50,  'C': 100,  'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        for char in reversed(s):  # Traverse from right to left
            value = roman_map[char]
            if value < prev_value:
                total -= value  # subtract if smaller than next numeral
            else:
                total += value  # otherwise, add
            prev_value = value

        return total
    except Exception as e:
        return f"Error: Please ensure the input is a valid Roman numeral string."

# Example usage
if __name__ == "__main__":
    roman_input = input("Enter a Roman numeral: ").upper()
    print("Integer value:", roman_to_integer(roman_input))
