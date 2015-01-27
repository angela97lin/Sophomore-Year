#Angela Lin
#pd 06
#03-15-13
#HW15

##Pig Latin Rules:
#1. If a word begins with a constant or constant sounds, move all constants
#to the end of the word and then add "ay."
#For example, "the" becomes "e-th" and "star" becomes "ar-stay"
#
#2.If a word begins with a vowel, simply add "ay" to the word.
#For example, "itch" becomes "itch-ay."
#3. If the word does not contain a vowel, then just return the word and "-ay" at the end.

#Summary Of Approach:
#First, a global variable, "vowels" was set up so that we can easily check where the first vowel is (or if it has any vowels at all).
#Then, I implemented pigLatinWord that would convert an English word into Pig Latin.
#Next, I created a helper function called countSpaces that could count the number of spaces in a phrase...
#Finally, using all of these helper functions, I was able to create a working code that will translate normal English into Pig Latin!

vowels="AEIOUaeiou" #helpful global variable


def pigLatinWord(word):
    currentIndex=0 
    newWord=""
    if vowels.find(word[0])!=-1:#if the first letter of the word is a vowel, return the original word and add "-ay"
        newWord=word+"-ay"
        return newWord
    while currentIndex<len(word) and vowels.find(word[currentIndex])==-1:#if the current character is NOT a vowel, move onto the next character!
        currentIndex+=1
    while currentIndex<len(word) and vowels.find(word[currentIndex])!=-1: #if the current character IS a vowel and has an index != 0, then
        #append all of the letters after the current index, followed by all of the characters before the current index, followed by "-ay"
        newWord+= word[currentIndex:]+word[:currentIndex]+"-ay"
        return newWord #return the newWord!
    if currentIndex==len(word): #if the currentIndex is beyond the length of the string, then there are no vowels in
        #that word and thus, append the "-ay" to the word and return the newWord
        newWord=word+"-ay"
        return newWord

print pigLatinWord("Sushi") #ushiS-ay
print pigLatinWord("Apple")#Apple-ay
print pigLatinWord("my") #my-ay




def countSpaces(phrase):
    spaces=0
    index=0
    while phrase.find(" ")!=-1 and index<len(phrase): #if there is a space in the phrase and the index is less than the phrase...
        spaces+=1 #add one to the counter
        phrase=phrase[phrase.find(" ")+1:] #shorten the phrase to 'delete' the first space and everything before it
        index=len(phrase[:phrase.find(" ")]) #the index is set to the length of the first word in the new phrase
    return spaces

print countSpaces("I baked cookies tonight!")#3
print countSpaces("Moonlight")#0
print countSpaces("Quack quack quack quack quack")#4
print countSpaces("I like to  dance")#4




def translate(phrase):
    retPhrase=""
    currentIndex=0
    while countSpaces(phrase)!=0 and currentIndex<len(phrase): #if there are spaces in the phrase...
        retPhrase+=pigLatinWord(phrase[:phrase.find(" ")])+" " #append to retPhrase the first word, Pig-Latin-ified
        phrase=phrase[phrase.find(" ")+1:] #set phrase as the phrase with, essentially, the first word 'deleted'
        currentIndex=len(phrase[:phrase.find(" ")])
    retPhrase+=pigLatinWord(phrase) #if the phrase has no spaces, it must only be a word
    #thus, Pig-Latin-ify the last word of the phrase and append it to retPhrase
    return retPhrase

print translate("The pope rocks red kicks")
print "should be..."
print "eTh-ay opep-ay ocksr-ay edr-ay icksk-ay"
print translate("The cookies that my friend made were burnt")
print "should be..."
print "eTh-ay ookiesc-ay atth-ay my-ay iendfr-ay adem-ay erew-ay urntb-ay"
