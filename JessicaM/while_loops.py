#!/usr/bin/python

#names = ['Alice', 'Bob', 'Cara']

#for name in names:
#    print("Hello Name:- " + name)


#for i in [1, 2, 3, 4, 5]:
#    print("for loop" + str(i))

#counter = 0

#while counter <= 5 :
#    print("while loop " + str(counter))
#    counter += 1

#counter = 0

#while True:
#    print("while True :- " + str(counter))
#    counter += 1

#    if counter >= 5:
#        break


print("Hello Human")

while True:
    user_input = raw_input(">  ")
    if user_input == 'quit':
        print("GoodBye")
        break
    else:
        print("you typed :- " + user_input)
