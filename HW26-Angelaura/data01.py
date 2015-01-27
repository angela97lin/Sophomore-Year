#!/usr/bin/python
print "Content-Type: text/html\n"
print ""
#these texts are separated so that it is easier to handle on python,
#to prevent having to go alllllll the way to the right to edit some text!

text="Our data compares how different students from different states in the United States do on the SAT and ACT test.The reason why we chose to analyze this data was because there are always debates (although many are not serious) about which states are smarter, which states have brighter students, etc."
text02=" In addition, it is interesting to read about these SAT scores and ACT scores in an organized matter because the SATs are something that will soon encompass us (in junior year).<br><br>"
text03="<br>This data (.csv file) was found on <i><a href=http://thomaslotze.com/projects/class_sizes/>Original Source</a></i> or <i><a href=http://thomaslotze.com/projects/class_sizes/2006-07.csv>Data in CSV (viewed as HTML)</a></i><br><br><br>"
text04="<a href=http://lisa.stuy.edu/~angela.lin/analysis01.py>Click here for Analysis of Data!</a>"


stream=open('scores.csv', 'r') 
readas=stream.read()
stream.close()
#print readas #just used to double check what readas returns

def tableify(readas):
    ret=readas.splitlines()
    retString="<html><title>SAT Scores</title><h1><center>SAT Scores in the USA</center></h1>"
    retString=retString+text+text02+text03+"<br><table border=1>"
    print ret
    for x in ret:
        innerlist=x.split(",")
        for element in innerlist:
            retString+="<td>"+element+"</td>"
        retString+="</tr>\n"
    return retString+"</table>"+"Now that you have read through (or at least skimmed through) this table...<br>"+text04+"</html>" #concludes and returns the proper HTML coding!

print tableify(readas)


#This is pretty much the same code we have been using, but I had to change my code because it only accepted two columns.



