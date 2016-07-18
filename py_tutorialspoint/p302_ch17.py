#!/usr/bin/python

print '''<<<<<<<<
Python Exceptions
>>>>>>>>'''

def CeltoFahren(Temp):
    assert (Temp >= 0), "Colder than absolute zero !"
    return ((Temp-273)*1.8)+32

print CeltoFahren(273)
print int(CeltoFahren(505.78))
print CeltoFahren(0)

print "Assertion Done !!!"

try:
    fh = open("testfile.txt", "w")
    try:
        fh.write("This is my test file for exception handling!! \n")
    finally:
        print "Going to close the file"
        fh.close()
except:
    print "Error: can\'t find file or read data"
else:
    print "written content in the file successfully"
    fh.close()

def temp_convert(var):
    try:
        return int(var)
    except ValueError, Argument:
        print "The argument doesn't contain numbers\n", Argument
#This is my comment

print temp_convert("xyz")

level = 0
def func_name(level):
    if level < 1 :
        raise "Invalid level!", level
    else:
        print "level number is : ", level
try:
    func_name(1)
except "Invalid level!":
    print "Invalid level found"
else:
    print "else statement block"

print "#End of p302_ch17.py \"Bye Bye\""

#This is end of the file
