#Angela Lin
#pd 06
#HW12
#2013-03-08



####Problem #1: Multiples of 3 and 5
##If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
##
##Find the sum of all the multiples of 3 or 5 below 1000.

def mult3and5():
    m=0
    n=0
    sum=0
    sum1=0
    while m<1000: #limits multiples of 3 to below 1000
        if m%5!=0:#makes sure we do not add the multiples of 3 AND 5 twice!
            sum1+=m
            m+=3
        else:
            m+=3
    while n<1000:
             sum=sum+n
             n+=5
    return sum+sum1
#mult3and5 calculates the sum of all the multiples of 3 and 5 that are below 1000.
#First, a few variables were set up; m and sum were used to
#calulate the sum of all multiples of 3 (NOT divisible by 5) and under 1000,
#while sum and n were used to calculate the sum of all multiples
#of 5 under 1000.
#mult3and5 first adds up all of the multiples of 3 that are not evenly divisible by 5 and are <1000.
#Then, mult3and5 adds that amount to the multiples of 5 under 1000.
#Finally, mult3and5 adds these two sums together for a grand total of 233168.


print mult3and5()
print "should be..."
print "233168"



####Problem 5: Smallest Multiple
##2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
##
##What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallestMultiple():
 #2520 is based off the fact that the smallest number that can be divided by numbers 1-10 without any remainder.
    return 2520*11*13*17*19*2
    #these numbers that are multiplied by 2520 are all numbers between 11-20:
    #it is unnecessary to multiply by 12 because it is equivalent to 2*6, which is covered by 2520.
    #it is unnecessary to multiply by 14 because it is equivalent to 2*7, which is covered by 2520.
    #it is unnecessary to multiply by 15 because it is equivalent to 3*5, which is covered by 2520.
    #it is unnecessary to multiply by 18 because it is equivalent to 2*9, which is covered by 2520.
    #BECAUSE THERE IS ONLY ONE MULTIPLE OF 4 COVERED IN 2520, the smallestMultiple must be multiplied by 2 to 'convert' 2 into 4 and thus, have 4*4 (aka 16) covered in the smallestMultiple


print smallestMultiple()
print "should be..."
print "232792560"

####Problem 16: Power Digit Sum
##2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
##
##What is the sum of the digits of the number 2^1000?



def powerDigitSum():
    sum=0
    number=2**1000 
    while number>0: #This is basically sumDigits, but it was refreshing to rework the code~
        sum+=(number%10)
        number/=10
    return sum


print powerDigitSum()
print "should be..."
print "1366"

####Problem 20: Factorial Digit Sum
##n! means n(n-1)  ...  3 * 2 * 1
##
##For example, 10! = 10 * 9  ...  3 * 2 * 1 = 3628800,
##and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
##
##Find the sum of the digits in the number 100!

def fact100():
    n=1
    product=1
    while n<=100:
        product=n*product
        n=(n+1)
    return product
##This will be used as a helper function to factDigitSum() to avoid confusion.

def factDigitSum():
    n=fact100()
    sum=0
    while n>0: #Once again, this is applying the use of sumDigits.
            sum=sum+(n%10)
            n/=10
    return sum

print factDigitSum()
print "should be..."
print "648"

####Problem 6: Sum Square Difference
##The sum of the squares of the first ten natural numbers is,
##
##1^2 + 2^2 + ... + 10^2 = 385
##The square of the sum of the first ten natural numbers is,
##
##(1 + 2 + ... + 10)^2 = 552 = 3025
##Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385 = 2640.
##
##Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sumOfSquares():
    sum=0
    n=1
    while n<=100:
        sum=sum+(n**2)
        n=n+1
    return sum
def squareOfSums():
    sum=0
    n=1
    while n<=100:
        sum=n+sum
        n=n+1
    return sum**2
##Both sumOfSquares and squareOfSums were used as helper functions for sumSquareDifference.

def sumSquareDifference():
   return squareOfSums()-sumOfSquares()
#sumSquareDifference calculates the difference between squareOfSums() and sumOfSquares().

print sumSquareDifference()
print "should be..."
print "25164150"

        











##And finally... a complete fail of an attempt at #42:
##Problem 42
##Coded Triangle Numbers:
##The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
##so the first ten triangle numbers are:

##1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

##By converting each letter in a word to a number corresponding
##to its alphabetical position and adding these values we form
##a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
##If the word value is a triangle number then we shall call the word a triangle word.
##
##def divideCodeTN(n):
##     return (.5)*n*(n+1)%1==0
##
##
##print divideCodeTN(1)
##print divideCodeTN(3)
##print divideCodeTN(6)
##print divideCodeTN(10)
##
##
##
##def assignLetter(word):
##    print word[0]
##
##assignLetter("abc")
##
##def wordV(word):
##    value=0
##    sum=0
##    if assignLetter(word)=="a":
##        value= 1
##    elif assignLetter(word)=="b":
##        value= 2
##    elif assignLetter(word)=="c":
##        value= 3
##    elif assignLetter(word)=="d":
##        value= 4
##    elif assignLetter(word)=="e":
##        value= 5
##    elif assignLetter(word)=="f":
##        value= 6
##    elif assignLetter(word)=="g":
##        value= 7
##    elif assignLetter(word)=="h":
##        value= 8
##    elif assignLetter(word)=="i":
##        value= 9
##    elif assignLetter(word)=="j":
##        value= 10
##    elif assignLetter(word)=="k":
##        value= 11
##    elif assignLetter(word)=="l":
##        value= 12
##    elif assignLetter(word)=="m":
##        value= 13
##    elif assignLetter(word)=="n":
##        value= 14
##    elif assignLetter(word)=="o":
##        value= 15
##    elif assignLetter(word)=="p":
##        value= 16
##    elif assignLetter(word)=="q":
##        value= 17
##    elif assignLetter(word)=="r":
##        value= 18
##    elif assignLetter(word)=="s":
##        value= 19
##    elif assignLetter(word)=="t":
##        value= 20
##    elif assignLetter(word)=="u":
##        value= 21
##    elif assignLetter(word)=="v":
##        value= 22
##    elif assignLetter(word)=="w":
##        value= 23
##    elif assignLetter(word)=="x":
##        value= 24
##    elif assignLetter(word)=="y":
##        value= 25
##    elif assignLetter(word)=="z":
##        value= 26
##    while len(word) != 0:
##        sum=sum+value
##        word=word[1:-1]
##        wordV(word)
##
##wordV("sky")
