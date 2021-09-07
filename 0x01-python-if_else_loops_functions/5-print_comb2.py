#!/usr/bin/python3
for count in range(0, 100):
    if count == 99:
        print("{:d}" .format(count))
    else:
        print("{:d}, " .format(count), end='')