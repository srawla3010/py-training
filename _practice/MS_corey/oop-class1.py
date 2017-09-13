#start using object oriented programming concepts
'''
class
methods (function in class)
attributes ( data in class )
self ( class instance representative)
init (class constructor)
instance ( class instance = objects of class)
class-1'''


class Employee(object):
	#class initialization or constructor
	def __init__(self, first, last, pay):   #self = instance, passed automatically
		self.first = first   # ins1.first = first
		self.last = last
		self.email = "{}.{}@email.com".format(self.first, self.last)
		self.pay = pay

	def fullname(self):
		return 'Employee\'s Full Name :-> {} {}'.format(self.first, self.last)

#Create class instance, constructor/init will run automatically and pass arg values
emp_1 = Employee('Alan', 'Safer', 50000)   # Employee(emp_1, 'Alan', 'Safer', 50000)
emp_2 = Employee('Maria', 'Chang', 6000)   # Employee(emp_2, 'Alan', 'Safer', 50000)



#print(emp_1)
#print(emp_2)

#attributes
#emp_1.first = 'Alan'
#emp_1.last = 'Safer'
#emp_1.email = 'Alan.Safer@email.com'
#emp_1.pay = 50000
#
#emp_2.first = 'Maria'
#emp_2.last = 'Chang'
#emp_2.email = 'Maria.Chang@email.com'
#emp_2.pay = 50000

print("{} : {} : {} : {}".format(emp_1.first, emp_1.last, emp_1.email, emp_1.pay))
print("{} : {} : {} : {}".format(emp_2.first, emp_2.last, emp_2.email, emp_2.pay))


print(Employee.fullname(emp_1))
print(emp_1.fullname())   # == Employee.fullname(emp1)
print(Employee.fullname(emp_2)) #== emp2.fullname()  
print(emp_2.fullname())  




