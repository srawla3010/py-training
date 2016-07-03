#!/usr/bin/python
import sys
##python Lists P157"

list1 = ["physics", 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ['a', 'b', 'c', 'd']

print "list1[0] = ", list1[0]
print "list1[1:5] ", list1[1:5]

print "Value available at index 2 : "
print list1[2]
list1[2] = 2016
print "New value available at index 2 is : "
print list1[2]

print list2
del list2[0]
print list2

#str1 = str(raw_input())
#print str1
print "len() function on list : \n"

list1, list2 = ['zzzz', 'xyz', 'zara'], [456, 'abc', 'def', 459]

print "First list length : ", len(list1)
print "Second list length :", len(list2)

print "max() function on list : \n"
print "Max in list1 : \n", max(list1)
print "Max in list2 : \n", max(list2)

print "min() function on list : \n"
print "Min in list1 : \n", min(list1)
print "Min in list2 : \n", min(list2)

print "list() function converts tuple to list : \n"
aTuple =(123, 'xyz', 'zara', 'abc')
print type(aTuple)
print type(list(aTuple))
