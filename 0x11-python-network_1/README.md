# Python - Network #1

### **This directory contains 11 programs. The programs were written in Python programming language.**

## [0. What's my status? #0](https://github.com/ehabsmh/alx-higher_level_programming/blob/main/0x11-python-network_1/0-hbtn_status.py)

Fetches https://alx-intranet.hbtn.io/status using `urllib` package.

---

## [1. Response header value #0](https://github.com/ehabsmh/alx-higher_level_programming/blob/main/0x11-python-network_1/1-hbtn_header.py)

 Takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response using `urllib` package.

---

## [2. POST an email #0](https://github.com/ehabsmh/alx-higher_level_programming/blob/main/0x11-python-network_1/2-post_email.py)

Takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8) using `urllib` package.

---

## [3. Error code #0](https://github.com/ehabsmh/alx-higher_level_programming/blob/main/0x11-python-network_1/3-error_code.py)

Takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8). using `urllib` package, but manage urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code.

---

## [4. What's my status? #1](https://github.com/ehabsmh/alx-higher_level_programming/blob/main/0x11-python-network_1/4-hbtn_status.py)

Fetches https://alx-intranet.hbtn.io/status using `requests` package.

---

## [5. Response header value #1](https://github.com/ehabsmh/alx-higher_level_programming/blob/main/0x11-python-network_1/5-hbtn_header.py)

Takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header by using `requests` package.

---

## [6. POST an email #1](https://github.com/ehabsmh/alx-higher_level_programming/blob/main/0x11-python-network_1/6-post_email.py)

Takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response. by using `requests` package.

---

## [7. Error code #1](https://github.com/ehabsmh/alx-higher_level_programming/blob/main/0x11-python-network_1/7-error_code.py)

Takes in a URL, sends a request to the URL and displays the body of the response. by using `requests` package.
- If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code

---

## [8. Search API](https://github.com/ehabsmh/alx-higher_level_programming/blob/main/0x11-python-network_1/8-json_api.py)

takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.

---

## [9. My GitHub!](https://github.com/ehabsmh/alx-higher_level_programming/blob/main/0x11-python-network_1/10-my_github.py)

Takes your GitHub credentials (username and password) and uses the GitHub API to display your id
