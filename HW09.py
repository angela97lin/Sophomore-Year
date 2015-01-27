#Angela Lin
# pd 06
# HW09
# 2013-03-04
##
##1. sumDigits(n) takes a positive integer n and returns the sum of its digits.
##
##2. squares(n) takes a positive integer n and prints each integer from 1 to n, inclusive, along with its square. The number and its square should appear on the same line.
##
##3. sumPerfSqs(n) takes a positive integer n and returns the sum of the perfect squares between 1 and n, inclusive.



def sumDigits(n):
    sum=0
    while n>0:
        sum=(n%10)+sum
        n=(n//10)
    return sum+n
#sumDigits takes a number, n, and inputs the sum of its digits.
#In this case, state variable sum was created. It begins with a value of 0.
#If n is greater than 0, sum will increase to equal the previous sum and n%10, which essentially finds the ones-place of n.
#n will then be divided by 10 (to get rid of the ones place that was computed). This will happen until n=0 (when n is less than 10), when sumDigits will return the current sum.
print sumDigits(123)
print "should be 6"
print sumDigits(1000000001)
#This case was to check whether or not sumDigits would be stopped by the 0's in between the two ones.
print "should be 2"
print sumDigits(00000002)
#Once again, this tests the strength of sumDigits against 0's.
print "should be 2"
print sumDigits(9999)
print "should be 36"



def squares(n):
    int=1
    while int<n:
        print int, int**2
        int=int+1
    print int, int **2

#squares(n) prints each number and its square from 1 to n.
#it will continually print each number and its square until it has reached n and n**2; that is when the program terminates.
#Test Cases:
squares(30)
squares(11)
#These cases are absolutely random and are just used to vertify that squares(n) works.



  
def sumPerfSqs(n):
    sum=0
    cow=1
    while cow<=n:
        if ((cow**.5)%1==0):
            sum=sum+cow
            cow=cow+1
        else: cow=cow+1
    return sum

#sumPerfSqs(n) returns the sum of all of the perfect squares between n and 1.
#At first, it checks whether or not "cow" is a square root; If it is, then sum becomes sum+cow, while cow increases by 1
#and slowly becomes closer to n.
#If cow is not a perfect square, it will simply become cow+1, while the sum remains unchanged.
#This process loops until cow=n.


print sumPerfSqs(2)
print "should be 1"
print sumPerfSqs(3)
print "should be 1"
print sumPerfSqs(4)
print "should be 5"
print sumPerfSqs(5)
print "should be 5"
print sumPerfSqs(16)
print "should be 30"
print sumPerfSqs(25)
print "should be 55"
