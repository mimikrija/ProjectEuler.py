# Summation of primes
# Problem 10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# # Find the sum of all the primes below two million.

from math import floor, sqrt
from itertools import islice
from time import time


def prime_generator(limit):
    for prime in (2, 3, 5, 7):
        yield prime

    while prime < limit:
        prime += 2
        if any(prime % divisor == 0 for divisor in range(3, floor(sqrt(prime) + 1))):
            pass
        else:
            yield prime

UNDER = 2 * 1000 * 1000
pr = prime_generator(UNDER)
a = time()
solution = sum(prime for prime in islice(pr, None))
b = time()
print(f'sum of primes smaller than {UNDER} is {solution} and it takes {b-a} seconds to solve it.')
# 142913828922, ~20 s

