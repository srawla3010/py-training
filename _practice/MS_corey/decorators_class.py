'''
#Decorators

A Python decorator is a specific change to the Python syntax that allows us to more conveniently alter functions, methods & class
'''

class decorator_class(object):
	def __init__(self, original_function):
		self.original_function = original_function

	def __call__(self, *args, **kwargs):
		 print('call method executed this before {}'.format(self.original_function.__name__))
		 return self.original_function(*args, **kwargs)

						  #@decorator_function      ## display = decorator_function(display)
@decorator_class		  ## display = decorator_class(display)	
def display():
	print('display function ran\n')

display()


						#@decorator_function     ## display_info = decorator_function(display_info)
@decorator_class		## display_info = decorator_class(display_info)
def display_info(name, age):
	print('display_info ran with arguments ({}, {})\n'.format(name, age))

display_info('Jessie', 25)


