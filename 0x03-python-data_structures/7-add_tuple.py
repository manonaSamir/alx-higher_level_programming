#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if not tuple_b:
        return tuple_a
    if not tuple_a:
        return tuple_b
    return tuple(map(sum, zip(tuple_a, tuple_b)))
