#!/usr/bin/python3

"""
    Python - Input/Output 13.Search and Update 
"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file
        after each line containing a
        specific string
    """
    with open(filename, 'r+') as f:
        lines = f.readlines()
        f.seek(0)

        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)

        f.truncate() 
