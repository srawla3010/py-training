##exceptions.py

'''
try:
	pass
except Exception:
	pass
else:
	pass
finally:
	pass

'''

try:
	f = open('test_file.txt', 'r')
	if f.name == 'corrupt file.txt':
		raise Exception  #raising exception manually
except IOError as e:
	print(e)
except Exception as e:
	print("Error: trying to read corrupt file")
else:
	print(f.read())
	f.close()
finally:
	print('executing Finally......')
