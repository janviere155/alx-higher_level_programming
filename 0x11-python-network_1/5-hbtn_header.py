#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
"""


import requests
import sys


if __name__ == "__main__":
    # get the URL from the command-line arguments
    url = sys.argv[1]

    # send a request to the URL and get the response
    response = requests.get(url)

    # get the value of the X-Request-Id header from the response
    x_request_id = response.headers.get('X-Request-Id')

    # display the value of the X-Request-Id header
    print(x_request_id)
