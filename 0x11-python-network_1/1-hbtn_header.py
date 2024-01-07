#!/usr/bin/python3
"""displays the value of the X-Request-Id variable found in the header of the\
 response."""

from sys import argv
from urllib.request import urlopen

if __name__ == "__main__":
    with urlopen(argv[1]) as response:
        req_id = response.getheader('X-Request-Id')
        print(req_id)
