#!/usr/bin/python
# ========= HASHBANG LINE ABOVE IS MAGIC! =========
# ========= (Must be first line of file.) =========

# ======= BACK END OF AN HTML/PYTHON FORM PROCESSING TEAM ========
# Receives data from HTML front end, processes, generates new HTML.

##Angela Lin
##pd06
##HW36: Get Out the Vote
##05=30=13
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
r1=open('voters.txt','r')


def register():
    l=[]
    d={}
    taken="Username already taken! Please choose a new username!" 
    if 'username' not in dict.keys(): #no username given
        return "Oops! You forgot to type an username! Please try again."
    if 'password' not in dict.keys():#no password given
        return "Oops! You forgot to type a password! Please try again."
    if 'sleep' not in dict.keys():#no value for sleep given
        return "Oops! You forgot to answer the first question! Please try again."
    if 'like' not in dict.keys():
        return "Oops! You forgot to answer the second question! Please try again."
    if 'best' not in dict.keys():
        return "Oops! You forgot to answer the third question! Please try again."
    for line in r1.readlines(): #for every line of text
        sep=line.find(":")  #these next 4 lines basically create a dictionary
        sep2=line.find("'\'") #where each username is a key, with the password
        l.append(line[:sep])#as its value
        d[line[:sep]]=line[(sep+1):sep2]
    #return d[dict['username']]
    if dict['submit']=='register': #if user clicks 'register'
        if dict['username'] in l:
            return "Username already taken! Please choose a new username!"
        else:
            a1=open('voters.txt','a') #appends the username and pwd to voters.txt
            a1.write(dict['username'])
            a1.write(":")
            a1.write(dict['password'])
            a1.write("\n")
            return go()
    if dict['submit']=='submit': #if user clicks submit
        if dict['username'] not in l: #username not found
            return "Username not found. Are you registered?"
        if dict['username'] in l and d[dict['username']]==(dict['password']).strip():
            return go()
        elif dict['username'] in l and d[dict['username']]!=dict['password']:
            return "Username/Password combination not recognized!"#username is taken, but password is incorrect
  
li= open('voted.txt','r').read().split(",")
def record():##records all votes!
    a=open('votes.txt','a')
    r=open('votes.txt','r')
    a.write(str(dict['sleep'])+",")
    a.write(str(dict['like'])+",")
    a.write(str(dict['best'])+",")
    return analysis()
    
def go():
    if 'username' not in dict.keys():
	return "Username?"		
    if dict['username'] not in li:
        a1=open('voted.txt','a')
        a1.write(dict['username'])
        a1.write(",") #if user has not already voted, write username in voted.txt and save votes
        open('voted.txt','r').read().strip('\n')
        return record()
    else: #if user tries to vote twice.
        return "Sorry! You voted already."


def analysis(): #basically makes data look pretty and presentable in a horizontal bar graph :)
    retStr=""
    r=open('votes.txt','r')
    l=r.read().split(",")
    retStr+="Thank you for voting, "+dict['username']+"!"
    retStr+="<br> Here are the current results!<br>"
    retStr+="Q1: How many hours of sleep do you get per night?<br>"
    retStr+="10+ hours! "
    retStr+=str(l.count("10+")*"=")+"<br>"
    retStr+="8-10 hours! "
    retStr+=str(l.count("8-10")*"=")+"<br>"
    retStr+="6-8 hours! "
    retStr+=str(l.count("6-8")*"=")+"<br>"
    retStr+="4-6 hours! "
    retStr+=str(l.count("4-6")*"=")+"<br>"
    retStr+="2-4 hours! "
    retStr+=str(l.count("2-4")*"=")+"<br>"
    retStr+="1 hour! "
    retStr+=str(l.count("1")*"=")+"<br>"
    retStr+="What is sleep?"
    retStr+=str(l.count("none")*"=")+"<br><br><br>"
    retStr+="Q2:How much do you like being a Stuyvesant High School student?<br>"
    retStr+="I'd rather be anything else. "
    retStr+=str(l.count("no")*"=")+"<br>"
    retStr+="Eh. "
    retStr+=str(l.count("eh")*"=")+"<br>"
    retStr+="I don't really see the big deal... "
    retStr+=str(l.count("nodeal")*"=")+"<br>"
    retStr+="It's okay! "
    retStr+=str(l.count("okay")*"=")+"<br>"
    retStr+="It's fantastic! "
    retStr+=str(l.count("fantastic")*"=")+"<br>"
    retStr+="I COULDN'T BE HAPPIER!SFSRYYUTYJMMN!!!! "
    retStr+=str(l.count("SUPER")*"=")+"<br><br><br>"
    retStr+="Q3: Who is the best?<br>"
    retStr+="I am! "
    retStr+=str(l.count("i")*"=")+"<br>"
    retStr+="Mr. Brown, of course! "
    retStr+=str(l.count("brown")*"=")+"<br>"
    retStr+="Narwhals "
    retStr+=str(l.count("narwhals")*"=")+"<br>"
    retStr+="What is going on... "
    retStr+=str(l.count("what")*"=")+"<br><br><br>"
    return retStr
    
    
    
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ========= CONTENT-TYPE LINE REQUIRED. ===========
# ======= Must be beginning of HTML string ========
                
htmlStr = "Content-Type: text/html\n\n" #NOTE there are 2 '\n's !!! 
htmlStr += "<html><head><title>Voting Booth Results</title></head></html>\n"
htmlStr += "<body>"


# ~~~~~~~~~~~~~ HTML-generating code ~~~~~~~~~~~~~~
# <<< INSERT YOUR HTML HERE >>>
# for example,

htmlStr += str(register())



        
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# == Wrap up HTML string and send it to browser ===
htmlStr += "</body></html>"
print htmlStr
