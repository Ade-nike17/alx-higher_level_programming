#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    len1 = len(sys.argv)
    op = '+', '-', '*', '/'
    if len1 < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if sys.argv[2] not in op:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    if op == "+":
        result = add(a, b)
    if op == "-":
        result = sub(a, b)
    if op == "*":
        result = mul(a, b)
    if op == "/":
        result = div(a, b)

    print(f"{a} {op} {b} = {result}")
