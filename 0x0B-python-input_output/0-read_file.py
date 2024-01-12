#!/usr/bin/python3
"""reads a file"""


def read_file(filename=""):
    """reads a file"""
    with open(filename, mode='r', encoding='utf-8') as file_object:
        for line in file_object:
            print(line, end="")
