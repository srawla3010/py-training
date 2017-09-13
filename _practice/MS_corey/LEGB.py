'''
LEGB
Local Enclosed Global Built-in
'''

x = 'global X'

def outer():
	#global x
	x = 'outer X'

	def inner():
		#nonlocal x
		x = 'inner X'
		print(x)

	inner()
	print(x)

outer()
print(x)
