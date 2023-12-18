#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        row = [item for item in my_list if item[1] <= x]
        return(row)
    except:
        return("enter a valid number")
        