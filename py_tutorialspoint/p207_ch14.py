#!/usr/bin/python

print "python function"

print "Define a function \" def <func name>(): "

def printer(str):
    "This prints a passed string into this function"
    print str
    return

print "calling function"
printer("Calling printer function")
printer("Again second call to funtion")

print "\n function parameter pass by refrence vs value"

def changeme( mylist ):
    "This changes a passed list into this function"
    print "Original value of mylist ", mylist
    mylist.append([4, 5, 6])
    print "Value inside the function ", mylist
    return

mylist = [1, 2, 3]
changeme(mylist)
print 'Value outside the function ', mylist

xy=[]

def changeme1( xy ):
    "This changes a passed list into this function"
    xy = [1, 2, 3, 4]
    print "Value inside function: ", xy
    return

mylist1 = [10, 20, 30, 40]
changeme1(mylist1)
print "Value outside function ", mylist1, xy

print "\n Type of arguements -> Required, Keyword, Default, Variable-length \n"

print "Required Arguements :-"
def required( str ):
    "Example for required arguements"
    print "Value of the argument :- ", str

try:
    required("Test")
except:
    print "required() takes exactly 1 argument ( 0 given )"

print "Keyword Arguemnts"

def printinfo(name, age):
    "This print passed info into this function: Keyword Arguemnts"
    print "Name : ", name
    print "Age  : ", age
    return

printinfo(age = 10, name = 'alice')

print "Default Arguemnts"

def printinfo1(name, age = 0):
    "This print passed info into this function : Default Arguements"
    print "Name : ", name
    print "age  : ", age
    return

printinfo1('Aisha')

print "Variable-length Arguemnts"

def printinfo1(name, *nametuple):
    "This prints a variable passed arguemnt : Variable-length"
    print "Output is :- "
    print name
    for var in nametuple:
        print var
    return

printinfo1("Alice", "Maria", "Lucia")
printinfo1("Alice")

print "anonymous function -> lambda "
sum = lambda arg1, arg2: arg1 + arg2

print "Value of total :- ", sum(10, 2)
print "Value of total :- ", sum(2, 2)

print "return statement "

def sum(arg1, arg2):
    "Use of return"
    tot = arg1 + arg2
    print "Total inside function :- ", tot
    return tot

total = sum(10, 90)
print "Outside the function ", total

print "Page 213, Good Bye"
