#!/usr/bin/python3
"""a Python script that takes GitHub credentials (username and password) and
uses the GitHub API to display your id"""

if __name__ == "__main__":
    import requests
    import sys

    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get('https://api.github.com/user',
                            auth=(username, password))

    if response.status_code == 200:
        print(response.json()['id'])
    else:
        print(None)
