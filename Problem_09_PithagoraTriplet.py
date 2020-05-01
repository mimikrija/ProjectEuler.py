# Special Pythagorean triplet
# Problem 9

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


import math
from math import floor, sqrt

def SpecialTriplet():
    for a in range(1,1000):
        for b in range (1,1000):
            potential_c_square = a**2 + b**2
            if floor(sqrt(potential_c_square)) == sqrt(potential_c_square):
                c = int(floor(sqrt(potential_c_square)))
                if a + b + c == 1000:
                    print ("Solution is: ", a ,"x", b, "x",c, " = ", a*b*c)
                    return

SpecialTriplet()