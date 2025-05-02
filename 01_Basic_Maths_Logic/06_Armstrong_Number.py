"""
Program to checks whether a number is an **Armstrong number**.

An **Armstrong number** (also called a narcissistic number) is a number that is equal
to the sum of its digits each raised to the power of the number of digits.

Examples:
    - 153 is an Armstrong number because: 1³ + 5³ + 3³ = 153
    - 9474 is an Armstrong number: 9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474
    - 123 is NOT an Armstrong number.

Time Complexity:
---------------
- Counting digits: O(log₁₀(n))
- Loop to extract digits and compute power: O(d) where d is number of digits
- Power calculation: each `d**digits` is O(log digits) (can vary by implementation)
- Total complexity is approximately: O(d × log d) ≈ O(log n × log log n)
"""

def count_digits(n):
    count = 0
    while n:
        count += 1
        n //= 10
    return count


def isArmstrong(n):
    num = n
    sum = 0
    digits = count_digits(num)

    # Calculate sum of each digit raised to the power of the total digits
    while num:
        d = num % 10
        sum += d ** digits
        num //= 10

    return sum == n


# --------- Main Program ---------
try:
    Test_Case = int(input("Enter Number of Test Cases: "))
    
    while Test_Case:
        n = int(input("Enter a number: "))
        if n < 0:
            print("Please enter a non-negative number.")
        else:
            print("Is Armstrong:", isArmstrong(n))
        Test_Case -= 1

except ValueError:
    print("Invalid input! Please enter an integer.")
