#json_parser.py
#java script object notation file
#Data is valid list or dict in python

import json

#methods
#json.dumps('string')
#json.dump(file_object)
#json.loads('string')
#json.load(file_object)


'''
load & loads
'''

example1 = '''{
    "fruit": "Apple",
    "size": "Large",
    "color": "Red",
    "price": null
}'''

example1_data = json.loads(example1)
print(example1_data)


with open('example2.json', 'r') as example2:
	example2_data = json.load(example2)


print(example2_data)


'''
dump 
and 
dumps
'''

example1 = {
    "fruit": "Banana",
    "size": "Long",
    "color": "Yellow",
    "price": 10,
    "expensive": True,
    "return": None
}
print(json.dumps(example1, indent=2))


with open('example3.json', 'w') as json_dump:
	json.dump(example1, json_dump, indent=4)

