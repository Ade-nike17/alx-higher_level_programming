#!/bin/bash
# sends a HET request to the URL and displays the body of the response
# A header variable X-School-Iser-Id must be sent with the value 98
curl -sH "X-School-User-Id: 98" "$1"
