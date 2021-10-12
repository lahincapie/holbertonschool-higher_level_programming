#!/usr/bin/python3
"""Contains the _same_class"""


def is_same_class(obj, a_class):
    """"Verify if the object  is exactly an instance of the specified class"""
    if type(obj) == a_class:
        return True
    else:
        return False
