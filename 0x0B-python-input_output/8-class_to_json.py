#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """classes to json"""
    return obj.__dict__
