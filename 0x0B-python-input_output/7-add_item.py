#!/usr/bin/python3
"""script that adds all arguments to a Python
list, and then save them to a file"""
import sys
import os


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file =( __import__('6-load_from_json_file')
                                        .load_from_json_file)

    filename = "add_item.json"
    exists = os.path.isfile(filename)

    if exists:
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    for arg in sys.argv:
        if arg == "7-add_item.py":
            continue
        my_list.append(arg)

    save_to_json_file(my_list, filename)
