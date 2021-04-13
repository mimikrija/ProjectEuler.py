# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

def even_fibos(lim):
    "returns only even fibonacci numbers lower than `lim`"
    # first three members are n
    for n in range(1, 4):
        prev = n - 1
        current = n
        if current %2 == 0:
            yield current
    # otherwise they are a sum of previous two
    while True:
        old_current = current
        current += prev
        if current > lim:
            return
        prev = old_current
        if current % 2 == 0:
            yield current

fibos = even_fibos(4*1000*1000)
solution = sum(n for n in fibos)

print(f"Sum of even-valued Fibonacci terms whose values do not exceed four million is: {solution}")
# Sum of even-valued Fibonacci terms whose values do not exceed four million is:  4613732
