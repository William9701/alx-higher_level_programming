#!/bin/bash
# a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -I -s "$1" | awk '/HTTP/{print $2}'
