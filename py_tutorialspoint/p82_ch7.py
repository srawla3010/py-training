#!/usr/bin/python

"""python loops"""

count = 0
while ( count < 9):
    print count
    count += 1
else:
    print "counte is greater than or equal to 9, quiting.........."



print "Infinite loop"

while True:
    num = raw_input("Input a number : ")
    print "You entered : ", num
    if (num == '' or num == 'q'):
        break

print "while single statement"
flag = 1
#while(flag): print "given flag is really true"

print "Good Bye while loop"
