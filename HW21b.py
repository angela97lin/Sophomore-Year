
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

def Madlibification(story):
    story.replace(',',' ,')
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
            newStory.replace(" ,",",")
    return newStory 




 
s1= "In <COUNTRY> , the <NOUN> covers <HERO> 's disclosure of his identity as Iron Man. Ivan Vanko, whose <NOUN> <VILLAN> has just <PASTV> , sees this and begins building a <NOUN> similar to <HERO> 's. <TIME> later, <HERO> has used his <NOUN> to help maintain world peace. He <VERB> the <HERO> Expo in <COUNTRY> to continue his <NOUN> 's legacy. <POSITION> <NAMES> <VERB> that <HERO> turn over the Iron Man <NOUN> to the <NOUN> . <HERO> refuses, claiming that <NOUN> and <NOUN> are <TIME> away from <VERBING> his <NOUN> , and that it is his property. The <NOUN> in the arc reactor that keeps <HERO> alive and <VERB> the <NOUN> is <ADVERB> <VERBING> him, and he has <PASTV> to find a <NOUN> . Growing <ADVERB> <ADJ> and <ADJ> due to his impending death, and <VERBING> not to tell anyone about his <NOUN> , Stark <VERB> his <POSITION> <HERO> CEO of Stark Industries, and replaces her with <POSITION> <NAMES> . While <HERO> is <VERBING> at the <COUNTRY> , he is attacked by <VILLAN> , who uses his <NOUN> to <VERB> <ADJ> <NOUN> . <HERO> <VERB> <VILLAN> with the aid of his <ADJ> <NOUN> ."

print Madlibification(s1)

















