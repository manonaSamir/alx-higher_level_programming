#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """prints the list, but sorted (ascending sort)"""

    def print_sorted(self):
        print(sorted(self))
