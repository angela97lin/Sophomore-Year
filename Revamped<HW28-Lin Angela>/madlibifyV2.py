#!/usr/bin/python

#print "Content-Type: text/html\n"

#print "" 

##Angela Lin
##pd 06
##HW28
##05-01-2013

#SUMMARY OF ALG:
#Oneof is basically a revamped version of our older oneOf, where it will return randomly, one of
##the elements in the list given. However, if the list does not contain any elements, it will return none.
##Dict_maker is another helper function which created a dictionary, d, so that each 'placeHolder' (ex: <VERBS>) will
##be a key, and each key will be assigned a list as a corresponding value.
#We can then ask for the value of a specific key and choose oneOf the elements in the list and replace it with the placeHolders in the story! :)

##Turns out get() was completely unnecessary; At first, I foolishly failed because I used d(a) instead of d[a] to extract the values...
#HUSKY is purposely capitalized@_@
import random

def oneOf(list):
    try:
        x=random.choice(list)
    except:
        x=None
    return x
#this is a helper function so our main function looks neater.

inStream= open('story.txt','r')
lines=inStream.readlines()  #LIST
inStream.close()
retString=""
for a in lines:
    retString+=a

def dict_maker():
    d={}
    i=0
    for line in open('words.csv').readlines():
        line=line.strip().split(',')
        while i+1<len(line):
            d[line[0]]=line[1:]
            i+=1
        i=0
    #print d
    return d

d=dict_maker()

def Madlibification(story,wordsF):
#####Rather than calling the helper function within the function, I returned d in the helper function so I can easily access it!
    story=story.replace(","," ,")
    story=story.replace("'"," '")
    story=story.replace("."," .")
    list=story.split(" ")
    list=list[:len(list)] #Deletes the random \n at the end of the list... (cleanup)
    open('words.csv').readlines()
    for a in d.keys(): #similar to old madlibify~
        while a in list:
            list[list.index(a)]=oneOf(d[a]) #d[a] will give the values corresponding to the key 'a'
            #^randomly replaces the placeHolder with a value from the certain placeHolder
        #print d.get(a)#tester~
            #print list
    string=" ".join(list)
    string=string.replace(" ,",",") ##CLEANUP FOR THE FINAL CODING!
    string=string.replace('"',"") ##More cleanup
    string=string.replace(" '","'")##Even more cleanup
    string=string.replace(" .",".")##etc...
    string=string.replace("  "," ")
    string=string.replace("\n","")#gets rid of random \n at end of code!
    return string #!!!!! :D


print Madlibification(retString,'words.csv')








