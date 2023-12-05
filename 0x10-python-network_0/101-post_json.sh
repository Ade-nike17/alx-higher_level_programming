#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument
# displays the body of the response.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
