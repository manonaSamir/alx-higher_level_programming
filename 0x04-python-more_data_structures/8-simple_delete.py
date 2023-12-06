#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    return {x: value for x, value in a_dictionary.items() if x != key}
