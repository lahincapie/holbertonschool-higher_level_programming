#!/usr/bin/python3
for numL in range(0, 10):
    for numR in range(numL + 1, 10):
        if numL == 8 and numR == 9:
            print("{:d}{:d}".format(numL, numR))
        else:
            print("{:d}{:d}, ".format(numL, numR), end='')
