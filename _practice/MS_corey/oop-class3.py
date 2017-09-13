'''
regular methods -> Automatically takes instance as first argument, by convention it's 'self'
class methods -> use @classmethod decorator -> automatically takes first arguments as class, by convention it's 'cls'
static methods -> use @staticmethod decoraton -> Don't take any argument automatically, it's like regular function. ( Tip : if method is not using any self/cls inside it, change it to staticmethod)

class methods as alternative constructors, by convention start from 'from_'
'''

'''
class variables
instance variables
'''

class Employee(object):
	
	raise_amount = 1.04  #class variables
	num_of_emps = 0  #class variables

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

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amount = amount

	@classmethod
	def from_string(cls, emp_str):               ## class method & alternative constructor - using employee data split on '-'
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

	@staticmethod		## static method , determine a day is workday or not. ##requires time module - import datetime before calling
	def is_workday(day):
		##datetime module has a function weekday()  0-4 Monday-Friday, 5-6 Sat-Sunday
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True

emp_1 = Employee('Alan', 'Safer', 50000)
emp_2 = Employee('Maria', 'Yone', 60000)

Employee.set_raise_amt(1.05)  #   Also but not recommended :- emp_1.set_raise_amt(1.06)

#print('\nEmployee, emp_1 & emp_2 raise amount:->')
#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

#first, last, pay = emp_str_1.split('-')
#new_emp_1 = Employee(first, last, pay)
new_emp_1 = Employee.from_string(emp_str_1)  # from_string return Employee(self, arg, arg, arg)

print(new_emp_1.email)
print(new_emp_1.pay) 


print("Using static method, is_workday() :-")
import datetime
my_date = datetime.date(2017, 9, 11)  #datetime.date(yyyy, m, d)

print(Employee.is_workday(my_date))  #callable via instance object also i.e. (new_emp_1.is_workday(date))
#PS
#print(Employee.__dict__)
#print(dir(Employee))

