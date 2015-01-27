#Angela Lin
#pd 06
#HW 08
#2013-02-27

##
##1. gradeConv(g) takes a numeric input g, representing a student’s grade, and returns its letter grade equivalent, according to this breakdown:
##
##A: 90-100
##B: 80-89
##C: 70-79
##D: 65-69
##F: 0-64
##
##e.g.,
##< Generate your own test cases. Pay close attention to border cases... >
##
##2. passJudgement(letterGrade) takes a string input letterGrade and prints congratulatory or scolding messages.
##

def gradeConv(g):
    if g>=90 and g<=100:
        return "A"
    elif g>=80 and g<90:
        return "B"
    elif g>=70 and g<80:
        return "C"
    elif g>=65 and g<70:
        return "D"
    elif g<=64 and g>=0:
        return "F"
    else: return "Please come see me for an accurate grade."

gradeConv(20)
#Should be F
gradeConv(65)
#Should be D
gradeConv(69)
#Should be D
gradeConv(70)
#Should be C
gradeConv(79)
#Should be C
gradeConv(80)
#Should be B
gradeConv(89)
#Should be B
gradeConv(90)
#Should be A
gradeConv(100)
#Should be A
gradeConv(89.5)
#Should be B
gradeConv(101)
#Should be "Please come see me for an accurate grade."
#This case is just for fun...Assuming gradeConv takes in a numeric input, g, that is less than 0 or greater than 100, something must be wrong.
##Although it seems like there are many test cases, it is crucial to test what happens when gradeConv is given a value between the intervals of two grades.
##For this assignment, I have decided to make everything "in between" the interval the next lower grade. For example, I made 89.5, which is between intervals A and B, a "B" rather than an A.




def passJudgement(letterGrade):
    if letterGrade=="A":
        print "Well Done! Keep up the good work! :)"
    elif letterGrade=="B":
        print "Satisfactory job!"
    elif letterGrade=="C":
        print "Please work to do better."
    elif letterGrade=="D":
        print "Please come see me. You are in danger of failing."
    elif letterGrade=="F":
        print "You are failing. Your parents will be immediately notified; Let's talk about how to improve!"

passJudgement("A")
passJudgement("B")
passJudgement("C")
passJudgement("D")
passJudgement("F")
#passJudgement takes a STRING input and returns a comment based on what the string input was.
#These test cases basically test all of the inputs possible (assuming the user does not insert a random letter, such as Z)

        
    
