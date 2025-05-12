"""
Program: Sum of Cubes of First N Natural Numbers

Problem Statement:
------------------
Given an integer `n`, calculate the sum of the series:
    1³ + 2³ + 3³ + 4³ + ... + n³

Examples:
---------
Input:  n = 5
Output: 225
Explanation: 1³ + 2³ + 3³ + 4³ + 5³ = 225

Input:  n = 7
Output: 784
Explanation: 1³ + 2³ + 3³ + 4³ + 5³ + 6³ + 7³ = 784

Approach:
---------
This implementation uses a **recursive** approach where:
    sum_of_cubes(n) = n³ + sum_of_cubes(n - 1)

Time Complexity:
----------------
- Recursive Depth: O(n)
- Space Complexity (call stack): O(n)

Alternatively, a formula-based approach can be used:
    Sum = (n(n + 1)/2)²

Problem Link:
-------------
GFG: https://www.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1
"""


def sum_of_cubes(n):
    if n == 1:
        return 1
    return n**3 + sum_of_cubes(n - 1)


# --------- Main Program ---------
if __name__ == "__main__":
    try:
        n = int(input("Enter the number of terms: "))
        if n < 1:
            print("Please enter a positive integer.")
        else:
            print("Sum of cubes:", sum_of_cubes(n))
    except ValueError:
        print("Invalid input! Please enter an integer.")
