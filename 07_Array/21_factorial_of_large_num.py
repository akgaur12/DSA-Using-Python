"""
Problem: Factorial of a Large Number (Without Using BigInteger Libraries)
GFG Link: https://www.geeksforgeeks.org/dsa/factorial-large-number/

Description:
-------------
Compute the factorial of a large number `n` using an approach that simulates
manual multiplication by storing the result as a list of digits.

This approach is language-agnostic and works in environments where you don't
have support for arbitrary-precision integers (like in C/C++).

Approach:
----------
1. Initialize a list `res` with 1, where each index represents a digit.
2. Loop from 2 to n, multiplying each number with the number represented by `res`.
3. Use a helper function `multiply()` that multiplies a number with the current
   result stored in `res`, digit by digit (handling carry manually).
4. Finally, reverse the result list and join digits to form the final number.

Time Complexity: O(n * d), where d is the number of digits in the result.
Space Complexity: O(d), for storing digits of the factorial.

Example:
---------
Input:  n = 5
Output: 120

Input:  n = 25
Output: 15511210043330985984000000
"""

def multiply(x, res):
    """
    Multiplies an integer x with the number represented by the list res.

    Args:
        x (int): The multiplier.
        res (List[int]): The current factorial result stored as digits in reverse.

    Returns:
        List[int]: Updated list of digits after multiplication with x.
    """
    carry = 0
    for i in range(len(res)):
        prod = res[i] * x + carry
        res[i] = prod % 10          # Store the last digit of product
        carry = prod // 10          # Carry for next digits

    # Append remaining carry digits (if any)
    while carry:
        res.append(carry % 10)
        carry //= 10

    return res


def factorial(n):
    res = [1]  # Initialize result as [1], i.e., 0! = 1

    for x in range(2, n + 1):
        res = multiply(x, res)

    # Convert the reversed list of digits to string in correct order
    return ''.join(map(str, res[::-1]))


# Example usage
if __name__ == "__main__":
    n = 25
    print(f"{n}! = {factorial(n)}")
