#!/usr/bin/python3

from sys import argv
from urllib.request import urlopen

with urlopen(argv[1]) as response:
    req_id = response.getheader('X-Request-Id')
    print(req_id)
