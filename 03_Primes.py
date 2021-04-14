# Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt

def largest_prime_factor(n):
    # keep dividing it by zero until we reach an odd number
    while n % 2 == 0:
        n //= 2

    # if we get to 3 and smaller just return that
    if n <= 3:
        return n

    # otherwise keep dividing it with odd numbers
    for odd in range(3, int(sqrt(n)) + 1, 2):
        while n % odd == 0:
            max_prime = odd
            n //= odd
            if n == 1:
                return max_prime

input_num = 600851475143
print(f"The largest prime factor of {input_num} is {largest_prime_factor(input_num)}!")
