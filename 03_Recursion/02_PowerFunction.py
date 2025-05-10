"""
Program: Calculate Power Using Recursion

Description:
------------
This program defines a recursive function to compute `x` raised to the power `n` (i.e., xⁿ),
where `x` is the base and `n` is a non-negative integer exponent.

Approach:
---------
- Base Case: If `n == 0`, return 1 (as any number raised to the power 0 is 1).
- Recursive Case: Multiply `x` by the result of `power(x, n - 1)`.

Time Complexity:
----------------
- O(n), where `n` is the exponent.

Space Complexity:
-----------------
- O(n) due to the recursive call stack.

Example:
--------
Input : x = 2, n = 3
Output: 8 (because 2³ = 2 × 2 × 2 = 8)
"""


def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)



# --------- Main Program ---------
if __name__ == "__main__":
    try:
        test_cases = int(input("Enter number of test cases: "))
        
        while test_cases:
            # Take the base and exponent as input for each test case
            x = int(input("Enter the base (x): "))
            n = int(input("Enter the exponent (n): "))
            
            # Handle the power calculation and print the result
            print(f"{x}^{n} =", power(x, n))
            
            test_cases -= 1

    except ValueError:
        print("Invalid input! Please enter integers for both base and exponent.")

