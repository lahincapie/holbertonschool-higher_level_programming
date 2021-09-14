#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max = my_list[0]
        for aux in my_list:
            if aux > max:
                max = aux
        return max
    return (None)
