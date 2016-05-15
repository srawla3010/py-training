#!/usr/bin/python

import sys

test_f = "test_file"

try:
    #open file stream
    file = open(test_f, "w")
except IOError:
    print "There was an error writing to", test_f
    sys.exit()

print "ended"
