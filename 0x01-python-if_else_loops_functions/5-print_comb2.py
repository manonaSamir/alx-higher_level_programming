#!/usr/bin/python3
for item in range(0, 99):
    if item <= 9:
        print("0{}, ".format(item), end="")
    else:
        print("{}, ".format(item), end="")
print("99")
