#!/usr/bin/python

"""for loop"""

print "for loop"

for letter in 'Python':
    print "Current letter is ", letter

fruits =['banana', 'mango', 'curry', 'laukee']

for fruit in fruits:
    print "Today's fruit is ", fruit

for index in range(len(fruits)):
    print "Tomorrow's fruit is  ", fruits[index]

print "Searching prime numbers "

for num in range(10, 20):
    for i in range(2, num):
        if num%i == 0:
            j = num/i
            print '%d equals %d * %d' % (num, i, j)
            break
    else:
        print num, ' is a prime number'


print "===PYTHON CONTROL STATEMENTS -> break, continue, pass"

if True:
    break

print "Good Bye for loop"
