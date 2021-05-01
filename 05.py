# Smallest multiple
# Problem 5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from math import sqrt


def min_factor(num):
    for n in range(2, num+1):
        if num % n == 0:
            return n

def min_missing_divisor(solution, num):
    for n in range(2, num+1):
        if solution % n != 0:
            return min_factor(n)

def smallest_multiple(num):
    "keeps multiplying solution with a missing divisor until it is evenly divisible by all numbers up to `num` including"
    solution = 1
    while True:
        missing = min_missing_divisor(solution, num)
        if not missing:
            return solution
        else:
            solution *= missing



top = 20
print(f"The smallest positive number that is evenly divisible by all of the numbers from 1 to {top} is: {smallest_multiple(top)}")
# 232792560
