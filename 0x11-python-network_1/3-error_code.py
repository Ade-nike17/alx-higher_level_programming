#!/usr/bin/python3
"""
This script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""

import urllib.error
import urllib.request
import sys


def send_request_and_display_body(url):
    try:
        # Send a request to the url
        with urllib.request.urlopen(url) as response:
            # Read and decode the response body
            response_body = response.read().decode('ascii')

            # Display the body of the response
            print(response_body)

    except urllib.error.HTTPError as e:
        print(f"Errror code: {e.code}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    url = sys.argv[1]
    send_request_and_display_body(url)
