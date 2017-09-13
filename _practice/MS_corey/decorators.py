'''
#Decorators

A Python decorator is a specific change to the Python syntax that allows us to more conveniently alter functions, methods & class
'''

'''==========Example =========='''
#def decorator_function(original_function):
#	def wrapper_function(*args, **kwargs):
#		print('wrapper executed this before {}'.format(original_function.__name__))
#		return original_function(*args, **kwargs)
#	return wrapper_function
#
#@decorator_function      ## display = decorator_function(display)
#def display():
#	print('display function ran\n')
#
#display()
#
#@decorator_function     ## display_info = decorator_function(display_info)
#def display_info(name, age):
#	print('display_info ran with arguments ({}, {})\n'.format(name, age))
#
#display_info('Jessie', 25)
#
#decorated_display = decorator_function(display)
#decorated_display()


'''==========USE CASES========='''

from functools import wraps  ##when stacking decorator, @wraps decorator is used to preserve value of original_function

def my_logger(original_function):
	import logging
	logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)

	@wraps(original_function)
	def wrapper_function(*args, **kwargs):
		logging.info('Ran with args : {}, and kwargs {}'.format(args, kwargs))
		return original_function(*args, **kwargs)
	
	return wrapper_function

def my_timer(original_function):
	import time

	@wraps(original_function)
	def wrapper_function(*args, **kwargs):
		t1 = time.time()
		results = original_function(*args, **kwargs)
		t2 = time.time() - t1
		print('{} ran in {} sec'.format(original_function.__name__, t2))
		return results
	return wrapper_function

#@decorator_function      ## display = decorator_function(display)
#def display():
#	print('display function ran\n')
#
#display()

#@my_logger    ## display_info = my_logger(display_info)
#@my_timer      ## display_info = my_timer(display_info)
@my_timer	  ## display_info = my_timer(mylogger(display_info))
@my_logger    
def display_info(name, age, courses=None):
	print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Tom', 15)


