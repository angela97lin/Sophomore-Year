#!/usr/bin/python

print "Content-Type: text/html\n"

print "" 

##Angela Lin
##pd 06
##HW22
##04-10-13

#Partner: Gabriel DelVecchio

import random
adjs=["red", "joyful", "excited","lazy","wondertastic", "superior"]
nouns=["cow", "student", "monkey", "penguin","HUSKY", "lax player"]
pluralN=["cows", "octopi", "monsters", "pokemon", "donkeys", "monkeys"]
verbs= ["flies", "karate kicks", "facepalms", "swings", "sleeps","cries"]
adverbs=["quickly","swiftly", "stealthly", "stupidly","slowly","weee-ly","boringly"]
placeHolders=["<ADJ>","<NOUN>","<VERB>","<ADVERB>","<COUNTRY>","<NAMES>","<PLURALN>","<VILLAN>","<VERBING>","<POSITION>","<HERO>","<TIME>","<PASTV>","<OBJECTS>"]
countries=["Japan","Great Britain","China","Cuba","Russia","Spain","Madagascar"]
hero=["Tony Stark"]
names=["Johnny Depp","Phillip Wang", "Edison Shi", "Adam Scott"]
pastV=["farted","flew","died","swung","dived"]
objects=["donuts","cookies","salads","paper","books","balls","jumping jacks"]
time=["5129302 days","60 months","1 day","10 seconds"]
position=["President","Lax player","Senator",]
VERBing=["loving","killing","destroying","wacking","flying"]
villan=["Vanko"]
def oneOf(list):
    return list[random.randrange(len(list))]
#this is a helper function so our main function looks neater.

inStream= open('story.txt','r')
lines=inStream.readlines()  #LIST
inStream.close()
retString=""
for a in lines:
    retString+=a



def Madlibification(story):
    story=story.replace(","," ,")
    story=story.replace("."," .")
    story=story.replace("'"," '")
    list=story.split(" ")
    for a in placeHolders: #for every element in placeHolders
        while a in list: #while the element is in list
            if a=="<NOUN>": #if the element is a noun, switch <NOUN> with a randomized noun
                list[list.index(a)]=oneOf(nouns)
            elif a=="<VERB>":#if the element is a verb, switch <VERB> with a randomized verb
                list[list.index(a)]=oneOf(verbs)
            elif a=="<ADJ>":#if the element is an adjective, switch <ADJ> with a randomized adjective
                list[list.index(a)]=oneOf(adjs)
            elif a=="<ADVERB>":#if the element is a adverb, switch <ADVERB> with a randomized adverb
                list[list.index(a)]=oneOf(adverbs)
            elif a=="<COUNTRY>":#if the element is a country, switch <COUNTRY> with a randomized country
                list[list.index(a)]=oneOf(countries)
            elif a=="<HERO>":
                list[list.index(a)]=oneOf(hero)
            elif a=="<PASTV>":
                list[list.index(a)]=oneOf(pastV)
            elif a=="<OBJECTS>":
                list[list.index(a)]=oneOf(objects)
            elif a=="<TIME>":
                list[list.index(a)]=oneOf(time)
            elif a=="<POSITION>":
                list[list.index(a)]=oneOf(position)
            elif a=="<VERBING>":
                list[list.index(a)]=oneOf(VERBing)
            elif a=="<PLURALN>":
                list[list.index(a)]=oneOf(pluralN)
            elif a=="<NAMES>":
                list[list.index(a)]=oneOf(names)
            elif a=="<VILLAN>":
                list[list.index(a)]=oneOf(villan)
            newStory=" ".join(list)
            newStory=newStory.replace(" ,",",")
            newStory=newStory.replace(" .",".")
            newStory=newStory.replace(" '","'")
    return newStory 


print "This is the madlibified verison of an Iron Man summary:\n"
print Madlibification(retString)








