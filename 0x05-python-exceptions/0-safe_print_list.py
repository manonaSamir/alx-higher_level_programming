#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        result = [item for item in enumerate(my_list) if item[1] < x]
        return (result)
    except ValueError:
        return ("enter a valid number")
