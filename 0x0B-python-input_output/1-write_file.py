#!/usr/bin/python3
"""returns number of lines"""


def write_file(filename="", txt=""):
    """Writes a txt to filename."""
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(txt)
