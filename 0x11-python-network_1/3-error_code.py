#!/usr/bin/python3
import urllib.request
import urllib.error
import sys

if len(sys.argv) != 2:
    print("Usage: ./3-error_code.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        response_content = response.read().decode("utf-8")
        print(response_content)

except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")
