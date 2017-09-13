'''
class inheritence

Inherit Employee to Developer & Manager

in-built function
isinstance(<inst name>, <class name>)
issubclasse(<child class>, <parent class>)

'''

#i.e HTTPException class
##simple Employee class

class Employee(object):

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = '{}.{}@email.com'.format(self.first, self.last)
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


dev_1 = Employee('Tana', 'loke', 50000)
dev_2 = Employee('Test', 'Employee', 60000)

#print(dev_1.email)
#print(dev_2.email)

class Developer(Employee):
	raise_amt = 1.50

	def __init__(self, first, last, pay, prog_lang):
		super(Developer, self).__init__(first, last, pay)  #recommended way to pass value to super class init method , python 2.7 specific code
		#super().__init__(first, last, pay) #python 3.xx compatible, use future in import for compatibility 
		#Employee.__init__(self, first, last, pay)
		self.prog_lang = prog_lang

class Manager(Employee):
	raise_amt = 1.75

	def __init__(self, first, last, pay, employees=None):
		super(Manager, self).__init__(first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees
	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print('--> {}'.format(emp.fullname()))



dev_3 = Developer('Ben', 'sg', 200000, 'java')
dev_4 = Developer('vivian', 'Bishoni', 30000, 'go')

mgr_1 = Manager('sue', 'smith', 9000, [dev_3])

print(mgr_1.email)

mgr_1.add_emp(dev_4)
mgr_1.remove_emp(dev_3)
mgr_1.add_emp(dev_4)  # Testing to make sure no duplicate emp are added


mgr_1.print_emps()

#PS 
print('\n')
print('is {} instance of {} : {}'.format('mgr_1', 'Employee', isinstance(mgr_1, Employee))) #print(issubclass(mgr_1, Employee))
print('is {} instance of {} : {}'.format('mgr_1', 'Developer', isinstance(mgr_1, Developer)))
print('is {} instance of {} : {}'.format('mgr_1', 'Manager', isinstance(mgr_1, Manager)))  

#issubclass()
print('\n')
print('is {} subclass of {} : {}'.format('Developer', 'Employee', issubclass(Developer, Employee))) #print(issubclass(mgr_1, Employee))
print('is {} subclass of {} : {}'.format('Manager', 'Employee',   issubclass(Manager, Employee)))
print('is {} subclass of {} : {}'.format('Manager', 'Developer',  issubclass(Manager, Developer)))  

#print(dev_3.pay)
#dev_3.apply_raise()
#print(dev_3.pay)
#print(dev_3.email)
#print(dev_3.prog_lang)
#print(dev_4.email)
#print(dev_4.prog_lang)
#help method for Method Resolution order
#print(help(Employee))
#print(help(developer))