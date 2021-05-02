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
    primes = deque([n for n in range(2, limit)])
    while True:
        candidate = primes.popleft()
        if candidate > sqrt(limit):
            primes.append(candidate)
            return primes
        else:
            primes = deque([n for n in primes if n % candidate != 0])
            primes.append(candidate)

UNDER = 2 * 1000 * 1000
a = time()
solution = sum(primes(2*1000*1000))
b = time()

print(f'sum of primes smaller than {UNDER} is {solution} and it takes {b-a} seconds to solve it.')
# 142913828922, ~12 s
