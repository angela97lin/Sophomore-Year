#Angela Lin, Farib Mohammed Khan, Tanvir Nadim
#pd 06
#HW17b/18
#13-03-20

#We decided to use Angela's rmNegative, but rather than using remove,
#we used pop() based on the code; pop() must be given an index, and
#removes the index it's given. This is the most efficient when you
#go through each index, as when the value of the current index is
#less than 0, pop() will just remove it, unlike Angela's previous code which
#used remove() by finding the value of the current index. Using pop() is much more
#direct and therefore, takes less steps.

######
#POP:
#syntax: Listname.pop(index)
#pop() removes the element of the list at a given index and returns it. If pop() is not given
#an index, then it simply removes the last element of the list, and returns it.
#For example...
#L=[1,2,3]
#print L.pop() => 3
#print L=> [1,2]

######
#REMOVE:
#syntax: Listname.remove(element)
#remove() takes an element from the list and removes the first occurence of that element
#from the list. If the element is not in the list, then it returns an ERROR message: "ValueError: list.remove(x): x not in list"
#For example...
#L=[1,2,3]
#L.remove(1)
#print L => [2,3]
######
#DEL:
#syntax: del Listname[index] or del Listname[index1:index2]
#Del is capable of removing an element from a list or removing all of the elements
#within a given slice (indicated by index1:index2), making it more useful to remove more than
#just one element.
#For example...
#L=[1, 2, 3]
#del L[0:2]
#print L =>[3]




#1. rmNegatives(L) removes the negative numbers from list L, assumed to contain only numeric elements. (Modifies L; does not create a new list.)
##rmNegatives( [5,4,3,2,1] ) → [5,4,3,2,1]
##rmNegatives( [5,-4,3,-2,1] ) → [5,3,1]

def rmNegatives(L):
    index = 0
    while index < len(L): 
        if L[index] < 0: #checks if the current number is less than 0 AKA negative
            L.pop(index) #removes the current number
        else:
            index+=1


L=[5,4,3,2,1]
rmNegatives(L)
print L

Z=[5,-4,3,-2,1]
rmNegatives(Z)
print Z

