#!/usr/bin/python3
"""
This script takes in a url, sends a request to the url
and displays the value of the variable X-Request-Id in the response header
"""


import requests
import sys


def display_x_request_id(url):
    # send a GET request to the url
    response = requests.get(url)

    x_request_id = response.headers['X-Request-Id']
    print(f"{x_request_id}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    url = sys.argv[1]
    display_x_request_id(url)
