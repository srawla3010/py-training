#!/usr/bin/python

print "Break statement ; "
for letter in 'Python':
    if letter == 'h':
        break
    print 'Current Letter is : ', letter

var = 10

while var > 0:
    print 'Current variable value :', var
    var -= 1
    if var == 5:
        break


print "Continue statment"

for letter in 'Python':
    if letter == 'h':
        continue
    print 'Current Letter is  :', letter


while var > 0:
    var -= 1
    if var == 2:
        continue
    print 'Current variable value :', var

print "pass statement"

for letter in 'Python':
    if letter == 'h':
        pass
        print 'This is pass block'
    print 'Current Letter :' , letter


print "Good Bye"
