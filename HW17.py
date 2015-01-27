#Angela Lin
#pd 06
#HW17
#2013-03-19

##1. rmNegatives(L) removes the negative numbers from list L, assumed to contain only numeric elements. (Modifies L; does not create a new list.)
##rmNegatives( [5,4,3,2,1] ) → [5,4,3,2,1]
##rmNegatives( [5,-4,3,-2,1] ) → [5,3,1]

def rmNegatives(L):
    index = 0
    while index < len(L): 
        if L[index] < 0: #checks if the current number is less than 0 AKA negative
            L.remove(L[index]) #removes the current number
        else:
            index+=1


L=[5,4,3,2,1]
rmNegatives(L)
print L

Z=[5,-4,3,-2,1]
rmNegatives(Z)
print Z


##2. listOFib(n) returns a list of the first n Fibonacci numbers, starting with 0 as the 0th term, 1 as the 1st term, 1 as the 2nd term, and so on.
##listOFib(1) → [0]
##listOFib(2) → [0,1]
##listOFib(3) → [0,1,1]
##listOFib(4) → [0,1,1,2]


#Honestly, I am not even sure how this works; I wanted a to begin at 0 and by luck, tried 1
#but for some reason, it doesn't work when I begin at 0

def listOFib(n):
    a = 1
    fiblist= []
    if a == 1:
        fiblist = [0]
        a = a + 1
    if a == 2:
        fiblist = [0,1]
        a = a + 1
    while len(fiblist) < n:
        fiblist = fiblist + [(fiblist[-1]) + fiblist[-2]]
        a = a + 1
    return fiblist

print listOFib(1)
print listOFib(2)
print listOFib(3)
print listOFib(4)
        
        
##3. sentify(L) returns a string comprised of list L’s elements, in order, with spaces between. Assumes L contains only string elements.
##sentify( [“this”, “is”, “how”, “we”, “do”] ) → “this is how we do”

def sentify(L):
    newString="" 
    while len(L)>0: #while L has elements...
        newString+=L[0]+" " #append to newString the first element of list L and a space
        L=L[1:] #L gets the value of all elements of L except the first (0th index)
    return newString #when there are no elements in L, return the string

print sentify( ["this", "is", "how", "we", "do"] )# → “this is how we do”
