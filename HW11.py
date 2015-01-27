# Angela Lin
# pd 06
# HW11
# 2013-03-07

##1. bondify("name") takes a name written in First Last format, and returns the sassy version, as shown below.
##bondify(“James Bond”) → “Bond, James Bond”

def bondify(name):
    n=name.find(" ") #finds the separation/space between the first and last name
    a=name[n+1:] #returns all characters from the space to the end, inclusive (aka the last name)
    return a+", "+name #returns the name in a sassy format, with a nice comma in the middle!


print bondify("Angela Lin")
print "should be..."
print "Lin, Angela Lin"

print bondify("James Bond")
print "should be..."
print "Bond, James Bond"
