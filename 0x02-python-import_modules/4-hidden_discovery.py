#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    total = 0
    for name in dir(hidden_4):
        if name.find("__"):
            print(name)
