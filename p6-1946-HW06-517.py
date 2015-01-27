# Angela Lin
# pd 6
# HW06
# 2013-02-22

import math

def pythTriple(a,b,c):
    if a>0 and b>0 and c>0 and (a**2)+(b**2)==(c**2):
        return True
    elif a>0 and b>0 and c>0 and (a**2)+(c**2)==(b**2):
        return True
    elif a>0 and b>0 and c>0 and (b**2)+(c**2)==(a**2):
        return True
    else: return False


#This is derived from the Pythagorean Theorem where a^2+b^2=c^2, where a, b, and c are all positive integers. *Crucial so that the first case is false, rather than true.*
#One problem encountered was the problem that the order of the three terms mattered. In order to solve this problem, three different cases were made.For example, because pythTriple (5,3,4) is true, regardless or the order in which a, b, and c are placed, it is important to list ALL cases using "or."
#In this case, "return" was used, since the point of the function was to return a boolean value. In order to actually see that boolean value, "print" must be used (to vertify our code's success.)
#Note: "and" and "or" are very picky. If not placed through separate elif conditions, the first case will take on a True value.


print pythTriple(0,0,0)
print "should be false"
print pythTriple(5,4,3)
print "should be true"
print pythTriple(3,4,6)
print "should be false"
print pythTriple(32,255,257)
print "should be true"
print pythTriple(4,5,3)
print "should be true"
#This test case is important in order to test whether or not order will affect our function; it should not.
print pythTriple (0,-1,1)
print "should be false"
#This test case is to make sure that negative values for a, b, and/or c will produce "false," regardless if the sum of the squares of two elements is equivalent to the third element squared.





def cartDist(X1,Y1,X2,Y2):
    return (((X1-X2)**2+(Y1-Y2)**2)**(.5))
#This is derived from the formula where the distance between two points is equivalent to the square root of the sum of the x-coordinates squared plus the sum of the y-coordinates squared.
#Similarly, as the assignment asked to produce a function that returned the distance between two points, return was used. If we wish to see the results,   
print cartDist(0,0,0,0)
print "should be 0"
print cartDist(4,4,4,4)
print "should be 0"
print cartDist(0,0,3,4)
print "should be 5"
print cartDist(0,0,4.5,1.5)
print "should be 4.74341649"
#This test case was used to make sure that cartDist can handle decimals :D
print cartDist(-4,-4,0,0)
print "should be 5.656854249"
#This test case was used to test whether or not it could handle negative numbers, as well as positive.

           
