##Team: Angelaura!
##Members: Angela Lin and Laura Wang
##MKS22-06
##HW-25
##
##Dataset: Starbucks locations in New York City
##Data Source:http://code.google.com/p/overplot/source/browse/geocoded-locations.csv
##Chosen because coffee is clearly essential to life. "Without coffee we are not people, we are skins without life force and caffeine! @_@
##It is always wonderful to be able to find a Starbucks when one feels like they are close to dying~


stream=open('data_hw25.csv', 'r') 
readas=stream.read()
stream.close()
print readas #just used to double check what readas returns


def tableify(readas):
    ret=readas.split("\n") 
    retString="<html><table border=1>"
    for n in ret: #for every element in the list ret
        findComma=n.find(",")
        n="<tr><td>"+n[:findComma]+"</td><td>"+n[findComma+1:]+"</td></tr>" #basically replaces the comma with necessary HTML coding
        retString+=n 
    return retString+"</table></html>" #returns the proper HTML coding!


cow=tableify(readas)
#cow was chosen for no particular reason...

outStream=open('HW25.html','w')
outStream.write(cow)
outStream.close()


