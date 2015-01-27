#Angela Lin, Tanvir Nadim, Farib Mohammed Khan(Team Pyth0nF.A.T)
#Period 6
#Homework 14
#2013-3-12


##1. rot13Chr(ch) takes a single-letter string input and returns its rot13 equivalent.
##e.g.,
##rot13Chr(‘B’) -> ‘O’
##rot13Chr(‘b’) -> ‘o’

def rot13Chr(ch):
    if ord(ch)<ord('N'): # checks that function is between A and N
     c=ord(ch)+13 #rot13 shifts 13 letters on the alphabet
    elif ord(ch)<ord('n') and ord(ch)>ord('Z'): #checks if the letter is between 'a' and 'n'
     c=ord(ch)+13
    else:
         c=ord(ch)-13 #for all other characters, rot13 shifts 13 letters back, rather than forward
    return chr(c)

#TEST CASES FOR THE ENTIRE ALPHABET:
print rot13Chr('a')#n
print rot13Chr('b')#o
print rot13Chr('c')#p
print rot13Chr('d')#q
print rot13Chr('e')#r
print rot13Chr('f')#s
print rot13Chr('g')#t
print rot13Chr('h')#u
print rot13Chr('i')#v
print rot13Chr('j')#w
print rot13Chr('k')#x
print rot13Chr('l')#y
print rot13Chr('m')#z
print rot13Chr('n')#a
print rot13Chr('o')#b
print rot13Chr('p')#c
print rot13Chr('q')#d
print rot13Chr('r')#e
print rot13Chr('s')#f
print rot13Chr('t')#g
print rot13Chr('u')#h
print rot13Chr('v')#i
print rot13Chr('w')#j
print rot13Chr('x')#k
print rot13Chr('y')#l
print rot13Chr('z')#m
print rot13Chr('A')#N
print rot13Chr('B')#O
print rot13Chr('C')#P
print rot13Chr('D')#Q
print rot13Chr('E')#R
print rot13Chr('F')#S
print rot13Chr('G')#T
print rot13Chr("H")#U
print rot13Chr("I")#V
print rot13Chr("J")#W
print rot13Chr("K")#X
print rot13Chr("L")#Y
print rot13Chr("M")#Z
print rot13Chr("N")#A
print rot13Chr("O")#B
print rot13Chr("P")#C
print rot13Chr("Q")#D
print rot13Chr("R")#E
print rot13Chr("S")#F
print rot13Chr("T")#G
print rot13Chr("U")#H
print rot13Chr("V")#I
print rot13Chr("W")#J
print rot13Chr("X")#K
print rot13Chr("Y")#L
print rot13Chr("Z")#M

##
##2. printEmAll() prints all letters of the alphabet along with the rot13 equivalent of each.
##e.g.,
##printEmAll()
##A <-> N
##B <-> O
##...
##a <-> n
##b <-> o
##...and so on


def printEmAll():
    C=ord("A")
    c=ord("a")
    Cret="" #begin with two empty strings
    cret=""
    while C<ord("Z"): #as long as C, which begins with ord("A") is less than ord("Z"), meaning this case takes care of uppercase letters...
        Cret+= str(chr(C))+"-> "+str(rot13Chr(chr(C)))+'\n' #we add to Cret chr(C), then its rot13Chr value
        C=C+1 #used to go up the alphabet, using ASCII
    while c>=ord("a") and c<=ord("z"): #as long as c, which begins with ord("a") is less than ord("z"), meaning this case takes care of lowercase letters...
            cret+= str(chr(c))+"->"+str( rot13Chr(chr(c)))+'\n'#we add to cret chr(c), then its rot13Chr value
            c=c+1#used to go up the lowercase alphabet using ASCII coding
    print Cret+cret #finally, we print the 'summation' of Cret and cret


printEmAll()
##should print...
##B<->O
##C<-> P
##D<->Q
##E<->R
##F<->S
##G<->T
##H<->U
##I<->V
##J<->W
##K<->X
##L<->Y
##M<->Z
##N<->A
##O<->B
##P<->C
##Q<->D
##R<->E
##S<->F
##T<->G
##U<->H
##V<->I
##W<->J
##X<->K
##Y<->L
##a<->n
##b<->o
##c<->p
##d<->q
##e<->r
##f<->s
##g<->t
##h<->u
##i<->v
##j<->w
##k<->x
##l<->y
##m<->z
##n<->a
##o<->b
##p<->c
##q<->d
##r<->e
##s<->f
##t<->g
##u<->h
##v<->i
##w<->j
##x<->k
##y<->l
##z<->m


##3. rot13(word) takes a string input (all caps, no spaces) and returns its rot13 encoding.
##e.g.,
##rot13(“JABBERWOCKY”)-> “WNOOREJBPXL”

def rot13w(word):
    a=0 #set a as the index we can use... a begins at 0 because we count indices from 0
    newWord=""#makes an empty string
    while len(word)>0 and a<len(word):
        newWord+=str(rot13Chr(word[a])) #this 'adds' the rot13Chr of the current index to our string newWord
        a+=1 #adds one to the index until it is greater than the length of the string, in which case, we stop the while loop
    return newWord #returns the new, rot13 version of the word!

print rot13w("JABBERWOCKY")#WNOOREJBPXL
print rot13w("MAGICAL")#ZNTVPNY

##4. rot13(phrase) takes a string input -- potentially including spaces and a mixture of upper- and lowercase letters -- and returns its rot13 encoding.
##e.g.,
##rot13(“Justin Bieber”) -> “Whfgva Ovrore”

def rot13 (phrase):
    howfarin = 0 #gives index of current character
    length = len(phrase) 
    newphrase = "" #begins the new phrase with an empty string
    while howfarin < length: #while the current index is not out of the string's range...
        if phrase [howfarin] == " ": #if the current character is a string...
            newphrase += " " #we append a space into the new phrase
            howfarin += 1 #move onto the next character!
        elif ord (phrase [howfarin]) < 65 or ord (phrase [howfarin]) > 122 or ord (phrase [howfarin]) > 90 and ord (phrase [howfarin]) < 97: #if the character is punctuation,
                newphrase += phrase [howfarin] #simply add the punctuation to the string and...
                howfarin += 1 #move to the next character!
        else: #otherwise, append the rot13Chr version of the current letter
            newphrase += rot13Chr(phrase[howfarin])
            howfarin += 1
    return newphrase #returns the new, rot13Chr version of the current phrase after howfarin is beyond the length of the string! 

print rot13 ("Justin Bieber") #"Whfgva Ovrore"
print rot13 ("Topher Brown Mykolyk") #"Gbcure Oebja Zlxbylx"
print rot13("Justin Bieber? Like, OMG!!! He's my hero!") #Whfgva Ovrore? Yvxr, BZT!!! Ur'f zl ureb!

#attempt at challenge (not a success)

def rotChr(ch):
    x=3 
    while ord(ch)>=ord("A") and ord(ch)<=ord("Z"):
        if ord(ch)<ord("Z")-x:
            return chr(ord(ch)+x)
        else:
            return chr(ord(ch)-x)
    while ord(ch)>=ord("a") and ord(ch)<=ord("z"):
        if ord(ch)<ord("z")-x:
            return chr(ord(ch)+x)
        else:
            return chr(ord(ch)-x)


       
print rotChr("d")
print rotChr("e")
print rotChr("o")
print rotChr("h")
print rotChr("z")
