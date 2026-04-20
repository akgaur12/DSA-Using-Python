"""
Program to find all the **factors** of a given positive integer.

A **factor** of a number `n` is any number that divides `n` exactly (no remainder).
For example:
    - Factors of 6: [1, 2, 3, 6]
    - Factors of 10: [1, 2, 5, 10]

This script handles multiple test cases and prints the list of all factors for each input.


Approaches Explained:
--------------------

1. Brute Force Approach (factors)
--------------------------------
- Iterates from 1 to n//2.
- If `i` divides `n`, it is added to the list.
- Finally, `n` itself is added as a factor.

Why n//2?
- No number greater than n//2 (except n) can divide n.

Time Complexity:
- O(n)

Space Complexity:
- O(k), where k = number of factors


2. Optimized Approach using √n (factors_optimized)
-------------------------------------------------
- Iterates only up to √n.
- If `i` is a factor, then `n//i` is also a factor.
  (Factors always come in pairs)

Example:
    n = 36
    (1,36), (2,18), (3,12), (4,9), (6,6)

- Uses a set to avoid duplicates.
- Finally returns sorted result.

Time Complexity:
- O(√n)

Space Complexity:
- O(k)

Why faster?
- Instead of checking all numbers up to n, we only check up to √n.


3. Optimized Generator Approach (factors_gen_optimized)
------------------------------------------------------
- Same √n logic as above, but memory efficient.
- Stores:
    small → stores smaller factors (ascending)
    large → stores larger factors (descending order initially)

    - small factors (≤ √n)
    - large factors (> √n)
- Yields values instead of storing full list.

Steps:
- Iterate till √n
- Add `i` to small list
- Add `n//i` to large list (if different)
- Yield small list first, then reversed large list

Benefits:
- Uses less memory (lazy evaluation)
- Produces sorted output without extra sorting

Time Complexity:
- O(√n)

Space Complexity:
- O(√n) (for temporary storage)


Final Takeaway:
---------------
- Brute force is simple but slow → O(n)
- √n approach is optimal → O(√n)
- Generator approach is best when memory matters
"""
import math


def factors(n):
    f = []
    
    # Check all numbers from 1 to n//2
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            f.append(i)  # i is a factor

    f.append(n)  # n is always a factor of itself
    return f


def factors_optimized(n):
    result = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n // i)
    return sorted(result)


def factors_gen_optimized(n):
    small, large = [], []
    
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            small.append(i)
            if i != n // i: # This condition prevents duplicate factors when n is a perfect square
                large.append(n // i)
    
    for x in small:
        yield x
    for x in reversed(large):
        yield x



# --------- Main Program ---------
try:
    Test_Case = int(input("Enter Number of Test Cases: "))

    while Test_Case:
        n = int(input("Enter a number: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            print("Factors:", factors(n))
        Test_Case -= 1

except ValueError:
    print("Invalid input! Please enter an integer.")
