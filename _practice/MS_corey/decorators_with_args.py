def decorator_prefix(prefix):
	def decorator_function(original_function):
		def wrapper_function(*args, **kwargs):
			print('{} Exectued Before {}'.format(prefix, original_function.__name__))
			result = original_function(*args, **kwargs)
			print('{} Executed After {}\n'.format(prefix, original_function.__name__))
			#return result
		return wrapper_function
	return decorator_function

@decorator_prefix('LOG:')   ##  display_info = decorator_function(display_info) <<--run & return-- decorator_prefix('LOG:')
def display_info(name , age):
	print('display_info ran with arguments ({}, {})'.format(name, age))
	return 'Finished'


#display_info = decorator_function(display_info)
display_info('joe', 25)
display_info('jessie', 19)