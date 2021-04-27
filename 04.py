# Largest palindrome product
# Problem 4

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
from itertools import combinations
from operator import mul


def is_palindrome(num):
    candidate = str(num)
    return candidate == candidate[::-1]

def largest_palindrome_which_is_a_two_number_product(digits):
    top = 10**digits - 1
    bottom = top - top // 10**(digits-3) if digits >= 3 else 10
    products = ((mul(*p), *p) for p in combinations(range(top, bottom, -1), 2) if is_palindrome(mul(*p)))
    return max(products)

digits = 3
max_palindrome, factor_1, factor_2 = largest_palindrome_which_is_a_two_number_product(digits)


print(f"The largest palindrome made from the product of two {digits}-digit numbers is: {factor_1} x {factor_2} = {max_palindrome}!")
