#logging_advance-2.py
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

#logging.basicConfig(filename='logging_advance_2.log', level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')

class Employee(object):

	def __init__(self, first, last):
		self.first = first
		self.last = last
		logger.info('Created Employee {} - {}'.format(self.fullname, self.email))

	@property
	def email(self):
		return '{}.{}@email.com'.format(self.first, self.last)

	@property
	def fullname(self):
		return '{} {}'.format(self.first, self.last)


emp1 = Employee('John', 'Smith')
emp2 = Employee('Sunny', 'Tang')
emp3 = Employee('Zeb', 'Mang')