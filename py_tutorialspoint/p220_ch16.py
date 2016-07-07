#!/usr/bin/python
import os
import time

print "File I/O operation function open() & close()"

print "Open function -> file object = open(file_name [, access_mode][,buffering])"

f = open("test_file", "r+")

print "File name :- ", f.name
print "File mode :- ", f.mode
print "File softspace :- ", f.softspace
print "File closed :- ", f.closed

print "File read :- f.read() \n", f.read()

print "Current cursor position f.tell() :- ", f.tell()
print "Reset cursor position 15bytes from begin f.seek(15, 0) "
f.seek(15,0)
print "Position after reset f.tell() :- ", f.tell()

print "Reading file f.readline() :- ", f.readline()
print "Reading file f.readline() :- ", f.readline()

print "========="
f.seek(0,0)
print "Reading file f.readlines():-", f.readlines()

print "renaming ft1 to testfile1"

f1 = open("testfile1", "w")
#time.sleep(1)
os.rename("testfile1", "t_file1")
#time.sleep(1)
os.remove("t_file1")
print "creating directory for testing"

try:
    os.mkdir("T1")
except(OSError):
    print "Directory already exist, skipping directory creation....."

os.chdir("T1")
print os.getcwd()
t1 = open("t1.txt", "w")
print "removing directory"
try:
    os.rmdir(os.getcwd())
except Exception as ex:
    print ex
    print "Deleting files in directory", os.getcwd()
    for files in os.listdir("."):
        os.remove(files)
    os.rmdir(os.getcwd())
    os.chdir("..")
    print "directory removed, current working directory is :- ",os.getcwd()

print "File and Directory related Object or Methods "

f3 = open("file1.txt", "r+")
#f2.write("hello, file1.txt")
f3.flush()
print "f2.fileno() ", f3.fileno()
print "f2.isatty() ", f3.isatty()

for index in range(5):
    line = f3.next()
    print "Line No %d - %s" % (index, line)

f3.close()
f2 = open("file1.txt", "r+")
print "Name of the file :- ", f2.name
line1 = f2.readline()
print "Read Line: %s " % (line1)
f2.seek(50,0)
#f2.truncate()

f3 = open("file3.txt", "w")
print "Name of the file :- ", f3.name
f3.write("# This is 1st line \n This is 2nd line \n This is 3rd line \n This is 4th line \n This is 5th line \n")

seq =["This is 6th line \n", "This is 7th line \n"]
f3.seek(0,2)
f3.writelines(seq)

f3.seek(0,0)
f3 = open("file3.txt", "r")
for index in range(7):
    line = f3.next()
    print "Line no. %d - %s" %(index, line)

print "p239 ch 16 Good Bye"








#file_name = raw_input("Enter file name :- ")
#f1 = open(file_name, "w")
#f1.write(raw_input("Type something to write into file :- "))
