# Special Pythagorean triplet
# Problem 9

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from itertools import combinations
from functools import reduce
from operator import mul

is_pyth_tripplet = lambda a, b, c: a**2 + b**2 == c**2


GOAL_SUM = 1000

# set of sorted triplets which give GOAL_SUM
triplets_sum_goal = {tuple(sorted((*combo, GOAL_SUM - sum(combo))))
                        for combo in combinations(range(1, GOAL_SUM-1), 2)
                        if sum(combo) < GOAL_SUM}


triplet = next(combo for combo in triplets_sum_goal if is_pyth_tripplet(*combo))
sides = ' x '.join(str(side) for side in triplet)
print(f'pythagora triplet with sum of sides equal to {GOAL_SUM} is: {sides} = {reduce(mul, triplet)}')
# 31875000
