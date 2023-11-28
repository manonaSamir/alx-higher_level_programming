#!/usr/bin/python3
for item in range(0, 99):
    if item <= 0:
        print("0{}, ".format(item), end="")
    else:
        print("{}, ".format(item), end="")
print("99")
