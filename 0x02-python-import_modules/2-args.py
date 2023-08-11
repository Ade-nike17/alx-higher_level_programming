#!/usr/bin/python3

import sys

if __name__ == "__main__":
    len1 = len(sys.argv) - 1
    plural_s = "s" if len1 != 1 else ""
    print(f"{len1} argument{plural_s}", end="")
    if len1 == 0:
        print(".")
        sys.exit()
    print(":")
    for i, arg in enumerate(sys.argv):
        if i > 0:
            print(f"{i}: {arg}")
