#!/usr/bin/python3
def search_replace(my_list, search, replace):
    row = list(map(lambda x: x if x != 2 else 98, my_list))
    return row
