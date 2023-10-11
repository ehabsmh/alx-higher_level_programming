#!/usr/bin/python3

"""
This module inserts a line of text to a file after specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file, after each line containing a specific
    string

    Args:
      filename: The file to insert text
      search_string: a specific string to append after
      new_string: The string will be appended after ``search_string``.
    """
    with open(filename, "r") as rf:
        lines_list = rf.readlines()
        modified_lines = []

        for line in lines_list:
            modified_lines.append(line)
            if search_string in line:
                modified_lines.append(new_string)

        with open(filename, "w") as wf:
            wf.writelines(modified_lines)
