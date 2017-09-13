# -*- coding: utf-8 -*-
## above line is for error Python “SyntaxError: Non-ASCII character '\xe2' in file”
'''
Closures 
In programming languages, closures (also lexical closures or function closures) are techniques for implementing lexically scoped name binding 

in languages with first-class functions. Operationally, a closure is a record storing a function[a] together with an environment:[1] a mapping associating each free variable of the function (variables that are used locally, but defined in an enclosing scope) with the value or reference to which the name was bound when the closure was created.
 [b] A closure—unlike a plain function—allows the function to access those captured variables through the closure's copies of their values or references, even when the function is invoked outside their scope.

example:-


def func_out(x):
	var1 = x
	def func_in(y):
		return var1+y     ## var1 is called free variable 
	return func_in

closure1 = func_out(5)
closure2 = func_out(10)

print(closure1.__name__)
print(clsoure2.__name__)

print(closure1(2))  ## 7
print(closure2(2))  ## 12
print(closure1(4))  ## 9
print(closure2(9))  ## 19


PS : A closures closes over the free variable in their environmnet
'''
## Use Cases

import logging
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func


def add(x, y):
    return x+y


def sub(x, y):
    return x-y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)

