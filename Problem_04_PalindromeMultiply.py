# Largest palindrome product
# Problem 4

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def IsPalindrome(Number):
    Candidate = str(Number)
    Digits = len(Candidate)
    if (Digits > 1):
        # do some testing
        for digitcounter in range (0,Digits//2):
            if (Candidate[digitcounter] != Candidate[-digitcounter-1]):
                return False
        return True
    else:
        # every single digit number is a palindrome
        return True

Solution = 1
for FirstNumber in range (999,99,-1):
    for SecondNumber in range (999,99,-1):
        Prospect = FirstNumber*SecondNumber
        if Prospect < Solution:
            continue
        if IsPalindrome(Prospect):
            Solution = Prospect


print ("The largest palindrome made from the product of two 3-digit numbers is: ", Solution)