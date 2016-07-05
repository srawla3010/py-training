#!/usr/bin/python
import mod_hello
import math
from mod_hello import *

print "PYTHON MODULE"

print_func("Testing from p213")

mod_hello.total_func(10, 20)


Money = 1000


def AddMoney():
    global Money
    Money = Money + 1

print Money
AddMoney()
print Money

func_hello = dir(mod_hello)
func_math = dir(math)

print "Functions in module func_hello :- ", func_hello
print "Functions in module func_math :- ", func_math

print math.__name__
print math.__doc__
print math.__file__

print mod_hello.__name__
print mod_hello.__doc__
print mod_hello.__file__

print "local functions :- \n", locals().keys(), "\n"
print "global functions :- \n", globals().keys()
