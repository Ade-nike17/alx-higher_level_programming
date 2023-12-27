#!/usr/bin/python3
"""
This script takes in a URL and an email
Sends a POST request to the passed URL with the email as a parameter
Displays the body of the response (decoded in utf-8)
"""

import urllib.request
import urllib.parse
import sys


def send_post_request(url, email):
    with urllib.request.urlopen(url, data) as response:
        # Read and decode the response body
        response_body = response.read().decode('utf-8')
        print(response_body)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    # Get the url and email from the cmd-line arg
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('ascii')

    # Call the function to send a POST request and display the response
    send_post_request(url, email)
