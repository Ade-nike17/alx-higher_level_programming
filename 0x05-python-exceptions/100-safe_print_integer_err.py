#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True

    except (TypeError, ValueError) as te:
        print("Exception: {}".format(te.args[0]), file=sys.stderr)
        return False
