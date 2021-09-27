#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if x == 0:
        return x
    try:
        for i in range(0, x):
            print("{:d}".format(my_list[i]), end="")
    except:
        print("")
        return i
    print("")
    return i+1
