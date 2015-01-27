#Angela Lin
#pd 06
#HW#16
#2013-03-18



##1. listFind(L,q) takes a list L and a query q as inputs, and returns the first index where q occurs in the L. Returns -1 if q is not found in L.
##listFind([5,4,3,2,1], 2) → 3
##listFind([5,4,3,2,1], 6) → -1
##listFind([5,4,’cat’,’dog’,’cat’], 'cat') → 2

def listFind(L,q):
    length=len(L) #finds the length of L
    index=0
    while length>index: #while the index of the string is not greater than the length
        if L[index-1:index]==[q]:#check if the current index is equivalent to q
            return index-1 #if so, return the current index
        else:
            index=index+1 #otherwise, move on 
    return -1 #otherwise, return -1 (if q is not found)

print listFind([4,2], 4) #4
print listFind([5,4,3,2,1], 2) #→ 3
print listFind([5,4,3,2,1], 6) #→ -1
print listFind([5,4,'cat','dog','cat'], 'cat') #→ 2


def listSum(L):
    sum=0
    index=0
    while index<len(L): #while the index is within the string
        sum+=L[index] #add the value of the current number to the sum variable
        index+=1 #move on to the next variable
    return sum #when the index is equal to the length of L, return the value of sum

print listSum( [0,1,2,3] ) #→ 6
print listSum( [0, -1, 1]) #0

def doublify(L):
    index=0
    newList=[]
    while index<len(L): #while the index is within the string
        newElement=L[index]*2 #multiplies the current character's value by 2
        newList+=[newElement] #adds the new element to a new list
        index+=1 
    return newList #returns the new list after all elements have been doubled

print doublify([0,1,2,3])#[0, 2, 4, 6]
print doublify([1,2,3,4,5])#[2, 4, 6, 8, 10]
