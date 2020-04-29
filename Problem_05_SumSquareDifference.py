# Sum square difference
# Problem 6

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum_of_the_squares = 0
natural_sum = 0

for natural in range(1,101):
    sum_of_the_squares += natural**2
    natural_sum += natural

square_of_the_sum = natural_sum**2
print ("solution is: ", square_of_the_sum - sum_of_the_squares)
