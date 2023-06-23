#!/usr/bin/python3
"""
script that takes in a URL and an email address,
sends a POST request to the passed URL
with the email as a parameter, and finally displays the body of the response.
"""

import requests
import sys


if __name__ == "__main__":
    # get the URL and email from the command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # define the data to be sent in the POST request
    data = {'email': email}

    # send a POST request to the URL with the email as a parameter
    response = requests.post(url, data=data)

    # display the body of the response
    print(response.text)
