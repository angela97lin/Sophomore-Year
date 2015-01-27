#!/usr/bin/python

print "Content-Type: text/html\n"

print ""
#print "foo"+"<br>"
import os
d=os.environ.keys()
for k in d:
    print k+" has value "+os.environ[k]+"<br>"


