#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for item in range(0, len(my_list)):
        """ [cadena].format() """
        print("{:d}".format(my_list[item]))
