#!/usr/bin/python

f = open("countries.txt", "r")

countries = []

for line in f:
    line = line.strip()
    #print(line)
    countries.append(line)

f.close()

#print(countries)
#print( len(countries))

for country in countries:
    if country[0] == "I" or country[0] == "i":
    #if  "T" in country or "t" in country:
        print(country)
