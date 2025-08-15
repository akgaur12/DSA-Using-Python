"""
Pattern Printing: Palindromic Number Pyramid

Description:
------------
This function prints a **palindromic number pyramid** pattern. 
Each row is symmetrical, with decreasing and then increasing numbers centered by spaces.

Structure:
----------
- The pyramid has 'n' rows.
- Each row 'i' consists of numbers:
  - Decreasing from i to 1
  - Then increasing from 2 to i
- Rows are center-aligned using leading spaces.

Example (n = 5):
        1
      2 1 2
    3 2 1 2 3
  4 3 2 1 2 3 4
5 4 3 2 1 2 3 4 5

Time Complexity: O(n²)
    - Nested loops iterate over approximately n² elements.
    
Space Complexity: O(1)
    - Only counters and fixed space used.
"""

def palindromic_number_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        print("  " * (n - i), end="")

        # Print decreasing numbers from i to 1
        for j in range(i, 0, -1):
            print(j, end=" ")

        # Print increasing numbers from 2 to i
        for j in range(2, i + 1):
            print(j, end=" ")

        print()


# Example usage
if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    palindromic_number_pyramid(n)
