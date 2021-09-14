#!/usr/bin/python3
def element_at(my_list, idx):
    len_my_list = len(my_list)
    if idx < 0 or idx >= len_my_list:
        return "None"
    my_new_list = my_list[idx]
    return my_new_list
