#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """prints sorted list of class"""
    def print_sorted(self):
        print(sorted(self))
