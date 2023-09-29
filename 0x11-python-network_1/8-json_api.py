#!/usr/bin/python3
"""a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) > 1:
        payload = {'q': sys.argv[1]}
    else:
        payload = {'q': ''}

    r = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        json_dict = r.json()
        if len(json_dict) == 0:
            print('No result')
        else:
            print(f"[{json_dict['id']}] {json_dict['name']}")
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')
