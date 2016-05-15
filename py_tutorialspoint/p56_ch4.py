#!/usr/bin/python

counter = 100
miles = 100.0
name = "John"
names = ["melissa", "diana", "michael", "cara"]
colors = ("red", "blue", "white", "black")
no_dupt = {"melissa", "diana", "michael", "cara", "cara"}
dictionary = {'a' : 'apple', 'b' : 'bat', 'c' : 'cat', 'd' : 'dump'}


print "counter type : ", type(counter), " : ", counter
print "miles type : ", type(miles), " : ", miles
print "name : ", type(name), " : ", name
print "names : ", type(names), " : ", names
print "colors : ", type(colors), " : ", colors
print "No Duplicate : ", type(no_dupt), " : ", no_dupt
print "dictionary : ", type(dictionary), " : ", dictionary

#List operations

print "\n \n \t \b List operations \n \n"
print "list.append()"
names.append("Anna")  #names[len(names):] = ["Kj"]  #names.insert(len(names), [List])
print names
print "list.extend()"
names.extend(["pj", "luigi", "mario"])  # names[len(names):] = [List]
print names
print "list.insert(index, str)"
names.insert(0, "corie")
names.insert(len(names), "endie")
print names
print "list.remove(str)"
names.remove('corie')
print names
print "list.pop([index])"
names.pop()
names.pop(4)
print names
print "list.clear()" # del list[:]
#names.clear()  : Error in python 2.7
#del list[:]  : Error in python 2.7
print "list.index(str)"
print "Index # for mario is :", names.index("mario")
# Error: print names.index("daisy")
print "list.count(str)"
names.insert(len(names), "mario")
print names.count("mario")
print "list.sort(key=str.lower, reverse=False)"
names.sort(key=str.lower, reverse=True)
print names
print "list.reverse()"
names.reverse()
print names
print "list.copy()" # names[:]
#names2 = names.copy()  -> Error in python 2.7


from collections import deque
queue = deque(names)
print queue
print "deque.append(), deque.popleft"
queue.append("masra")
print queue
print queue.popleft()
print queue

#list comprehensive --->>
print """ List comprehensive ********
      ************
      ******************************* \n"""

print "Square of numbers"

squares = []
for x in range(10):
    squares.append(x**2)

print "squares using for loop & range() function : ", squares

squares =[]
squares = list(map(lambda x: x**2, range(15)))
print squares
