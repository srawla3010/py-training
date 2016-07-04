#!/usr/bin/python

import time

print "Python Date & Time "
ticks = time.time()
print "Number of ticks since 12:00 am, Jan 1, 1970 :- ", ticks
localtime = time.localtime(time.time())
print "Local current time in python struct format \n:- ", localtime
localtime = time.asctime(time.localtime(time.time()))
print "Local current time in human readable format  :-\n ", localtime

print "sleeping for 1 seconds......"
time.sleep(1)
print "time.clock() :- \n", time.clock()
print "time.ctime() :- \n", time.ctime()
print "time.ctime(time.clock()) :- \n", time.ctime(time.clock())

print "Calendar"

import calendar
cal = calendar.month(2016, 7)
print "Here is the Calendar of current month"
print cal


def procedure():
    time.sleep(1)

print "measure process time"
t0 = time.clock()
procedure()
print time.clock() - t0, "seconds process time"

print "measure wall time"
t0 = time.time()
procedure()
print time.time() - t0, "seconds wall time"

print "time.gmtime() : %s" %time.gmtime()

struct_time = time.strptime("30 Nov 00","%d %b %y")
print "returned tuple: %s " %struct_time


print "======Calendar========="
print "calendar.calendar(year, w=2, l=1, c=6)", calendar.calendar(2016, w=2, l=1, c=6)
print "calendar.firstweekday() ", calendar.firstweekday()
print "calendar.isleap(year)", calendar.isleap(2016)
print "calendar.leapdays(y1,y2)", calendar.leapdays(2001,2016)

print "Page 206, Good Bye!!"
