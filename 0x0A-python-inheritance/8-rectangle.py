#!/usr/bin/python3
'''
class Rectangle that inherits
from BaseGeometry (7-base_geometry.py).
'''


BaseGeometry = __import__('7-base_geometry').Rectangle


class Rectangle(BaseGeometry):
    '''Instantiation '''
    def __init__(self, width, height):
        '''Instantiation '''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
