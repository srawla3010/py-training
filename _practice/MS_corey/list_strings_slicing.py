#list & string slicing

#list=['list of comma separated items']
#list_read=[index]
#list_read[start:end:step]

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
		  #0, 1, 2, 3, 4, 5, 6, 7, 8, 9
		#-10, -9, -8, -7, -6, -5, -4, -3, -2, -1

print(my_list[-1:1:-1]) 


#slicing string


sample_url='http://example.com'
print(sample_url)

#reverse the url
print(sample_url[::-1])

#Get the top level domain
print(sample_url[-4:])

#Print the url without http://
print(sample_url[7:])

#print the url without http:// and top level domain
print(sample_url[7:-4])