#!/usr/bin/python

print "Content-Type: text/html\n"

print ""

import cgi
import cgitb
cgitb.enable()##Gives tracing info to help debug
formData=cgi.FieldStorage()

#print formData #Dictionary
#print formData.values()
#print formData.keys()
print "<br>"

def convert():
    d={}
    retString=""
    for k in formData.keys():
        try:
            if float(formData[k].value)>0:
                d[k] = float(formData[k].value) ##atrribute; piece of data...
            else:
                retString+= "Given negative value! Please try again."
        except:
            retString+= "Error! Not given  proper dimensions!"
    print retString
    return d
dict=convert()
#print convert()



#Reusable Helper Function!! It pretty much can turn any query string into a dictionary.
##def StrToDict(string):
##    d={}
##    L=string.split("&")
##    #print L
##    for a in L:
##        a=a.split("=")
##        #print a
##        try:
##            float(a[1])>0
##            d[a[0]]=float(a[1])
##        except:
##            print "ERROR!<br>"
##        
##    return d
##    #TRY BLOCK FOR NEGATIVE, NON#'s, FLOATS
##
##print dict

def dim():
    i=0
    dictList=dict.keys()
    d2List=dict.values()
    while i<len(d2List):
        try:
            if d2List[i]<0:
                print "Error! Negative value given!"
            else:
                i+=1
        except:
            print "Not given numerical values."
    if len(dictList)==0:
        print 'Given no parameters! Please put parameters <b><i>"length", "width", and "height"</b></i> to see proper results!'
        print "<br>This means, after dim.py, put ?length=NUM&width=NUM&height=NUM"
    elif len(dictList)==1:
        print "Given only ONE dimension! Feed me more dimensions, in the format, ?length=NUM&width=NUM&height=NUM please!"
    else:
        try:
            length=dict['length']
            width=dict['width']
            height=dict['height']
            v=length*width*height
            print "The volume of a rectangular prism with your dimensions"
            print "<b>length="
            print length
            print "width="
            print width
            print "height="
            print height
            print "</b><br>IS..."
            print "<br>"
            print float(v)
            print " cubed units! <br>This is what a rectangular prism looks like!<br> <img src='cuboid.gif' alt='cuboid' width=400 height=275>"
        except:
            d1=dict[dictList[0]]
            #print length
            d2=dict[dictList[1]]
            a=d1*d2
            print "Silly! Didn't you want dimensions of a volume? Given that you only gave me two dimensions, here is the area corresponding to those dimensions."
            print "<br>"
            print a
            print " squared units<br>"
            print "If you want the volume of something, please give parameters <b>'length', 'width', and 'height'!<b>"
            print "<br>This means, after dim.py, put ?length=NUM&width=NUM&height=NUM"
            
                    
dim()



