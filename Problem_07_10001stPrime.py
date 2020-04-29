# 10001st prime
# Problem 7

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?
import time

def is_prime(candidate):
    if candidate > 3 and candidate%2 == 0:
        return False
    for divisor in range(3,candidate):
        if candidate%divisor == 0:
            return False
    return True

counter = 0
solution = 1
start = time.time()
while counter < 10001:
    solution +=1
    if is_prime(solution):
        counter += 1
end = time.time()

print (counter, "-th prime is ", solution )
print ("total solution time: ", end-start)
