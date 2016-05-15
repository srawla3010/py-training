## parsing command line arguments getopt

import getopt
import sys

arg_list = list(sys.argv)
#print str(sys.argv[1:])

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        #opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
        opts, args = getopt.gnu_getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print arg_list[0], '-i <inputfile> -o <outputfile>'
        sys.exit()

    #print type(opts)
    #print len(args)
    print opts
    print args


    for opt, arg in opts:
        if opt == '-h':
            print arg_list[0], '-i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ('-i', '--ifile'):
            inputfile = arg
        elif opt in ('-o', '--ofile'):
            outputfile = arg
    print "Input file is :", inputfile
    print "Output file is :", outputfile

if __name__ == "__main__":
    main(sys.argv[1:])
