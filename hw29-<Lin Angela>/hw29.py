#Angela Lin
##pd 06
##HW29
##05=06=13

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

def textextract():
    retString=""
    FINALStr=""
    retList=[]
    d={}
    numofVal=0
    for line in open("myths.txt").readlines():
        retString+=line
    retString=retString.replace("(","")
    retString=retString.replace(")","")
    retString=retString.replace(".","")
    retString=retString.replace(",","")
    retString=retString.replace(";","")
    retString=retString.replace('"','') #Couldn't get strip to work, so I used replace 
    retString=retString.replace("'","")#for each punctuation.
    retString=retString.replace("_","")
    retString=retString.replace("-"," ")
    retString=retString.lower()
    retString=retString.strip()
    retString=retString.replace("\n"," ")
    retList=retString.split(" ")
    print retList
    for a in retList:
        if d.has_key(a)==False:
            d[a]=0 ##if a is not a key in d, make it a key with an assigned value of 0
    #print d.values()
    #print d.keys()
    for a in retList: #2nd runthrough! This time, every time the same word is encountered, return add to the value of d[a] by 1
        d[a]+=1
    #print d.values()
    freqL=d.values()
    freqCorrespond=d.keys()
    while numofVal<=30:
        maxV=max(freqL)
        #print maxV
        #print freqL
        FINALStr+=str(maxV)+" "+str(freqCorrespond[freqL.index(maxV)])+"\n" #appends the freq, the word, and \n
        freqCorrespond=freqCorrespond[:freqL.index(maxV)]+freqCorrespond[(freqL.index(maxV)+1):] #slices lists to delete the previous max values
        freqL=freqL[:freqL.index(maxV)]+freqL[freqL.index(maxV)+1:]
        numofVal+=1
    return FINALStr
        

print textextract()
