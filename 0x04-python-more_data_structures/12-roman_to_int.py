#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    decimal = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    len_roman_string = len(roman_string)
    respond = decimal[roman_string[len_roman_string-1]]

    for i in range(len_roman_string-1, 0, -1):
        current = decimal[roman_string[i]]
        prev = decimal[roman_string[i-1]]
        if prev >= current:
            respond += prev
        else:
            respond -= prev
    return respond
