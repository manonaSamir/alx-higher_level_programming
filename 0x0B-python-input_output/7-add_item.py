#!/usr/bin/python3
"""loads adds saves json to file"""

import json
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('8-load_from_json_file').load_from_json_file

    try:
        jsonList = load_from_json_file("add_item.json")
    except FileNotFoundError:
        """handling the specific exception"""
        jsonList = []

    for i in sys.argv[1:]:
        jsonList.append(i)
    save_to_json_file(jsonList, "add_item.json")
