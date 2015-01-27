##Angela Lin
##pd06
##HW21
##04/09/13
import random
adjs=["red", "joyful", "excited","lazy","wondertastic", "superior"]
nouns=["cow", "student", "monkey", "penguin","HUSKY", "lax player"]
verbs= ["flies", "karate kicks", "facepalms", "swings", "sleeps","cries"]
adverbs=["quickly","swiftly", "stealthly", "stupidly","slowly","weee-ly","boringly"]

##Mechanism for Madlibification:

#Peer-reviewed (ish) by Gabriel

#I wanted to first change the 'story' by changing the
#story string into a list, split by the spaces.
#Then, I replaced every element in list that was in placeHolders
#until placeHolders was an empty list...

placeHolders=["<ADJ>","<NOUN>","<VERB>","<ADVERB>"]
pH=[adjs, nouns, verbs, adverbs]
def fillinBlanks(story):
    i=0
    pH=[adjs, nouns, verbs, adverbs]
    placeHolders=["<ADJ>","<NOUN>","<VERB>","<ADVERB>"]
    list=story.split(' ') #converts story into a list of words from the story
    while i<=len(list) and placeHolders!=[] and pH!=[]:
        if list[i] in placeHolders: #if the current element is <ADJ> or <NOUN> or anything of that kind...
            list[i]=pH[0][random.randrange(6)] #chooses a random element from the current first element of pH
            pH=pH[1:] #slices off the first element of pH
        else:
            i+=1 #otherwise, move on!
    return " ".join(list) #return the joined list, with spaces 'sticking' the elements together.
            
print fillinBlanks("A <ADJ> <NOUN> <VERB> <ADVERB> upside down!")
