#!/usr/bin/python

tup1 = ('physics', 'chemistry', '1997', 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"

print "tup1 : \n", tup1
tup1 = ("test",)
print "tup1 : \n", tup1
print type(tup1), type(tup2), type(tup3)

print "tup2[1:] :- ", tup2[1:]

tup3 = tup3 + tup2
print "tup3 = tup3 + tup2 \n", tup3

try:
    tup3[0] = "changing"
except(TypeError):
    print "trying to update tuple --- NOT ALLOWED"

try:
    del tup1
    print tup1
except(NameError):
    print "Name <tup1> not defined"
except:
    print "UNKNOWN error"

print "Good Bye!!"
