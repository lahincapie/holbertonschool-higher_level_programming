#!/usr/bin/python3
'''function that reads a text file (UTF8) and prints it to stdout'''


def read_file(filename=""):
    '''Using with is also much shorter than writing
    equivalent try-finally blocks:'''
    with open(filename, mode="r", encoding="utf-8") as f:
        my_file = f.read()
        print(my_file, end="")
