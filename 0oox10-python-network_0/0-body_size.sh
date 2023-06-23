#!/bin/bash
# Bash script that displays the size of the body
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
