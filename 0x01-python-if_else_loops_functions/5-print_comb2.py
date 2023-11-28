#!/usr/bin/python3
for item in range(0, 99):
    if item == 98:
        print("{}".format(item), end="")
    else:
        print("{:02}".format(item), end=", ")

