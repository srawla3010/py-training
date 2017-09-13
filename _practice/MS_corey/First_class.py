'''
wikipeadia definition:-
In computer science, a programming language is said to have first-class functions if it treats functions as first-class citizens. 

 this means 
 the language supports passing functions as arguments to other functions, 
 returning function as the values from other functions
  and 
  assigning function to variables or storing function in data structures.


====
 [1] Some programming language theorists require support for anonymous functions (function literals) as well.
 [2] In languages with first-class functions, the names of functions do not have any special status; they are treated like ordinary variables with a function type.
'''

##Assigning function to a variable

def square(x):
	return x*x

def cube(x):
	return x*x*x

#var1 = square
#
#print(square)
#print(var1)
#print(var1(10))


##Passing Function as an argument Or returning function as values
##it's called high order function

def my_map(func, arg_list):    #Higher-order function -> func = square , arg_list = [1-5], result = []*[]
	result = []
	for i in arg_list:
		result.append(func(i))
	return result

num = [1, 2, 3, 4, 5]
squares = my_map(square, num)
cubes = my_map(cube, num)
print('squares : {}'.format(squares))
print('cubes : {}'.format(cubes))

##returning function as values

def logger(msg):
	def log_message():
		print('Log: ', msg)    ## passing value as an argument

	return log_message			## returning function

log_hi = logger('Hi')			##closures :- closes values on closing for msg variable
log_hello = logger('Hello')

print('\nValue of variable \\log_hi & \\log_hello :-')
print(log_hi)
print(log_hello)

print('\nValue of variable \\log_hi() & \\log_hello() :-')
log_hi()
log_hello()



##use case
##html tagging

def html_tag(tag):

	def wrap_text(msg):
		print('<{0}>{1}</{0}>'.format(tag, msg))

	return wrap_text

display_h1 = html_tag('H1')
display_paragraph = html_tag('P')

print('\nUse Case Output :->')
display_h1('Breaking News')
display_paragraph('it\'s a paragraph')

print('\nClosure example:- ')
display_h1('Advertisement Time')  ## example of closure, value of 'tag' is closing with value assignment


