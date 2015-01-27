#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

stream=open('scores.csv', 'r') 
readas=stream.read()
stream.close()
#print readas #just used to double check what readas returns
beginText='Although we North-easterners might argue that the Northeastern United states holds the best K-12 educational systems and therefore produces the best testing-results and send off students to the best colleges, this set of data begs to differ. Although the prestigious Ivy-League universities have carved their stay in the confines of the North-Eastern United states, they Ivy-bound SAT scores have not. A careful analysis of this averaged data set containing scored from the states separated into Regions of the United States, the North-Eastern United states is actually the lowest of the 4 regions. However, this does not mean that the North-East is the dumbest regions of the USA. Although the NorthEast retains the lowest average SAT scores, the overall percentage of students taking the SATs in the NE United States towers over the amount of students taking the test in other parts of the country with a whoping 81.4%. In this case, it is logical to persume that although the average is low, students from all knowledge areas and skill levels are taking time to take this test, whereas in other parts of the US where the SAT test taking percentage is rather low, maybe only students that are in the top percentile or at least confident in their abilities are taking the test, therefore making these results a rather population-based thinking puzzle.'
beginText2='This same analyzation of data goes for the averaged results of ACT scores in the US. Although the Northeast skyrockets above the other regions of the U-s-and-A, only a meager 14.6% of NE United States students actually take the ACT, whereas up to 65 percent of students in other parts of the USA take this exam. Therefore, it is reasonable to conclude that Higher SAT/ACT scores cannot account for how well an educational system functions in a certain are of the United States, nor can it account for how smart students heiling from a certain region of the United States are, since none of these data values can account for results shown by 100% of the regional student body, but rather only a select percentage.'
beginText3='Therefore, it is unreasonable to declare that SAT scores can determine the knowledge and perception of students based on where they live and recieve education. Although these facts do prove for an interesting statistic, the fact that not all students take this test hinders the proper conclusion of academic knowledge and advantage in a realistic sense. As one may say, "If the apple of top looks fresh, the ones underneath it may as well be rotten."'
text="<br><br><br>We had much difficulty trying to ground ourselves in interesting and unique data. At first, we had planned to take Starbucks locations, their given longitude and latitude coordinates, and construct a map on/using Google Maps to visually represent our data."
textH="When that proved to be too challenging, we decided to compare the SAT and ACT scores of the four major regions of the United States: Northeast, Midwest, South, and West. "
textH2="One of the many difficulties we encountered was trying to use Python very effiently to run our code with a for/while loop. "
textH3="Because we were not necessarily successful with this approach, we opted to repeat the same code four times, once for each region instead. Thus, the length of the code is much longer than expected."
text01="<br><br>Lost?<br>Return to raw data <a href=http://lisa.stuy.edu/~angela.lin/data01.py>here!</a>"
textCon="In the future, I want to be able to compare two data tables as my partner and I had proposed, so that we can see if there is any correlation between the two sets of data. For example, we wanted to observe whether or not economy had an effect of education by comparing"
textCon2="the average SAT/ACT scores with the amount of funding each state receives from the government to see if there are any relationships between money/funding and education.<br><br><br>"
Northeast=["Maine","New Hampshire", "Vermont","Massachusetts","Rhode Island","Connecticut","New York","Pennsylvania","New Jersey"]
Midwest=["Wisconsin","Michigan","Illinois","Indiana","Ohio","Missouri","North Dakota","South Dakota","Nebraska","Kansas","Minnesota","Iowa"]
South=["Delaware","Maryland","District of Columbia","Virginia","West Virginia","North Carolina","South Carolina","Georgia","Florida","Kentucky","Tennessee","Mississippi","Alabama","Oklahoma","Texas","Arkansas","Louisiana"]
West=["Idaho","Montana","Wyoming","Nevada","Utah","Colorado","Arizona","New Mexico","Alaska","Washington","Oregon","California","Hawaii"]

##One problem we encountered was the use of string.find() when states have different amount of letters,
##Heading got stuck in code
NortheastSum=[0,0,0,0,0,0,0,0,0,0,0,0]
MidWestSum=[0,0,0,0,0,0,0,0,0,0,0,0]
SouthSum=[0,0,0,0,0,0,0,0,0,0,0,0]
WestSum=[0,0,0,0,0,0,0,0,0,0,0,0]
NEAverage=[]
MWAverage=[]
SAverage=[]
WAverage=[]
AVGHolders=[NEAverage,MWAverage,SAverage,WAverage]
NAMES=["Northeast", "MidWest", "South", "West"]
def analysis():
    ret=readas.splitlines()
    #print ret
    ret=ret[1:]
    #print ret #checks that heading is gone
    for x in ret:
        index=0
        state=x[:x.find(",")]
        if state in Northeast:
            x=x.split(",") #splits by commas: basically, each column in the .csv file will become a separate string within the list
            x=x[1:]
            while index<len(x):
                NortheastSum[index]+=float(x[index])
                index+=1
        if state in Midwest:
            x=x.split(",") #splits by commas: basically, each column in the .csv file will become a separate string within the list
            x=x[1:]
            while index<len(x):
                MidWestSum[index]+=float(x[index])
                index+=1
        if state in South:
            x=x.split(",") #splits by commas: basically, each column in the .csv file will become a separate string within the list
            x=x[1:]
            while index<len(x):
                SouthSum[index]+=float(x[index])
                index+=1
        if state in West:
            x=x.split(",") #splits by commas: basically, each column in the .csv file will become a separate string within the list
            x=x[1:]
            while index<len(x):
                WestSum[index]+=float(x[index])
                index+=1
    for variable in NortheastSum:
        variable=variable/9 #9 is the number of states in the Northeast (hence average of those 9 states can be found by dividing by 9)
        NEAverage.append(variable)
        #print NEAverage
    for variable in MidWestSum:
        variable=variable/12 #12 is the number of states in the MidWest
        MWAverage.append(variable)
        #print MWAverage
    for variable in SouthSum:
        variable=variable/17 #17 is the number of states including D.C. in the South
        SAverage.append(variable)
        #print SAverage
    for variable in WestSum:
        variable=variable/13 #13 is the number of states in the West
        WAverage.append(variable)
        #print WAverage
    html="<html><title>SAT Analysis</title><h1><center>Average SAT and ACT scores in different regions of the United States<center></h1>"
    html+=beginText+beginText2+beginText3+text+textH+textH2+textH3
    html+=text01
    ##setting up table
    html+="<table border=1><tr><td>Region Name</td><td>SAT: Avg. Composite Score</td><td>SAT: Avg. Critical Reading Score</td>"
    html+="<td>SAT: Avg. Mathematics Score</td><td>SAT: Avg. Writing Score</td><td>Percent taking SAT</td>"
    html+="<td>Student to Teacher Ratio</td><td>Percent taking ACT</td><td>ACT: Avg. Composite Score</td>"
    html+="<td>ACT: Avg. English Score</td><td>ACT: Avg. Math Score</td><td>ACT: Avg. Reading Score</td><td>ACT: Avg. Science Score</td>"
    html+="<tr><td>Northeast</td>"
    ##separating each average value into its own cell in the table
    for e in NEAverage:
            html+="<td>"+str(e)+"</td>"
    html+="</tr>"
    html+="<tr><td>MidWest</td>"
    for e in MWAverage:
            html+="<td>"+str(e)+"</td>"
    html+="</tr>"
    html+="<tr><td>Sourh</td>"
    for e in SAverage:
            html+="<td>"+str(e)+"</td>"
    html+="</tr>"
    html+="<tr><td>West</td>"
    for e in WAverage:
            html+="<td>"+str(e)+"</td>"
    html+="</tr>"
    html+=textCon+textCon2+"</html>"
    return html

##A failed attempt at combining a for and while loop:
##    while i<4:
##        html+="<tr><td>"+NAMES[a]+"</td>"
##        a+=1
##        for x in AVGHolders:
##            for e in x:
##                html+="<td>"+str(e)+"</td>"
##        html+="</tr>"
##        i+=1
##    return html


print analysis()
