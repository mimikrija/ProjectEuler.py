# 10001st prime
# Problem 7

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?
import time
import math

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

counter = 1
solution = 1
start = time.time()
while counter < 10001:
    solution +=2
    if is_prime(solution):
        counter += 1
end = time.time()

print (counter, "-th prime is ", solution )
print ("total solution time: ", end-start)
