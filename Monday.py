import random

#random.randrange(n) returns a random integer from 0 to n-1, inclusive
#eg, random.randrange(3) will return either 0, 1 or 2 with equal probability

print random.randrange(3)


##Note how the strings below can be used to represent components of an ASCII face.
##
##Generate several more of each component. The more the better!
##
##Write a function called randFace that will return a randomly generated face
##by combining randomly chosen components.


import random



hair= [ " ''''' ", "@@@@@", "~~~~~", "[[[[[", "=====", ".....", "mmmmm"]
eyes= [ " o o ", " o O ", " @ @ ", " ~ ~ ", " e e ", " T T ", " X X "]
noses= [ "  0  ", "  v  ", "  I  ", "  x  " ]
mouths= [ " XXX ", "-----", "  _  ", " ~~~ ", " www "]
placeH= ["HAIR", "EYES", "NOSES", "MOUTHS"]


def oneOf(list):
    s=random.randrange(len(list))
    return list[s]
    

def randFace():
    finalR=""
    for a in placeH:
        if a == "HAIR":
            finalR+=oneOf(hair) + "\n"
        elif a == "EYES":
            finalR+=oneOf(eyes) + "\n"
        elif a == "NOSES":
            finalR+=oneOf(noses) + "\n"
        elif a == "MOUTHS":
            finalR+=oneOf(mouths) + "\n"
    return finalR


print randFace()
    


randFace()

