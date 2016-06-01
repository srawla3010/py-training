#!/usr/bin/python

print "Arithmetic Operator"
a = 21
b = 10
c = 0

c = a + b
print "Line 1 - Value of c is ", c

c = a - b
print "Line 2 - Value of c is ", c

c = a * b
print "Line 3 - Value of c is ", c

c = a / b
print "Line 4 - Value of c is ", c

c = a % b
print "Line 5 - Value of c is ", c

a = 2
b = 3
c = a**b
print "Line 6 - Value of c is ", c

a = 11.0
b = 5.0
c = a//b
print "Line 7 - Value of c is ", c

print "Comparison Operator"

x = 21
y = 10
z = 0

if(x==y):
    print "Line 1 - x is equal to y"
else:
    print "Line 2 - x is not equal to y"

if(x<>y):
    print "Line 1 - x is not equal to y"
else:
    print "Line 2 - x is equal to y"

if(x!=y):
    print "Line 1 - x is not equal to y"
else:
    print "Line 2 - x is equal to y"

if(x<y):
    print "Line 1 - x is less than y"
else:
    print "Line 2 - x is not less than y"

if(x>y):
    print "Line 1 - x is greater than y"
else:
    print "Line 2 - x is not greater than y"


print "Membership operator in not in"

name = "michael"
names = ['michael', 'Laura', 'robin', 'singh']

if('m' in name):
    print "\'m\' is in name \'michael\'"
else:
    print "\'m\' not in \'michael\'"

if('laura' in names):
    print "laura is in names"
else:
    print "laura is not in names"

print "Python identity operators- is / is not"

xx = "test"
yy = "fire"

if(xx is yy):
    print "xx is yy"
else:
    print "xx is not yy"
