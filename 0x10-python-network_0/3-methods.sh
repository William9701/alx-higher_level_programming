#!/bin/bash
# a Bash script that takes in a URL and displays all HTTP methods the server will accept.
if [ $# -lt 1 ]; then
	  echo "Usage: $0 <URL>"
	    exit 1
fi

URL=$1

# Send an OPTIONS request to the URL to determine accepted HTTP methods
curl -X OPTIONS -i -sS $URL | grep -i "Allow:" | sed -e 's/Allow: //I'

