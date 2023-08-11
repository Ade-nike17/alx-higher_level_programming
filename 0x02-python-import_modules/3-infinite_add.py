#!/usr/bin/python3

import sys

if __name__ == "__main__":
    len1 = len(sys.argv)
    if len1 == 0:
        print("0")
    number = [int(sys.argv[i]) for i in range(1, len1)]
    total = sum(number)
    print(f"{total}")
