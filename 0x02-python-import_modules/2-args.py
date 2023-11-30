#!/usr/bin/python3
import sys

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        if i == 0:
            if len(sys.argv) - 1 == 1:
                print(f"{len(sys.argv) - 1}", "argument:")
            elif (len(sys.argv) - 1) == 0:
                print(f"{len(sys.argv) - 1}", "arguments.")
            else:
                print(f"{len(sys.argv) - 1}", "arguments:")
        else:
            print(f"{i}: {arg}")
