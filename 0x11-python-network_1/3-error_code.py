#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the body of the\
 response (decoded in utf-8)."""

from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    try:
        with urlopen(url) as response:
            body = response.read().decode('UTF-8')
            print(body)
    except HTTPError as error:
        print("Error code:", error.getcode())
