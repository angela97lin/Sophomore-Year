stream=open('testdata.csv', 'r') 
readas=stream.read()
stream.close()
print readas #just used to double check what readas returns


def tableify(readas):
    ret=readas.split("\n") 
    retString=""
    for n in ret: #for every element in the list ret
        findComma=n.find(",")
        n="<tr><td>"+n[:findComma]+"</td><td>"+n[findComma+1:]+"</td></tr>" #basically replaces the comma with necessary HTML coding
        retString+=n 
    return retString #returns the proper HTML coding!


print tableify(readas)

# ???
outStream=open('table.html','w')
outStream.write(tableify(readas))
outStream.close()


