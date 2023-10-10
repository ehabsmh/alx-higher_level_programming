#!/usr/bin/python3

"""
This module adds all arguments to a Python list
"""


import sys
import os

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

if __name__ == "__main__":
    filename = sys.argv[0]
    args_list = sys.argv[1:]

    x = []
    if os.path.exists("add_item.json"):
        x = load_from_json_file("add_item.json")
        x += args_list
    save_to_json_file(x, "add_item.json")
