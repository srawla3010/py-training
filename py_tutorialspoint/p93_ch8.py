#!/usr/bin/python

import math

print "Python numbers :- "

var1 = 10
var2 = 100

print var1, var2

del var1, var2

var1, var2 = 1, 10
print var1, var2

print "Number functions :"

print "abs(-45) : ", abs(-45)
# "abs(100.12L) : ", abs(100.12L)
print "abs(119L) : ", abs(119L)

print "math.ceil(-45.17) : ", math.ceil(-45.17)
print "math.ceil(100.12) : ", math.ceil(100.12)
print "math.ceil(100.72) : ", math.ceil(100.72)
print "math.ceil(math.pi) :", math.ceil(math.pi)

print "cmp(80, 100) :", cmp(80, 100)
print "cmp(180, 100) :", cmp(180, 100)
print "cmp(80, 80) : ", cmp(80, 80)

print "math.exp(x) :", math.exp(100)

numbers =[10,9,7,3,100,321,22]

print max(numbers)

name_age = {"alan", "mark", "tabu"}
print type(name_age)

name_age1 = {"hr" :{"alan" : 5, "mark" : 9, "tabu" : 3}, "ES" : {"maria" :3, "maxie" : 22}}
print type(name_age1)
print name_age1['hr']['alan']
