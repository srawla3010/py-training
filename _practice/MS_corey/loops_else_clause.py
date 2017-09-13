#loops_else_clause.py

my_list =[1,2,3,4,5,9,8,7]

for x in my_list:
	print x
	if x >=10:
		break
else:   ## else here is equivelent to 'no-break'
	print('Hit the for/Else statement')


#while -else
print  #line space
i = 1

while i<5:
	print(i)
	i +=1
	if i == 6:
		break
else:
	print('Hit the While/Else statement')

#Use Case : Find index of a value in list, if not found return -1
print  #line space

def find_index(to_search, target):
	for index, value in enumerate(to_search):
		if value == target:
			break
	else:
		return -1
	return index

my_list =['Rick', 'Nodi', 'Kat']
index_location = find_index(my_list, 'Nodi')
print('Location of target is index {}'.format(index_location))