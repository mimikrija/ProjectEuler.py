# Smallest multiple
# Problem 5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from math import sqrt


def is_prime(num):
    return not any(num % divisor == 0 for divisor in range(2, int(sqrt(num)+1)))

def min_prime_factor(num):
    for n in range(2, num+1):
        if num % n == 0 and is_prime(n):
            return n

def min_missing_prime_divisor(solution, num):
    for n in range(2, num+1):
        if solution % n != 0:
            return min_prime_factor(n)

def smallest_multiple(num):
    "keeps multiplying solution with a missing divisor until it is evenly divisible by all numbers up to `num` including"
    solution = 1
    while True:
        missing = min_missing_prime_divisor(solution, num)
        if not missing:
            return solution
        else:
            solution *= missing



top = 20
print(f"The smallest positive number that is evenly divisible by all of the numbers from 1 to {top} is: {smallest_multiple(top)}")
# 232792560
