#!/usr/bin/python3
for item in range(97, 123):
    if chr(item) not in ['q', 'e']:
        print("{}".format(chr(item)), end="")
