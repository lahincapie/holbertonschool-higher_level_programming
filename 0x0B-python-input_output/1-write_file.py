#!/usr/bin/python3
'''function that writes a string to a text file
(UTF8) and returns the number of characters
written'''


def write_file(filename="", text=""):
    '''open() returns a file object, and is most
    ommonly used with two arguments:
    open(filename, mode).'''
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
