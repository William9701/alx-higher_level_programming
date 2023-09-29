#!/usr/bin/python3
""" a Python script that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)"""

if __name__ == "__main__":
    import urllib.request
    import sys
    import urllib.parse

    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary with email as a key and its value from command line
    # argument

    values = {'email': email}

    # Convert dictionary into query parameters and then encode it into bytes
    data = urllib.parse.urlencode(values).encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        html = response.read()

    print(html.decode('utf-8'))
