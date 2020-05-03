# Smallest multiple
# Problem 5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def evenly_divisible(number,max_divisor):
    for divisor in range (2,max_divisor+1):
        if number%divisor != 0:
            return False
    return True

solution = 1
for factor in range (2,21):
    solution *= factor

for factor in range (2,21):
    while solution % factor == 0 and evenly_divisible(solution//factor,20):
        solution = solution // factor

print ("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is: ", solution)
