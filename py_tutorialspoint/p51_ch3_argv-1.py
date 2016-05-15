#!/usr/bin/python

import sys
import getopt

arg_list = sys.argv[1:]

def usage():
    print """use -v or --verbose
             -o or --output
             -h or --help"""

def main(arg):
    try:
        opts, args = getopt.getopt(arg, "ho:v:", ['help', 'output='])
    except getopt.GetoptError as err :
        print(err)
        sys.exit(2)
    output = None
    verbose = False

    #print opts
    #print args

    for op, ar in opts:
        if op in "-v":
            verbose = True
            print "Verbose :", verbose
        elif op in ("-h", "--help"):
            usage()
            sys.exit()
        elif op in ("-o", "--output"):
            output = ar
            print output
        else:
            assert False, "unhandled option"

if __name__ == "__main__":
    main(arg_list)
