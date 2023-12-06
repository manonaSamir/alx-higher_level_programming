#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        values = max(a_dictionary, key=a_dictionary.get)
        return values
