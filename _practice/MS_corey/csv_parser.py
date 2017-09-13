import csv


'''
writting to csv with different type of delimiter
'''

#with open('names.csv', 'r') as csv_file:
#	csv_data = csv.reader(csv_file, delimiter=',')
#
#	with open('new_names.csv', 'w') as new_csv_file:
#		csv_writer = csv.writer(new_csv_file, delimiter=':')
##
#		for line in csv_data:
#			csv_writer.writerow(line)
#
##reading from csv
#with open('new_names.csv', 'r') as csv_file:
#	csv_data = csv.reader(csv_file, delimiter=':')
#
#	next(csv_data)
#
#	for line in csv_data:
#		print(line)
#

'''
Reading and writting using DictReader & DictWriter back to file
'''

with open('names.csv', 'r') as names_file:
	csv_data = csv.DictReader(names_file)

	#for line in csv_data:
	#	print(line)
	#	print(line['email'])

	with open('new_names.csv', 'w') as new_csv_file:
		fieldnames =['email', 'first_name', 'last_name']
		#fieldnames =['first_name', 'last_name']    ## in case we want only first and last name - no mail

		file_writer = csv.DictWriter(new_csv_file, fieldnames, delimiter='\t')

		file_writer.writeheader()

		for line in csv_data:
			#del line['email']
			file_writer.writerow(line)
