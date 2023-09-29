#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header"""

import requests
import sys

r = requests.get(sys.argv[1])
hold = r.headers
for key, value in hold.items():
    if key == "X-Request-Id":
        print(value)
