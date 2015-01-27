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
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ========= CONTENT-TYPE LINE REQUIRED. ===========
# ======= Must be beginning of HTML string ======== 
htmlStr = "Content-Type: text/html\n\n" #NOTE there are 2 '\n's !!! 
htmlStr += "<html><head><title>Insert Cleverer Title Here</title></head></html>\n"
htmlStr += "<body>"


# ~~~~~~~~~~~~~ HTML-generating code ~~~~~~~~~~~~~~
# <<< INSERT YOUR HTML HERE >>>
# for example,
htmlStr += str( FStoD() )
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# == Wrap up HTML string and send it to browser ===
htmlStr += "</body></html>"
print htmlStr
