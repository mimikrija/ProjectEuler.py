# Largest palindrome product
# Problem 4

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def IsPalindrome(Number):
    Candidate = str(Number)
    Digits = len(Candidate)
    if (Digits > 1):
        # do some testing - this will work for both even and odd number of digits
        for digitcounter in range (0,Digits//2):
            if (Candidate[digitcounter] != Candidate[-digitcounter-1]):
                return False
        return True
    else:
        # every single-digit number is a palindrome
        return True

Solution = 1
for FirstNumber in range (999,99,-1):
    for SecondNumber in range (FirstNumber,99,-1):
        Prospect = FirstNumber*SecondNumber
        if Prospect < Solution:
            continue
        if IsPalindrome(Prospect):
            Solution = Prospect
            FactorOne = FirstNumber
            FactorTwo = SecondNumber



print ("The largest palindrome made from the product of two 3-digit numbers is: ", FactorOne, " x ", FactorTwo, " = ", Solution)