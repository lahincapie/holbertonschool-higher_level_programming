#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return None
    """ [inicio : fin : pasos]  """
    """ [inicia en 0 : hasta el final : de uno en uno desde el final ]  """
    for item in my_list[::-1]:
        print("{:d}".format(item))
