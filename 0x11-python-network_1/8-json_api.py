#!/usr/bin/python3
"""takes in a letter and sends a POST request to\
 http://0.0.0.0:5000/search_user with the letter as a parameter."""

import requests
from sys import argv

if __name__ == "__main__":
    argv = argv[1:2]
    if not len(argv):
        argv.append('')

    payload = {"q": argv[0]}
    url = "http://0.0.0.0:5000/search_user"

    try:
        response = requests.post(url, data=payload).json()

        if response.json() == {}:
            print("No result")
        else:
            print(f"[{response.get('id')}] {response.get('name')}")
    except ValueError:
        print("Not a valid JSON")
