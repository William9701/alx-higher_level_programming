#!/bin/bash
# Send a GET request with the specified header and display the body of the response
curl -X GET -H "X-School-User-Id: 98" -i -sS "$1" | sed -n '/^\s*$/,$p'
