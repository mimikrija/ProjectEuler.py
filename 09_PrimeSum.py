# Summation of primes
# Problem 10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# # Find the sum of all the primes below two million.

import math
import time

def is_prime(candidate):
    if candidate == 1:
        return False # 1 is not a prime
    if candidate < 4:
        return True # but all other numbers less than 4 are
    if candidate%2 == 0:
        return False # all other primes are odd (except 2 which is handle by the above case)
    if candidate < 9:
        return True # which leaves us with 5 and 7
    for divisor in range(3,math.floor(math.sqrt(candidate))+1):
        # divisibility by 2 was already eliminated above,
        # we can only check up until sqrt(candidate)+1
        if candidate%divisor == 0:
            return False
    return True

start = time.time()
solution = 0
for potential_prime in range(1,2000000):
    if is_prime(potential_prime):
        solution += potential_prime
end = time.time()

print("sum of all primes below two million is: ", solution)
print ("total solution time: ", end-start)
