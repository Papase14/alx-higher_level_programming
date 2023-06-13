#!/usr/bin/python3
"""
    0-read_file: read_file()
"""


def read_file(filename=""):
    """
        read_file reads teaxt file and prints to stdout
    """
    with open(filename, "r+", encoding='utf-8') as f:
        print("{}".format(f.read()), end="")
