#!/usr/bin/python3

if __name__ == "__main__":
    hid = __import__("hidden_4")
    print(*[name for name in dir(hid) if not name.startswith("__")], sep="\n")
