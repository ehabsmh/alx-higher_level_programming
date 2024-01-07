#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter,\
 and displays the body of the response"""

from urllib.request import Request, urlopen
from urllib import parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}

    data = parse.urlencode(value)
    data = data.encode('ascii')
    with urlopen(url, data) as response:
        body = response.read()
        body.decode('UTF-8')
        print(body)
