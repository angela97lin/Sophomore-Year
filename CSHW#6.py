# Angela Lin
# pd 6
# HW06
# 2013-02-22

import math

def pythTriple(a,b,c):
    if a**2+b**2==c**2 and a>0 and b>0 and c>0 :
        print "true"
    else: print "false"
#This is derived from the Pythagorean Theorem where a^2+b^2=c^2, where a, b, and c are all positive integers. *Crucial so that the first case is false, rather than true.*
    
pythTriple(0,0,0)
print "should be false"
pythTriple(3,4,5)
print "should be true"
pythTriple(3,4,6)
print "should be false"
pythTriple(32,255,257)
print "should be true"



def cartDist(X1,Y1,X2,Y2):
    return (((X1-X2)**2+(Y1-Y2)**2))**.5
#This is derived from the formula where the distance between two points is equivalent to the square root of the sum of the x-coordinates squared plus the sum of the y-coordinates squared.


print cartDist(0,0,0,0)
print "should be 0"
print cartDist(4,4,4,4)
print "should be 0"
print cartDist(0,0,3,4)
print "should be 5"
