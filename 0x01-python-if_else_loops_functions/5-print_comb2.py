#!/usr/bin/python3
for count in range(0, 100):
    print("{:02d}, ".format(count), end='')
    if count == 99:
        print("{:d}".format(count))
