# Largest palindrome product
# Problem 4

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def IsPalindrome(Number):
    Candidate = str(Number)
    return Candidate == Candidate[::-1]

Solution = 1
for FirstNumber in range (999,99,-1):
    for SecondNumber in range (FirstNumber,99,-1):
        Prospect = FirstNumber*SecondNumber
        if Prospect > Solution and IsPalindrome(Prospect):
            Solution = Prospect
            FactorOne = FirstNumber
            FactorTwo = SecondNumber


print ("The largest palindrome made from the product of two 3-digit numbers is: ", FactorOne, " x ", FactorTwo, " = ", Solution)
