#!/usr/bin/python

print "python dictionary"

print "create empty dict using dict ={}"

dict1 = {}
print type(dict1)

dict1 = {'Alice' : 1990, 'Beth' : 2016, 'Cecil' : 2013}
print dict1['Beth']
print dict1.keys()
print dict1.values()

print 'Updating Dictionary \n'
print 'dict1 :- ', dict1
dict1['Alice'] = 1980
print 'dict1 after update :- ', dict1

print 'Delete Dictionary Elements \n'
del dict1['Alice']
print 'dict1 after delete :- ', dict1
dict1.clear()
print dict1
del dict1
try:
    print dict1
except(NameError):
    print 'dict1 doesn\'t exist, already deleted'

dict1 = {'Alice' : 1990, 'Beth' : 2016, 'Cecil' : 2013}
dict2 ={'a' : {'name' : 'Zara', 'age' : 20, 'city' : 'SF' }, 'b':{'name' : 'Alex', 'age' : 25, 'city' : 'LA'}}

print 'dict2[a][name] :- ', dict2['a']['name']
print 'dict2 keys :- ', dict2.keys()
print 'dict2.values :- ', dict2.values()

print "Dictionary Built-in Functions & Methods :- \n"
print "cmp(dict1,dict2) ", cmp(dict1, dict2)
print "len(dict1) :-", len(dict1)
print "type(dict1) :- ", type(dict1)
print "str(dict1) :- ", str(dict1)
dict1_str = str(dict1)
print type(dict1_str)
print "dict1_str :- ", dict1_str
dict_x = {}
print "type(dict_x) before assignment ", type(dict_x)
dict_x = dict1_str
print "type(dict_x) after assignment ", type(dict_x)

dict1_x = {}
dict1_x = dict1.copy()
print 'dict1_x -> copy of dict1.copy() :- ', dict1_x

dict1_y = dict1.fromkeys(dict1)
print "dict1_y -> dict1.fromkeys() :- ", dict1_y

print "dict1_y.has_key() :- ", dict1_y.has_key('Alice')

print "dict1.items() :- ", dict1.items()

print "dict1.get(key) :-", dict1.get('Alice')
dict1.setdefault('alice', 'NA')
print "dict1.get(key) :-", dict1.get('alice')
dict1.update(dict2)
print "dict.update() :- ", dict1

print "dict1 keys :- ", dict1.keys()
print "dict1 values :- ", dict1.values()

print "page 191 - Good Bye"
