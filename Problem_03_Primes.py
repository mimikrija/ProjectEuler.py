# Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def IsPrime(Number):
    for divisor in range(2,Number):
        if Number%divisor == 0:
            return False
    return True

input = 600851475143

Solution = input

divisor=2
while (Solution//divisor > 1):
    if IsPrime(divisor) and Solution%divisor == 0:
        Solution = Solution //divisor
    else:
        divisor+=1

print ("The largest prime factor of the ", input, " is ", Solution, "!")
