#!/usr/bin/python
# ========= HASHBANG LINE ABOVE IS MAGIC! =========
# ========= (Must be first line of file.) =========

# ======= BACK END OF AN HTML/PYTHON FORM PROCESSING TEAM ========
# Receives data from HTML front end, processes, generates new HTML.


import cgi
import cgitb
cgitb.enable()  #comment out once full functionality achieved
formData=cgi.FieldStorage()#parses query string

# ========= CONTENT-TYPE LINE REQUIRED. ===========
# ======= Must be beginning of HTML string ======== 
htmlStr = "Content-Type:text/html\n\n" #NOTE there are 2 '\n's !!!
htmlStr += "<html><head><title>Volume-ator</title></head></html>\n"
htmlStr += "<body background='prism.jpg'><font color='#FFFFFF'>"

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

dict=FStoD() #stores dictionary under the name 'dict'

def dim():
    retStr=""
    retStr+= "<h1>Here are your results:</h1>"
    KeyL=dict.keys()
    ValueL=dict.values()
    if len(KeyL)==0:
        retStr+= 'Given no parameters! Please put parameters <b><i>"length", "width", and "height"</b></i> \
in the appropriate fields to see proper results!'
        retStr+= "<br>"
        return retStr
    if len(KeyL)==1: 
        try: ##MAKES SURE NUMERICAL VALUE GIVEN
            d1=float(dict[KeyL[0]])
            retStr+= "Given only ONE dimension! Feed me more dimensions, \
in the appropriate fields! Go back <a href=http://lisa.stuy.edu/~angela.lin/forms/dim3.html> here</a> to add more parameters!"
        except:
            retStr+="Did you insert numerical values? Maybe you should go back <a href=http://lisa.stuy.edu/~angela.lin/forms/dim3.html> here</a> \
and try again!"
        return retStr
    if len(KeyL)==2:
        try:##MAKES SURE NUMERICAL VALUE GIVEN
            d1=float(dict[KeyL[0]])
            d2=float(dict[KeyL[1]])
            a=d1*d2
            if a>0:
                retStr+= "Silly! Didn't you want dimensions of a volume? Given that you \
only gave me two dimensions, here is the area corresponding to those dimensions:"
                retStr+= "<br>"
                retStr+= str(a)
                retStr+= " squared units<br>"
                retStr+= "If you want the volume of something, please give \
parameters <b>'length', 'width', and 'height'!<b>"
                retStr+= "<br> Go back here to calculate the volume of something else: <a href=http://lisa.stuy.edu/~angela.lin/forms/dim3.html>Click here!</a>"
                return retStr
            else:
                retStr+="Oh dear, you inserted a negative value, or zero, didn't you?! Please go back and try again<a href=http://lisa.stuy.edu/~angela.lin/forms/dim3.html> here!</a>"
                return retStr
        except:
            retStr+= "Did you insert numerical values? Maybe you should go back <a href=http://lisa.stuy.edu/~angela.lin/forms/dim3.html> here</a> \
and try again!"
            return retStr
    if len(KeyL)==3:
        try:##MAKES SURE NUMERICAL VALUE GIVEN
            length=float(dict['length'])
            width=float(dict['width'])
            height=float(dict['height'])
            v=length*width*height
            if v>0:
                retStr+= "Congrats!! You have entered proper dimensions for a volume of a rectangular prism (or cube!) \
As a reward... <br><br><br>"
                retStr+= "The volume of a rectangular prism with your dimensions, "
                retStr+= "<b>length="
                retStr+= str(length)
                retStr+= " units, width="
                retStr+= str(width)+" "
                retStr+= "units, height="
                retStr+= str(height)+" units "
                retStr+= "</b><br>IS..."
                retStr+= "<br>"
                retStr+= str(float(v))
                retStr+= " cubed units! <br> AND... <br> <br> This is what a rectangular prism looks \
like!<br> <img src='cuboid.gif' alt='cuboid' width=400 height=275><br>"
                retStr+= "Want to recalculate? Go back <a href=http://lisa.stuy.edu/~angela.lin/forms/dim3.html> here</a>!"
                return retStr
            else:
                retStr+="Oh dear, you inserted a negative value, or zero, didn't you?! Please go back and try again<a href=http://lisa.stuy.edu/~angela.lin/forms/dim3.html> here!</a>"
                return retStr
        except:
            retStr+="Did you insert numerical values? Maybe you should go back <a href=http://lisa.stuy.edu/~angela.lin/forms/dim3.html> here</a> \
and try again!"
            return retStr
            return retStr
                            
# ~~~~~~~~~~~~~ HTML-generating code ~~~~~~~~~~~~~~
# <<< INSERT YOUR HTML HERE >>>

htmlStr +=str(dim())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# == Wrap up HTML string and send it to browser ===
htmlStr += "</font></body></html>"
print htmlStr 




