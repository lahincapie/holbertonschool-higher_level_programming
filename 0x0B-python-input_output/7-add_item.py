#!/usr/bin/python3
"""script that adds all arguments to a Python
list, and then save them to a file"""
import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

f = "add_item.json"

if os.path.isfile(f):
    my_list = load_from_json_file(f)
else:
    my_list = []

for args in sys.argv:
    my_list.append(args)

save_to_json_file(my_list, f)
