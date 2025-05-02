"""
Program to calculate the **Greatest Common Divisor (GCD)** of two positive integers.

The **GCD** of two numbers is the largest number that divides both numbers without a remainder.

Examples:
    GCD(12, 18) = 6
    GCD(100, 80) = 20

This script supports:
1. Brute-force approach
2. Euclidean Algorithm (iterative)
3. Euclidean Algorithm (recursive)

Time Complexity:
---------------
1. Brute-force method:            O(min(a, b))
2. Euclidean (iterative):        O(log(min(a, b)))
3. Euclidean (recursive):        O(log(min(a, b)))
"""

# Finds GCD using a brute-force method by checking from min(a, b) downward.
def gcd_brute_force(a: int, b: int) -> int:
    gcd = min(a, b)

    while gcd >= 1:
        if a % gcd == 0 and b % gcd == 0:
            return gcd
        gcd -= 1

    return 1


# Calculates GCD using the iterative Euclidean algorithm.
def gcd_euclidean_iterative(a: int, b: int) -> int:
    """
    The algorithm is based on the principle:
    GCD(a, b) = GCD(b, a % b)
    Repeats until b becomes 0.
    """
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


# Calculates GCD using the recursive Euclidean algorithm.
def gcd_euclidean_recursive(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd_euclidean_recursive(b, a % b)


# --------- Main Program ---------
try:
    Test_Case = int(input("Enter Number of Test Cases: "))

    while Test_Case:
        a_str, b_str = input("Enter two numbers separated by space: ").split()
        a = int(a_str)
        b = int(b_str)

        if a <= 0 or b <= 0:
            print("Please enter positive integers only.")
        else:
            # print("GCD (Brute Force):", gcd_brute_force(a, b))
            # print("GCD (Iterative Euclidean):", gcd_euclidean_iterative(a, b))
            print("GCD (Recursive Euclidean):", gcd_euclidean_recursive(a, b))

        Test_Case -= 1

except ValueError:
    print("Invalid input! Please enter valid integers.")
