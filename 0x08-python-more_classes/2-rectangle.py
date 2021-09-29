#!/usr/bin/python3
'''Write a class Rectangle that defines a
rectangle by: (based on 0-rectangle.py)'''


class Rectangle:
    '''class Rectangle'''

    def __init__(self, width=0, height=0):
        '''Initializes the instance'''
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.__height

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        per = (2 * self.__height) + (2 * self.__width)
        return per
