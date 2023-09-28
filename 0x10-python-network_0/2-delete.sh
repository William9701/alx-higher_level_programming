#!/bin/bash
#  a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
if [ $# -lt 1 ]; then
	  echo "Usage: $0 <URL>"
	    exit 1
fi

URL=$1

# Send a DELETE request and display the body of the response
curl -X DELETE -i -sS $URL | sed -n '/^\s*$/,$p'

