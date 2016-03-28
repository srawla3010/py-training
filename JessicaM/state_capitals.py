#!/usr/bin/python
import random

capitals_dict ={'Alabama': 	'Montgomery',
'Alaska': 	'Juneau',
'Arizona': 	'Phoenix',
'Arkansas': 	'Little Rock',
'California': 	'Sacramento',
'Colorado': 	'Denver',
'Connecticut': 	'Hartford',
'Delaware': 	'Dover',
'Florida': 	'Tallahassee',
'Georgia': 	'Atlanta',
'Hawaii': 	'Honolulu',
'Idaho': 	'Boise',
'Illinois': 	'Springfield',
'Indiana': 	'Indianapolis',
'Iowa': 	'Des Moines',
'Kansas': 	'Topeka',
'Kentucky': 	'Frankfort',
'Louisiana': 	'Baton Rouge',
'Maine': 	'Augusta',
'Maryland': 	'Annapolis',
'Massachusetts': 	'Boston',
'Michigan': 	'Lansing',
'Minnesota': 	'Saint Paul',
'Mississippi': 	'Jackson',
'Missouri': 	'Jefferson City',
'Montana': 	'Helena',
'Nebraska': 	'Lincoln',
'Nevada': 	'Carson City',
'New Hampshire': 	'Concord',
'New Jersey': 	'Trenton',
'New Mexico': 	'Santa Fe',
'New York': 	'Albany',
'North Carolina': 	'Raleigh',
'North Dakota': 	'Bismarck',
'Ohio': 	'Columbus',
'Oklahoma': 	'Oklahoma City',
'Oregon': 	'Salem',
'Pennsylvania': 	'Harrisburg',
'Rhode Island': 	'Providence',
'South Carolina': 	'Columbia',
'South Dakota': 	'Pierre',
'Tennessee': 	'Nashville',
'Texas': 	'Austin',
'Utah': 	'Salt Lake City',
'Vermont': 	'Montpelier',
'Virginia': 	'Richmond',
'Washington': 	'Olympia',
'West Virginia': 	'Charleston',
'Wisconsin': 	'Madison',
'Wyoming': 	'Cheyenne',
}

states = list(capitals_dict.keys())
capitals =list(capitals_dict.values())

#print(capitals_dict)
#print(capitals)

for i in [1, 2, 3, 4, 5]:
    state = random.choice(states)
    capital = capitals_dict[state]
    #print("Hint...... :- " + state)
    capital_guess = raw_input("Please enter Capital name of " + state +" ? ")
    #print("State_guess is :- " + state_guess)

    if capital_guess not in capitals:
        print("OOPS , Invalid capital Name")
        print("The Capital of state " + state + " is " + capital)
    elif capital_guess == capital:
        print("Correct! Nice Job")
    else:
           print("Incorrect, The Capital of state " + state + " is " + capital)

print("All Done")
