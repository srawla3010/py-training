#!/usr/bin/python

var1 = "Hello World"
var2 = "Python Programming"

print type(var1)
print type(var2)

print "var1[0]", var1[0]
print "var2[1:5]", var1[1:5]

print "Updating string- var1[:6] + 'python' \n", var1[:6] + '\tPython'

print "String Operations + * [] [:] , in , not in, r/R , %"

print "my name is %s and weight is %d" % ("Zara", 21)

F_name = 'alana'
L_name = 'smith'

print "Full Name :- %s %s" %(F_name, L_name)
Name = F_name + L_name
print "Doubling full name = ", Name*2
print "Character from full Name = ", Name[0:3]

if 'X' not in Name[0:3]:
    print "X is not part of first 3 character of the name"
else:
    print "X is part of first 3 character of the name"

print r"c:\\data"

print Name.capitalize()
print Name.center(20,' ')
print Name.count('a',0,5)
print Name.find('mith',0,len(Name))

try:
    print Name.index('mithi',0,len(Name))
except:
    print "String not found"

str = 'this is string cap '
print str.lstrip()
print str.capitalize()

print "page 145 done"
