"""
Program: Calculate the n-th Fibonacci Number (Recursive Approach)

Problem Statement:
------------------
The Fibonacci sequence is defined as:
    F(0) = 0
    F(1) = 1
    F(n) = F(n - 1) + F(n - 2), for n > 1

Problem Link: https://leetcode.com/problems/fibonacci-number/description/

Given an integer `n`, compute F(n).

Examples:
---------
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1

Input: n = 6
Output: 8
Explanation: 0, 1, 1, 2, 3, 5, 8 → F(6) = 8

Approach:
---------
This implementation uses a **recursive** approach that directly follows
the mathematical recurrence relation.

Time Complexity:
----------------
- Exponential: O(2^n), due to repeated calculations.

Space Complexity:
-----------------
- O(n) call stack depth in the worst case.
"""


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# --------- Main Program ---------
if __name__ == "__main__":
    try:
        Test_Case = int(input("Enter Number of Test Cases: "))

        while Test_Case:
            n = int(input("Enter a number: "))
            if n < 0:
                print("Please enter a non-negative number.")
            else:
                 print(f"F({n}) =", fibonacci(n))
            Test_Case -= 1

    except ValueError:
        print("Invalid input! Please enter an integer.")

