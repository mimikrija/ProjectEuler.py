# Summation of primes
# Problem 10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# # Find the sum of all the primes below two million.

from math import floor, sqrt
from itertools import islice
from time import time
from collections import deque

# Sieve of Erathosten
# eliminate all composites below N to get a list of primes

def primes(limit):
    # eliminate even numbers greater than 2
    primes = {n: False for n in range(3, limit, 2)}
    primes[2] = False
    for n in range(3, floor(sqrt(limit)+1), 2):
        for p in range(2*n, limit, n):
            # cross out multiples of n
            primes[p] = True
    return sum(p for p, crossed_out in primes.items() if not crossed_out)


UNDER = 2 * 1000 * 1000
a = time()
solution = primes(UNDER)
b = time()

print(f'sum of primes smaller than {UNDER} is {solution} and it takes {b-a} seconds to solve it.')
# 142913828922, ~2.5 s
