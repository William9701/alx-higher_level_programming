#!/bin/bash
# a Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -X OPTIONS -i -sS "$1" | grep -i "Allow:" | sed -e 's/Allow: //I'
