#!/usr/bin/env python3
def no_c(my_string):
    my_new_string = ""
    letter = 0
    while letter < len(my_string):
        if my_string[letter] != "C" and my_string[letter] != "c":
            my_new_string += my_string[letter]
        letter = letter + 1
    return my_new_string
