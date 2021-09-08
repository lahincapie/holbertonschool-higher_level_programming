#!/usr/bin/python3
import sys
if _name_ == "_main_":
    argc = len(sys.argv)-1
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{:} arguments:".format(argc))
        for counter in range(1, argc + 1):
            print("{}: {}".format(counter, sys.argv[counter]))
