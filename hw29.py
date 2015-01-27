#Angela Lin
##pd 06
##HW29
##05=06=13/05=07=13

##Write a Python script that will read in a literary work of appreciable length and print its 30 most frequently occurring words.
##
##General guidelines:
##Place your files in a folder named “hw29-<Last First>”, then compress this folder into a ZIP archive. (no RAR!)
##Upload to the homework server.
##Include heading and descriptive in-line comments.
##
##Outline of approach:
##Download a TXT file (from gutenberg.org or other source for public domain works)
##Manually curate text (remove intro & end text)
##Create list of “words” separated by whtspc
##Automate some curating:
##Convert words to lowercase   (  s.lower()  )
##Strip words of their punctuation
##Create a dictionary key for each word, with its value being that word's frequency in text
##Print top 30 most frequently occurring words along with each's frequency
##
##Deliverables:
##<chosen work of lit>.txt
##freq30.py

##From my data analysis, I realized that there are waaaay too many pronouns and
##useless common day words. Even when I asked for the top 100 most frequent words,
##many, if not all, were not really useful words.
##After typing a huge number however, I began to see results such as "golden","king",
##"jason","midas", etc. This has led me to conclude, without reading the text,
##that the author has probably found Jason and the Golden Fleece and King Mida's story
##as one of the most important myths that children should know. Pronouns and names seem
##to appear much more frequently than general verbs, such as 'person' (showed up only 24 times)
##or 'guests.'
##What really surprised me was that "zeus" only came up 23 times, since most myths
##involve a conflict caused by Zeus's affairs with Hera.
x=input("Insert Desired Num. Freq Here:")

def inputFunc():
    try:
        x
    except:
        print "Nope!"

inputFunc()

def textextract():
    retString=""
    FINALStr=""
    retList=[]
    d={}
    numofVal=0
    for line in open("myths.txt").read().strip(".,;()"):
        retString+=line
    retString=retString.replace("(","")
    retString=retString.replace(")","")
    retString=retString.replace(".","")
    retString=retString.replace(",","")
    retString=retString.replace(";","")
    retString=retString.replace("!","")
    retString=retString.replace("?","")
    retString=retString.replace("[","")
    retString=retString.replace("]","")
    retString=retString.replace(":","")
    retString=retString.replace('"','') #Couldn't get strip to work, so I used replace 
    retString=retString.replace("'","")#for each punctuation.
    retString=retString.replace("_","")
    retString=retString.replace("-"," ")
    retString=retString.lower()
    retString.strip()
##    retString.strip('"')
##    retString.strip(".")
##    retString.strip("().;'")
    retString=retString.replace("\n"," ")
    #print retString
    retList=retString.split(" ")
    for each in retList:
        if each=="":
            retList.remove("") #SLOWS DOWN MY CODE SO MUCH!
    #print retList
    for a in retList:
        if d.has_key(a):
            d[a]+=1  #same approach as below, but only runs through the text file once!
        else:
            d[a]=1
##        if d.has_key(a)==False:
##            d[a]=0 ##if a is not a key in d, make it a key with an assigned value of 0
    #print d.values()
    #print d.keys()
    ##for a in retList: #2nd runthrough! This time, every time the same word is encountered, return add to the value of d[a] by 1
       ## d[a]+=1 [THIS WAS MY INITIAL CODING!
    #print d.values()
    freqL=d.values()
    freqCorrespond=d.keys()
    while numofVal<=x:
        maxV=max(freqL)
        #print maxV
        #print freqL
        FINALStr+=str(maxV)+" "+str(freqCorrespond[freqL.index(maxV)])+"\n" #appends the freq, the word, and \n
        freqCorrespond=freqCorrespond[:freqL.index(maxV)]+freqCorrespond[(freqL.index(maxV)+1):] #slices lists to delete the previous max values
        freqL=freqL[:freqL.index(maxV)]+freqL[freqL.index(maxV)+1:]
        numofVal+=1
    return FINALStr
        

print textextract()
