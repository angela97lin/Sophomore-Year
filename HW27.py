##Angela Lin
##pd 06
##HW27
##04-29-2013


##the above process accesses and reads the file (plain text file) given.
inStream=open('freqdata_comma','r')
lines=inStream.read() ##returns a string with the contents from filename
inStream.close()


def modeFC(filename):
    list2=[]
    buckets=[]
    i=0
    list=lines.split(",")#splits the string based on the commas, which separates each number
    for n in list: #for every element in list
        n=int(n) #turn the string into an int (ex: '21'-->21)
        list2.append(n) #add this integer value to a new list
    #print list2 -> tests that list2 is a list of int, not strings containing int
    while i<=max(list2): ##this code is essentially the same as the original modeList code
        buckets.append(0)
        i+=1
    for a in list2:
        buckets[a]+=1
    return buckets.index(max(buckets))
        

print modeFC('freqdata_comma') #21




    
##modeFL is essentially the same as modeFC, except that rather than having a set
##of data separated by commas, the data values are separated by "\n."
##In addition, we have to eliminate the last element of the list when we split it because
##the last element is '', not a string with an integer.

inStream=open('freqdata_line','r')
lines=inStream.read() ##returns a string with the contents from filename
inStream.close()
#print lines
##the above process accesses and reads the file (plain text file) given.

def modeFL(filename):
    list2=[]
    buckets=[]
    i=0
    list=lines.split("\n")
    #print list #splits the string based on the commas, which separates each number
    list=list[:-1] #this is necessary because for some reason, ' ' is the last element of list...
    for n in list:
        n=int(n)
        list2.append(n)
    #print list2 -> tests that list2 is a list of int, not strings containing int
    while i<=max(list2):
        buckets.append(0)
        i+=1
    for a in list2:
        buckets[a]+=1
    return buckets.index(max(buckets))
        

print modeFL('freqdata_line') #21
    
