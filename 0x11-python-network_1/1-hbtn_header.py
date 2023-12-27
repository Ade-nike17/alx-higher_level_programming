#!/usr/bin/python3
import urllib.request
import sys

def get_x_request_id(url):
    # Send a request to the url
        with urllib.request.urlopen(url) as response:
        # Retrieve the X-Request-Id from the header
            x_request_id = response.headers.get('X-Request-Id')

            # Display the value of X-Request-Id
            print(f"{x_request_id}")

if __name__ == "__main__":
    # Check if a URL is provided as a cmd-line arg
    if len(sys.argv) != 2:
        sys.exit(1)

    # Get the url from the cmd-line arg
    url = sys.argv[1]

    # Call the function to get and display X-Request-Id
    get_x_request_id(url)
