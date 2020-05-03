# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def IsMultipleOf(NaturalNumber,divisor):
    return (NaturalNumber%divisor == 0)

Solution = 0
for Candidate in range(1,1000): # range (1,1000) goes from 1 to 999
    if ( IsMultipleOf(Candidate,3) or IsMultipleOf(Candidate,5) ):
        Solution += Candidate

print("the sum of all the multiples of 3 or 5 below 1000 is: ", Solution)
