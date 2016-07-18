#!/usr/bin/python

'''class oob method etc'''

print "Program Comment #### class oob method etc ####"

class Employee:
    'Class __DOC__ string :- Common base class for all employees names as Employee'
    empCount = 0
    __permempCount = 0

    def __init__(self, name, age, salary = 'confidential'):
        self.name = name
        self.salary = salary
        self.age = age
        print "Class Employee initialized "
        Employee.empCount += 1
        Employee.__permempCount += 1

    def displayCount(self):
        #print "Total Employee ", Employee.empCount
        print "Permanant Employee ",  Employee.__permempCount

    def displayEmployee(self):
        print "Name : ", self.name, " Age : ", self.age, " Salary : ", self.salary


class Point:
    '\n \n \n Garbage collector'
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "destoryed"


class Contractor(Employee):
    'Contractor __DOC__ string :- sub class from Employee'
    contCount = 0
    def __init__(self, name, age, salary = 'confidential', contid='NA'):
        self.name = name
        self.salary = salary
        self.age = age
        self.contid = contid
        Employee.empCount += 1
        Contractor.contCount += 1

    def displayEmployee(self):
        print self.name, "is an Contractor "
        print "Name : ", self.name, " Age : ", self.age, " Salary : ", self.salary, "Contractor id :", self.contid



print "Emp1's details :-"
emp1 = Employee('Maxman', 22, '10000')
emp2 = Employee('Minman', 18)
emp1.displayEmployee()
emp2.displayEmployee()
c1 = Contractor("Alex", 27, "297K", "cont001")
c2 = Contractor("Mayee", 22, contid='cont005')
print c1.displayEmployee()
print c2.displayEmployee()
print "Total Employee       :", Employee.empCount
print  c2.displayCount()
print "Contractual Employee :", Contractor.contCount

print issubclass(Contractor, Employee)
print isinstance(emp1, Contractor)

print "p310_ch18.py Bye Bye"
