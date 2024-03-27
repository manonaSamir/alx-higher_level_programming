#!/usr/bin/python3
"""
this function finds a peak in a list of unsorted integers
"""


def Find(lo, h, ints):
    """find the peak int"""
    mid = (lo + h) // 2
    if lo == h:
        return ints[h]
    if ints[mid] < ints[mid + 1]:
        return(Find(mid + 1, h, ints))
    return(Find(lo, mid, ints))


def find_peak(list_of_integers):
    if not list_of_integers:
        return
    return(Find(0, len(list_of_integers) - 1, list_of_integers))
