#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status using `requests`
"""

import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    r = requests.get(url)

    print("Body response:")
    print("\t- type:", type(r.text))
    print("\t- content:", r.text)
