#!/usr/bin/python3

"""
This module adds all arguments to a Python list
"""


from sys import argv
from os.path import exists

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

if __name__ == "__main__":

    filename = "add_item.json"
    args_list = argv[1:]
    file_content = []

    if exists(filename):
        file_content = load_from_json_file(filename)

    file_content += args_list

    save_to_json_file(file_content, filename)
