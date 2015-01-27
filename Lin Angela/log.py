#!/usr/bin/python
# ========= HASHBANG LINE ABOVE IS MAGIC! =========
# ========= (Must be first line of file.) =========

# ======= BACK END OF AN HTML/PYTHON FORM PROCESSING TEAM ========
# Receives data from HTML front end, processes, generates new HTML.


import cgi
import cgitb
cgitb.enable()  #comment out once full functionality achieved


# ~~~~~~~~~~~~~~~ support functions ~~~~~~~~~~~~~~~
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

append=open('log.txt','a') #fileObject stored as append

def log():
    append=open('log.txt','a')
    if dict.has_key('name') ==False and dict.has_key('message') ==False: #if no name and no message has been submitted
        return "At least write something TT"
    elif dict.has_key('name') ==False: #if a name is not submitted
        dict['name']="Guest"
        append.write("<b><i>") #formatting for name
        append.write(dict['name'])
        append.write("</b></i>")
        append.write(" : ")
        append.write(dict['message'])
        append.write("<br>")
    elif dict.has_key('message') ==False: #if a message is not submitted
        return "Please write a message OR GO AWAY :)" ##this concludes the first part of the logbook
    else:
        append.write("<b><i>")
        append.write(dict['name'])
        append.write(" : ")
        append.write("</b></i>")
        append.write(dict['message'])
        append.write("<br>")
    log2() #calls log2
    append.close()
        
def log2():
    inS=open('log.txt','r')
    l=inS.read().split("\n")
    return "<br>".join(l)
    inS.close()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ========= CONTENT-TYPE LINE REQUIRED. ===========
# ======= Must be beginning of HTML string ======== 
htmlStr = "Content-Type: text/html\n\n" #NOTE there are 2 '\n's !!! 
htmlStr += "<html><head><title>Logbook!</title></head></html>\n"
htmlStr += "<h1><center>LOGBOOK ENTRIES</h1><body bgcolor=#FFB6C1>"


# ~~~~~~~~~~~~~ HTML-generating code ~~~~~~~~~~~~~~
# <<< INSERT YOUR HTML HERE >>>
# for example,
##does the appending!!
if dict.has_key('message'):
    log()
    htmlStr += str (log2() )
else:
    htmlStr += "Please <a href=http://lisa.stuy.edu/~angela.lin/forms/log.html>\
go back </a> to the prompt and ACTUALLY \
ENTER A MESSAGE! (As a bonus, you can also check out what others have wrote!)"
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# == Wrap up HTML string and send it to browser ===
htmlStr += "</center></body></html>"
print htmlStr
