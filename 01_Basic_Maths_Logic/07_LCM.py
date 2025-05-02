import math

"""
Program to calculate the **Least Common Multiple (LCM)** of two positive integers.

The **LCM** of two numbers is the smallest positive number that is divisible by both.
Examples:
    LCM(4, 6) = 12
    LCM(10, 15) = 30

Time Complexity:
---------------
1. Brute Force (for-loop):         O(a * b)
2. Brute Force (optimized step):   O(a * b), but fewer steps than 1
3. GCD-based (efficient):          O(log(min(a, b))) due to Euclidean algorithm
"""


def lcm_for_loop(a, b):
    """
    Calculates the LCM using a for-loop starting from the max of a and b.

    Time Complexity: O(a * b)
    """
    if a == 0 or b == 0:
        return 0

    greater = max(a, b)

    for i in range(greater, a * b + 1, greater):
        if i % a == 0 and i % b == 0:
            return i


def lcm_optimized_step(a, b):
    """
    Calculates the LCM by incrementing in steps of the larger number
    until a multiple of the smaller number is found.

    Time Complexity: O(a * b)
    """
    if a == 0 or b == 0:
        return 0

    min_num = min(a, b)
    max_num = max(a, b)

    i = max_num

    while True:
        if i % min_num == 0:
            return i
        i += max_num


def lcm_by_gcd(a, b):
    """
    Calculates the LCM using the GCD formula:
    LCM(a, b) = abs(a * b) // GCD(a, b)

    Time Complexity: O(log(min(a, b)))
    """
    if a == 0 or b == 0:
        return 0

    return abs(a * b) // math.gcd(a, b)


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
            print("LCM (GCD Method):", lcm_by_gcd(a, b))
            # print("LCM (For Loop):", lcm_for_loop(a, b))
            # print("LCM (Optimized Step):", lcm_optimized_step(a, b))
        Test_Case -= 1

except ValueError:
    print("Invalid input! Please enter valid integers.")
