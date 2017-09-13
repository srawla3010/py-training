'''
@property decoraton   :- accessing class method as class attributes. 
getter
setter  :- @<function name>.setter 
deleter functionality 

'''

class Employee(object):

    def __init__(self, first, last):
        self.first = first
        self.last = last
        #self.email = '{}.{}@email.com'.format(self.first, self.last)

    @property  ##getter
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property 
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter  #setter
    def fullname(self, name):
    	first , last = name.split(' ')
    	self.first = first
    	self.last = last

    @fullname.deleter
    def fullname(self):
        print('Deleting Names')
        self.first = None
        self.last = None

emp_1 = Employee('John', 'Smith')

emp_1.fullname = 'Mel maria'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del(emp_1.fullname)

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

