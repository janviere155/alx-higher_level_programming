#!/bin/bash
# print all the HTTP request methods allowed by server
curl -sI "$1" | grep -i "Allow:" | awk -F ": " '{print $2}' | xargs
