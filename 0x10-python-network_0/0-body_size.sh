#!/bin/bash
# Displays the size of body of the URL response
curl -s "$1" | wc -c
