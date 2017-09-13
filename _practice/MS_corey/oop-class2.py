'''
class variables
instance variables
'''

class Employee(object):
	
	raise_amount = 1.04
	num_of_emps = 0

	def __init__(self, first, last, pay):
		self.first = first  # instance variables. initiated via self ( instance or object of the class )
		self.last = last
		self.pay = pay 
		self.email = '{}.{}@mail.com'.format(first, last)
		Employee.num_of_emps += 1

	def fullname(self):
		return 'Employee\'s Full Name : {} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)  
		#self.pay = int(self.pay * Employee.raise_amount)

	def number_of_emps(self):
		return Employee.num_of_emps

print("Number of Employees Before: {}".format(Employee.num_of_emps) )

emp_1 = Employee('Alan', 'Safer', 50000)
emp_2 = Employee('Maria', 'Yone', 60000)

print("Number of Employees After: {}".format(Employee.num_of_emps) )

#print(Employee.__dict__)
#print(dir(Employee))

print('\nEmployee, emp_1 & emp_2 raise amount:->')
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print('\nemp_1\'s pay before and after raise : ')
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print('emp_2\'s pay before and after raise : ')
print(emp_2.pay)
emp_2.apply_raise()
print(emp_2.pay)