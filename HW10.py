
#Angela Lin, Tanvir Nadim, Farib Khan (Team FAT)
#pd 06
#HW10b
#2013-03-05

##1. addMultPrint(a,b) takes 2 numeric inputs and prints a message like that shown below.
##addMultPrint(3,6) → 
##“the sum of 3 and 6 is 9
##their product is 18”
##
##2. addMultHTML(a,b) takes 2 numeric inputs and returns a string of HTML code that will render as shown below.
##addMultHTML(3,6) → 
##the sum of 3 and 6 is 9 
##their product is 18

##Although addMultHTML and addMultPrint were done differently than presented in class, they are working functions and thus, remained relatively unchanged.
##Tablefy(a,b) was a different story. Instead of previously taking the easy route and printing the HTML code, tablefy was modified so that
#a state variable, tfy, was initially assigned "" (an empty string). Then, the basic HTML coding for a table was created and "added" onto the
#empty string. While a<=b, tablefy would create another row in the HTML table with an updated a, a**2, and sumDigits(a),and then set a=a+1 until a>b.
#At that point, "</table>" would be added to the current tfy string, closing the table tag and successfully creating a table.
#This was different from the initial coding as tfy was a variable used; we built onto tfy and in the end, simply returned tfy, instead of
#printing the entire table at the very end. Creating and using a new variable was very crucial and made the coding much more flexible.


def addMultPrint(a,b):
    sum=a+b
    product=a*b
    print "the sum of "+str(a)+" and "+str(b)+" is "+str(sum)
    print "their product is "+str(product)

##in order to create a string sentence, it is important to use the + to 'add' the strings.
#If the variable is not a string, it must be made a string by enclosing it in str(n).

#Test Cases:
addMultPrint(1,3)
print "...should be"
print "the sum of 1 and 3 is 4"
print "their product is 3"
addMultPrint(10,10)
print "...should be"
print "the sum of 10 and 10 is 20"
print "their product is 100"




def addMultHTML(a,b):
    sum=a+b
    product=a*b
    return "the <i>sum</i> of "+str(a)+" and "+str(b) +" is <b>"+str(sum)+"</b><br>"+" their <i>product</i> is <b>"+str(product)+"</b>"

#addMultHTML takes a and b and generates a HTML code where the word "sum" and "product"
#are in italics and the sum and product of the two numbers are in bold.
#Test Cases:
print addMultHTML(3,6)
print "...should be"
print "the <i>sum</i> of 3 and 6 is <b>9</b><br>"
print "their <i>product</i> is <b>18</b>"
print addMultHTML(2,10)
print "...should be"
print "the <i>sum</i> of 2 and 10 is <b>12</b> <br>"
print "their <i>product</i> is <b>12</b>"





def sumDigits(n):
    sum=0
    while n>0:
        sum=(n%10)+sum
        n=(n//10)
    return sum+n


def tablefy(a,b):
    tfy=""
    tfy+= "<table border=1><tr><td><b>n</td><td>n^2</td><td>sumDigits</td></tr>" #sets up the essential coding for table
    while a<=b:
        tfy+= "<tr><td>"+str(a)+"</td><td>"+str(a*a)+"</td><td>"+str(sumDigits(a))+"</td></tr>"
        a=a+1
    tfy+= "</table>" #ends or closes the table tag
    return tfy


print tablefy(2,5)
print "should be..."
print "<table border=1><tr><td><b>n</td><td>n^2</td><td>sumDigits</td></tr><tr><td>2</td><td>4</td><td>2</td></tr><tr><td>3</td><td>9</td><td>3</td></tr><tr><td>4</td><td>16</td><td>4</td></tr><tr><td>5</td><td>25</td><td>5</td></tr></table>"
#Tablefy first sets up the coding of a table in HTML...
#I was unable to get the squaren to change and as a result, n^2 remained 4...
