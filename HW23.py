##Angela Lin
##pd 06
##HW 23
##04-16-13


##1. common(L1,L2) takes 2 lists as input and returns a new list containing values common to both. Assumes no repeated values in either list.
##e.g.,
##common( [1,5,4,3,2] , [4,5,10,15] ) → [4,5]

def common(L1,L2):
    retL=[]
    for n in L1:
        if n in L2:
            retL.append(n)
    return retL

##Common basically goes through the every element in the first list.append If that
##element is in L2, then append that element to a new list that will be returned
##after the for loop is done.
print common( [1,5,4,3,2] , [4,5,10,15] ) #[5,4]

            
##2. alphabetize(names) takes a string of names, assumed to be in Last-First pairings, separated by commas, and returns an alphabetized list of names with line breaks in string form.
##e.g.,
##alphabetize( “Wayne,Bruce,Kent,Clark,Parker,Peter” ) → “Kent Clark\nParker Peter\nWayne Bruce”

def alphabetize(names):
    i=1
    list=names.split(",")
    firstName=list[0:2] #first full name! meant as a comparison
    retString=" ".join(firstName)+"\n" #retString begins with the full name
    while i+1<len(list):
        if i%2==0:
            if ord((list[i])[0])>firstName: #if the first letter of the last name is after the first letter of firstName
                retString+=list[i-1]+" "+list[i]+"\n" #append full name to retString
                list=list[i+1:] #remove from list
                i=0
            else:
                retString=" ".join(list[i:i+2])+"\n"+retString
                list=list[i+2:]
                i=0
        else:
            i+=1
    return retString
    
##This alphabetize can only handle 2 names, or else it will simply print the names
#nonalphabetically... :/


print alphabetize("Wayne,Bruce,Kent,Clark,Parker,Peter,Lane,Louis") 

