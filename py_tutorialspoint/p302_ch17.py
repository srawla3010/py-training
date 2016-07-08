#!/usr/bin/python

print '''<<<<<<<<
Python Exceptions
>>>>>>>>'''

def CeltoFahren(Temp):
    assert (Temp >= 0), "Colder than absolute zero !"
    return ((Temp-273)*1.8)+32

print CeltoFahren(273)
print int(CeltoFahren(505.78))
print CeltoFahren(-5)
