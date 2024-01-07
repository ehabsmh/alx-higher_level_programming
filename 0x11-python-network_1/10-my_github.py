#!/usr/bin/python3
"""takes your GitHub credentials (username and password) and uses the\
 GitHub API to display your id."""

import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    payload = HTTPBasicAuth(argv[1], argv[2])

    url = "https://api.github.com/user"

    response = requests.get(url, auth=payload).json()
    print(response.get('id'))
