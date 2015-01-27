#Angela Lin
#pd 06
#HW20b
#04-05-13

def modeListA(L):
    maxV=max(L)
    buckets=[]
    i=0
    while i<=maxV:
        buckets.append(0)
        i+=1
    for n in L:
        buckets[n]+=1
    return buckets.index( max(buckets) ) 

print modeListA([1,2,3,4,5,0,6,6,7,7]) #5/6/7
    
