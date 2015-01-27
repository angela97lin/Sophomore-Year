
    
englist=['cat','dog','man','yes','sit']
spanlist=['gato','perro','hombre','si','sentar']

def translate(word):
    if word in englist:
        i=englist.index(word)
        return spanlist[i]
    else:
        return None
    
##
##print translate("cat")
##print translate("gato")



def dict_maker():
    d={}
    for line in open('dictionary.txt').readlines():
        line=line.strip().split(',')
        d[line[0]]=line[1]
    return d.keys()
    #return d.values()

print dict_maker()
        
        

def load_dictionary(fname):
    L1=[]
    L2=[]
    for line in open(fname).readlines():
        words=line.strip().split(",")
        L1.append(words[0])
        L2.append(words[1])
    return L1, L2

#print load_dictionary('dictionary.txt')

def translate(word,L1,L2):
    if word in L1:
        i=L1.index(word)
        return L2[i]
    return none

lists=load_dictionary('dictionary.txt')
englist=lists[0]
spanish=lists[1]
#print translate('cat',spanish,english)
#print translate('si',spanish,english)

d={}
d['hello']='hola'
d['goo']='p'
##print d.values()
##print d.keys()

