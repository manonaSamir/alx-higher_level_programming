#!/usr/bin/python3
for item in range(0, 100):
    if item == 99:
        print("{}".format(item))
    else:
        print("{:02}".format(item), end=", ")
