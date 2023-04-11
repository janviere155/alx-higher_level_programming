#!/bin/bash
# Send a GET request to the URL passed as the first argument and include the -s flag to silence progress meter and other non-error messages.
curl -s -o /dev/null -w '%{http_code}' "$1"
