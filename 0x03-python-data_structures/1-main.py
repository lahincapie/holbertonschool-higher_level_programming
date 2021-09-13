#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
print("Element at index {:d} is {}".format(-2, element_at(my_list, -2)))
print("Element at index {:d} is {}".format(-1, element_at(my_list, -1)))
print("Element at index {:d} is {}".format(0, element_at(my_list, 0)))
print("Element at index {:d} is {}".format(1, element_at(my_list, 1)))
print("Element at index {:d} is {}".format(2, element_at(my_list, 2)))
print("Element at index {:d} is {}".format(3, element_at(my_list, 3)))
print("Element at index {:d} is {}".format(4, element_at(my_list, 4)))
print("Element at index {:d} is {}".format(5, element_at(my_list, 5)))
print("Element at index {:d} is {}".format(6, element_at(my_list, 6)))
