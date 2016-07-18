#!/usr/bin/python

import p310_ch18

emp1 = p310_ch18.Employee('Maxman', 22, '10000')
emp2 = p310_ch18.Employee('Minman', 18)

print "Emp1's details :-"
emp1.displayEmployee()
emp2.displayEmployee()

print "Total number of employee ", p310_ch18.Employee.empCount

emp2.salary = '200K'
emp2.displayEmployee()

print "Built-In class attributes :-"
print p310_ch18.Employee.__doc__
print p310_ch18.Employee.__dict__
print p310_ch18.Employee.__name__
print p310_ch18.Employee.__module__
print p310_ch18.Employee.__bases__

p1 = p310_ch18.Point()
p2 = p1
p3 = p1

print id(p1), id(p2), id(p3)
del p1
del p2
del p3

print "P312_ch18.py Bye Bye"
