#!/usr/bin/python3
"""Adds items to json file from arguments."""
import json
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

"""actually does it"""
try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
