# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def is_multiple_of_any(num, divisors):
    "returns if `num` is divisible by any of the `divisors`"
    return any(num % divisor == 0 for divisor in divisors)

solution = sum(candidate for candidate in range(1, 1000)
                        if is_multiple_of_any(candidate, (3, 5)))


print(f'the sum of all the multiples of 3 or 5 below 1000 is: {solution}')
# the sum of all the multiples of 3 or 5 below 1000 is: 233168
