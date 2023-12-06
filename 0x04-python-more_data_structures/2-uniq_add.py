#!/usr/bin/python3
def uniq_add(my_list=[]):
    row = sum(item for item in set(my_list) if isinstance(item, int))
    return row
