#logging_basic-2.py
import logging

logging.basicConfig(filename='employee.log', level=logging.INFO, format='%(levelname)s:%(message)s')

class Employee(object):

	def __init__(self, first, last):
		self.first = first
		self.last = last
		logging.info('Created Employee {} - {}'.format(self.fullname, self.email))

	@property
	def email(self):
		return '{}.{}@email.com'.format(self.first, self.last)

	@property
	def fullname(self):
		return '{} {}'.format(self.first, self.last)


emp1 = Employee('John', 'Smith')
emp2 = Employee('Sunny', 'Tang')
emp3 = Employee('Zeb', 'Mang')