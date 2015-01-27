# Angela Lin
# pd #6
# HW#05
# 2013-02-21

import math
math.pi
math.pow



expression1= (3.0+4)/(7-2)

expression2=((math.pow(5,2))-(4/8))/(16-(8*(9**.5)))

#should be -3.0625 but instead, "print expression2 gives me -3.125!!
expression3=(5.0/6)/(7+(9/5))

#should be .094696969697 but is 0.1041666667??


def AreaCirc(r):
   print math.pi*(r**2)

##I used the math formula, pi*r^2 to define AreaCirc
  
AreaCirc(1)
print "should be 3.141592653589793"

AreaCirc(3)
print "should be 28.274333882308138"

AreaCirc(5)
print "should be 78.53981633974483"


def AreaWasher(radInner,radOuter):
    print AreaCirc(radOuter)-AreaCirc(radInner)
##The area of the washer should be equivalent to the difference between the two circles. However, I am unable to get this to work and instead, receive an error message stating that - is unsupported by the type "NoneType" and "NoneType"

    
AreaWasher (0,2)
print "should be 12.566370614359172"
AreaWasher (3,5)
print "should be 50.26548245743669"
AreaWasher (6,10)
print "should be 201.06192982974676"
##The error for this code is very frustrating.."TypeError: unsupported operand type(s) for -: 'NoneType' and 'NoneType'"



def SumOfSquares(a,b):
    print (a**2)+(b**2)

SumOfSquares(0,0)
print "should be 0"
SumOfSquares(1,2)
print "should be 5"
SumOfSquares(4,5)
print "should be 41"
