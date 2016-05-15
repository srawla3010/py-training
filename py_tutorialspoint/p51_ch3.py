#!/usr/bin/python

#python multiline statement

item_one = 1 ; item_two = 2 ; item_three =3;

total = item_one + \
        item_two + \
        item_three

print "total : ", total

days = ["Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday"]

print "days: ", days

word = 'word'

print "word :", word

sentence = "This is a sentence"

print "sentence :", sentence

paragraph = """This is a paragpraph, it's
                    made of multiple
                        lines"""

print "paragraph :", paragraph #print multiple line paragraph

#input from keyboard

name = raw_input ("Input your name : ")
print "your name is :", name

import sys; x = 'foo'; sys.stdout.write(x + '\n')

if 'D' in name :
    print "Name is : Daisy"
elif 'V' in name :
    print "Name is : Vivaan"
else :
    print "Name : UNKNOWN"

#command line arugments

#import sys ; already done

print 'Number of command line arguments : ', len(sys.argv)
arg_list = list(sys.argv)
print 'Arguments List : ', arg_list
print 'First Argument :', arg_list[0]
