#!/usr/bin/python3
'''
BaseGeometry
(based on 6-base_geometry.py).
'''


class BaseGeometry:
    '''Public instance method'''
    def area(self):
        '''raises Exception'''
        raise Exception("area() is not implemented")


    '''Public instance method'''
    def integer_validator(self, name, value):
        if type(value) is not  int:
            raise TypeError("{:s} must be an integer".format(name))
        if type(value) <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
