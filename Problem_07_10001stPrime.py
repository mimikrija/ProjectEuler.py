# 10001st prime
# Problem 7

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

def is_prime(candidate):
    for divisor in range(2,candidate):
        if candidate%divisor == 0:
            return False
    return True

counter = 0
candidate = 1
while counter < 10001:
    candidate +=1
    if is_prime(candidate):
        counter += 1

print (counter, "-th prime is ", candidate )
