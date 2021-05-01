# Sum square difference
# Problem 6

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum_of_the_squares = sum(natural**2 for natural in range(1, 101))
square_of_the_sum = sum(natural for natural in range(1, 101))**2

print(f"Solution is: {square_of_the_sum - sum_of_the_squares}")
# 25164150
