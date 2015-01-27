##Angela Lin
##pd 06
##HW20
##04-03-13

##1a. modeListA(nums) returns the mode, as a single number, of the set of numeric elements in list nums.
##e.g.,
##modeListA( [0,5,7,3,2,3] ) → 3
##modeListA( [0,5,7,3,7,3] ) → 3  ( or 7 )


def modeListA(nums):
    i=0
    modeV=nums.count(nums[i])
    while i<len(nums) and i+1<len(nums):
        if nums.count(nums[i])>modeV: 
            mode=nums[i] #the mode becomes the value of the current index
            i+=1
            modeV=nums.count(nums[i])
        else:
            i+=1
    return mode



print modeListA([1,2,3,3,3,4,5,6,6]) #3
print modeListA([1,2,3,4,4,5,5,6]) #4/5
print modeListA([1,2,2,2,3,2,3,3,3])#2/3

##1b. modeListB(nums) returns the mode, as a list, of the set of numeric elements in list nums. 
##e.g.,modeListB( [0,5,7,3,2,3] ) → [3]modeListB( [0,5,7,3,7,3] ) → [3,7]

def modeListB(nums):
    modeList=[]
    i=0
    modeV=nums.count(nums[i])
    while i<len(nums) and i+1<len(nums):
        if nums.count(nums[i])>modeV:
            mode=nums[i]
            modeList.append(nums[i])#the mode is appended to the list
            nums.remove(mode)
            modeV=nums.count(nums[i])
        else:
            i+=1
    return modeList
#Essentially the same as modeListA except it is appended to a list.
#In addition, it is important to note that because an element is removed from
#the original list, i does not increase by 1 in the if statement.


print modeListB([1,2,3,3,3,4,5,6,6]) #[3]
print modeListB([1,2,3,4,4,5,5,6]) #[4,5]
print modeListB([1,2,2,2,3,2,3,3,3])#[2,3]


##2. vBarGraphify(nums) takes a list of non-negative integers and prints a set of vertical bars.
##>>> x = [0,1,2,3]
##[0, 1, 2, 3]
##>>> vBarGraphify(x)
##
##      *
##    * *
##  * * *
##0 1 2 3
##
##>>> x = [1,0,3,2]
##[1, 0, 3, 2]
##>>> vBarGraphify(x)
##
##    *  
##    * *
##*   * *
##0 1 2 3


def maxList(nums):
    i=1
    maxV=nums[0]       
    while i<len(nums):
        if maxV>=nums[i]:
            i+=1
        else:
            maxV=nums[i] 
    return maxV
#Helper Function: maxList


#sadly, I was unable to get this code to work properly... it simply creates a pretty design...
def vBarGraphify(nums):
   maxV=maxList(nums)
   i=0
   printBar= " "
   while maxV>=0:
         while nums[i]!=maxV:
             i+=1
         print " "*i + "*"+(len(nums)-i)*" "+'\n'
         nums[i]-=1
         maxV=maxList(nums)
         i=0

   
    



vBarGraphify([0,3,2,1])
