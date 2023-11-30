#!/usr/bin/python3
import sys

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        if i == 0:
            print(f"{len(sys.argv) - 1}", "argument." if (len(sys.argv) - 1)
                  == 1 else "arguments:")
        else:
            print(f"{i}: {arg}")
