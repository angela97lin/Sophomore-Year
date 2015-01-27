# -*- coding: utf-8 -*-
##Angela Lin
## pd 06
##HW #7
##2013-02-26

##Assignment:
##1. numRealRoots(a,b,c) takes numeric inputs a, b, c -- representing coefficients of a quadratic equation in standard form -- and returns the number of real roots of said equation.
##e.g.,
##numRealRoots(1,2,3) → 0
##numRealRoots(2,4,2) → 1
##numRealRoots(1,3,2) → 2
##
##2. quadSolver(a,b,c) takes numeric inputs a, b, c -- representing coefficients of a quadratic equation in standard form -- and prints the roots, if any. Uses numRealRoots(a,b,c) as a helper function.
##e.g.,
##quadSolver(1,2,3) → “no real roots”
##quadSolver(1,4,4) → -2
##quadSolver(1,-2,-15) → -3  5

import math

def numRealRoots(a,b,c):
	if b**2-(4*a*c)== 0: return 1
	elif b**2-(4*a*c) > 0: return 2
	elif b**2-(4*a*c) < 0: return 0



numRealRoots(2,4,2)
#should be 1
numRealRoots(1,2,3)
#should be 0
numRealRoots(1,3,2)
#should be 2
numRealRoots(-1,-1,1)
#should be 2
#This case vertifies that numRealRoots can take negative numbers.
numRealRoots(0.5,0.6,0.7)
#should be 0
#This case vertifies that numRealRoots can take floats.





def quadSolver(a,b,c):
    if numRealRoots(a,b,c) == 0:
            return "No Real Roots: Discriminant is negative!"
    elif numRealRoots(a,b,c) == 1:
            print (-b/(2*a))
    else:
     print ((-b-math.sqrt(b**2-(4*a*c)))/(2*a)),
     print ((-b+math.sqrt(b**2-(4*a*c)))/(2*a))



quadSolver(1,2,3)
#Should be "No Real Roots: Discriminant is negative!"
quadSolver(1,4,4)
#Should be 2
quadSolver(1,-2,-15)
#Should be -3  5
quadSolver(2.5,1,0)
#Should be 0, -0.4
#This specific case was written to see whether or not quadSolver could handle floats.
quadSolver(1,0,-9)
#This case checks for whether or not quadSolver could handle an ax**2+b*x+c=0 where b=0


