#!/usr/bin/python3
'''
this function contains the MyList class
'''

class MyList(list):

    '''Public instance method of class MyList'''
    def print_sorted(self):
        print(sorted(self))
