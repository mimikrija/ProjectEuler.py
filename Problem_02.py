#Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

def FibonacciTerm(Term):
    if (Term < 3):
        return Term
    else:
        return FibonacciTerm(Term-1) + FibonacciTerm(Term-2)

counter = 1
Solution = 0
while (FibonacciTerm(counter) <= 4000000):
    if FibonacciTerm(counter)%2 == 0:
        Solution += FibonacciTerm(counter)
    counter += 1

print("Sum of even-valued Fibonacci terms whose values do not exceed four million is: ", Solution)
