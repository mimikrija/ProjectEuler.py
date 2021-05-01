# 10001st prime
# Problem 7

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

from math import floor, sqrt
from itertools import islice


def prime_generator():
    for prime in (2, 3, 5, 7):
        yield prime

    while True:
        prime += 2
        if any(prime % divisor == 0 for divisor in range(3, floor(sqrt(prime) + 1))):
            pass
        else:
            yield prime

def prime(count):
    pr = prime_generator()
    return next(islice(pr, count-1, count))


n = 10001
print(f'{n}-th prime is {prime(n)}!')
# 104743
