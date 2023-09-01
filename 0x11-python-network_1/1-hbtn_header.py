#!/usr/bin/python3
import sys
import urllib.request

with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.headers["X-Request-Id"])

