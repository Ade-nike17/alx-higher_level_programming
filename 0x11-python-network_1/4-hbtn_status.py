#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status
"""

import requests


def fetch_and_display_status(url):
    # Send a GET request to the url
    response = requests.get(url)

    # Display the body of the response with tabulation
    print(f"Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    fetch_and_display_status(url)
