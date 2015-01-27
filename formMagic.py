#!/usr/bin/python
# ========= HASHBANG LINE ABOVE IS MAGIC! =========
# ========= (Must be first line of file.) =========

# ======= BACK END OF AN HTML/PYTHON FORM PROCESSING TEAM ========
# Receives data from HTML front end, processes, generates new HTML.


##Phase I partners: Annique, Radhika
##Phase II partners: Laura
##support:


##The drop-down menu basically assigns the value of the choice chosen to the name of the menu, so {name:value}...As expected!
#Angela Lin
#pd06
#5-21-13
#HW34
##
##To be honest, I'm not even sure I'm using the radio buttons and the
##other goodies properly. However, one problem I had with the radio buttons
##and check buttons is that when nothing is choosen for the radio buttons,
##my code breaks (otherwise, it functions relatively well!) and becomes wacky,
##even though I attempted to add a special case to handle it...



import cgi
import cgitb
cgitb.enable()  #comment out once full functionality achieved


# ~~~~~~~~~~~~~~~ support functions ~~~~~~~~~~~~~~~
#These codes are simply taken from past HW's and such...
def FStoD():
    '''
    Converts return val of FieldStorage() into a standard dictionary
    '''
    d = {}
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value
    return d
dict=FStoD()


def rotate(c,n):
    i = ord(c)
    if i in range(65, 91):
        i += int(n)
        if i > 90:
            i += -26
        return chr(i)
    if i in range(97, 123):
        i += int(n)
        if i > 122:
            i += -26
        return chr(i)


def rotn(n,string):
    temp=[]
    strung=""
    c=''
    for s in string:
       temp.append(s)
    for i in range(len(temp)):
        r = temp[i]
        if ord(r) >= 65 and ord(r) <= 122:
                c = rotate(r,n)

                strung += c
        else:
            strung += r
    return strung

#print rotn(2,"Abc")
#print rotn(5,'foobar')

def reverseStr(string):
    l=[]
    while string != '':
        l.append(string[-1])
        string=string[:-1]
    #print l
    retS="".join(l)
    return retS
    #print retS
#reverseStr('abcdef')

dictK=dict.keys()
dictV=dict.values()
#if ROT13 mode is chosen:
def rotMode():
    retStr=""
    if dict['txt01']!="":
        text=str(rotn(int(dict['rot']),dict['txt01']))
        for d in dictK:
            if dict[d]=='yes':
                retStr+="<"+ d + ">"
        retStr+=text
        for d in dictK:
            if dict[d]=='yes':
                retStr+="</"+ d + ">"
    elif dict['txt01']=="":
         retStr+= "Cannot process: Not given text :("
    return retStr


#if Reverse mode is chosen:
def reverseMode():
    retStr=""
    if dict['txt01']!="":
        text=str(reverseStr(dict['txt01']))
        for d in dictK:
            if dict[d]=='yes':
                retStr+="<"+ d + ">"
        retStr+=text
        for d in dictK:
            if dict[d]=='yes':
                retStr+="</"+ d + ">"
    elif dict['txt01']=="":
         retStr+= "Cannot process: Not given text :("
    return retStr
    
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ========= CONTENT-TYPE LINE REQUIRED. ===========
# ======= Must be beginning of HTML string ========

htmlStr = "Content-Type: text/html\n\n" #NOTE there are 2 '\n's !!! 
htmlStr += "<html><head><title>ROT13</title></head>\n"
htmlStr += "<body>" 


# ~~~~~~~~~~~~~ HTML-generating code ~~~~~~~~~~~~~~
# <<< INSERT YOUR HTML HERE >>>
if 'mode' in dict.keys():
            if dict['mode']=='Reverse' and 'rot' in dict.keys():
                htmlStr += str(rotn(dict['rot'],reverseMode()))
            elif dict['mode']=='Reverse':
                htmlStr += str( reverseMode() )
            elif 'rot' in dict.keys() and dict['mode']=="ROT":
                htmlStr += str(rotMode())
else:
            htmlStr+= "You didn't choose a mode!"

    
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# == Wrap up HTML string and send it to browser ===
htmlStr += "</body></html>"
print htmlStr
