#!/usr/bin/python3
'''
this function contains the MyList class
'''
class MyList(list):

    def __init__(self):
        pass

    '''Public instance method of class MyList'''
    def print_sorted(self):
        print(sorted(self))
