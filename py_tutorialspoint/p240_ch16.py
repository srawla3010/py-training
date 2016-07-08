#!/usr/bin/python
import os, sys, stat

print '''>>>>>>>>>>>>>>>>>>>>>>>>>>
 240 ch16 -> OS Object Methods
<<<<<<<<<<<<<<<<<<<<<<<<<<<
'''

ret = os.access("test_file", os.F_OK)
print "F_OK -path exist - return value %s" %ret

ret = os.access("test_file", os.R_OK)
print "R_OK - path readable -return value %s" % ret

ret = os.access("test_file", os.W_OK)
print "W_OK - path readable - return value %s" %ret

ret = os.access("test_file", os.X_OK)
print "X_OK - path executable - return value %s" %ret

retvalcwd = os.getcwd()
print retvalcwd
newdir = retvalcwd + "/newdir"
try:
    os.mkdir(newdir)
except Exception as ex:
    print "Directory already exist, No action taken"

os.chdir(newdir)
print os.getcwd()
#f1 = open("test_f1.txt", "r")
#f2 = open("test_f2.txt", "r")

os.chmod("test_f1.txt", stat.S_IRWXU)
os.chown("test_f2.txt", 956075640, 0)



#open a file1
fd = os.open("foo.txt", os.O_RDWR | os.O_CREAT)

#Now get the touple
info = os.fstat(fd)
print "File Info : ", info
print "File UUID : ", info.st_uid
print "File GIS  : ", info.st_gid
print "File ctime : ", info.st_ctime
print "File Block Size :", info.st_blksize
print "File protection :", info.st_mode

sys_info = os.fstatvfs(fd)

print "File system info : ", sys_info
print "Maximum filename length : ", sys_info.f_namemax

print "create hard link to file foo.txt"
try:
    os.link("foo.txt", "foo1.txt")
except Exception as ex:
    print "Link already exist"

print "List current directory's contents : \n",
for file in os.listdir(newdir):
    print file

ls_info = os.lstat("foo1.txt")
major_dnum = os.major(info.st_dev)
minor_dnum = os.minor(info.st_dev)
print "foo1.txt Major Device Number : ", major_dnum
print "foo1.txt Minor Device Number : ", minor_dnum

print "P301 Good Bye ....!!"
