#!/usr/bin/python3
import json
'''function that returns the JSON representation
of an object (string)'''


def to_json_string(my_obj):
    '''Serialize obj to a JSON formatted str.
    If skipkeys is true then dict keys that are
    not basic types (str, int, float, bool, None)
    will be skipped instead of raising a TypeError.'''
    return json.dumps(my_obj)
