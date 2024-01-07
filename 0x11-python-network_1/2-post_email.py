#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter,\
 and displays the body of the response"""

from urllib.request import urlopen
from urllib import parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}

    data = parse.urlencode(value).encode('UTF-8')

    with urlopen(url, data) as response:
        body = response.read().decode('UTF-8')
        print(body)
