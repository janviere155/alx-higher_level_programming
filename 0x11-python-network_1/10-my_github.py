#!/usr/bin/python3
"""
script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""

import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = ' https://api.github.com/users/{}'.format(username)
    headers = {'Authorization': 'Bearer {}'.format(password)}
    try:
        r = requests.get(url, headers=headers)
        response = r.json()
        print(response.get('id'))
    except (ValueError, TypeError) as err:
        pass
