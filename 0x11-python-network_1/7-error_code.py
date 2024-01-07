#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the body of the\
 response. If the HTTP status code is greater than or equal to 400,\
 print: Error code: followed by the value of the HTTP status code
"""

import requests
from requests.exceptions import HTTPError
from sys import argv

if __name__ == "__main__":
    try:
        response = requests.get(argv[1])
        response.raise_for_status()
        print(response.text)
    except HTTPError as error:
        print("Error code:", error.response.status_code)
