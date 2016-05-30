#!/usr/bin/python

print "Assigning Value to variables"

counter = 100
miles = 1000.0
name = "John"

print "counter ", counter
print "miles ", miles
print "name ", name

print "Multiple Assignment a=b=c=<value> "
a, b, c = 1, 2, "John"
d = e = f = 5
print a, b, c, d, e, f


print "Python Strings, string operations"
str = "Hello World"

print "str ", str
print "str[0] ", str[0]
print "str[2:5]", str[2:7]
print "str[2:]", str[2:]
print "str[:2]", str[:2]
print "str[:]", str[:]
print "str * 2", str * 2
print "str + \"Test\" ", str + "Test"

print "Python list, list operations"

list = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print "list ", list
print "list[0] ", list[0]
print "list[1:3] ", list[1:3]
print "list[2:] ", list[2:]
print "tinylist * 2 ", tinylist * 2
list_tinylist = list + tinylist
print "list + tinylist ", list_tinylist
# "list_tinylist[-1] " list_tinylist[-1]

print "page 60 : Dictionary Operations"

dict = {}
dict['one'] = 'This is one'
dict['two'] = 'This is two'

tinydict ={'name' : 'John', 'code' : 6734, 'dept' : 'sales'}

print "dict[\'one\'] ", dict['one']
print "dict[\'two\'] ", dict['two']
print "tinydict ", tinydict
print "tinydict.keys() ", tinydict.keys()
print "tinydict.values() ", tinydict.values()
