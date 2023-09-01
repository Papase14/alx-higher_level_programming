#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: ./7-error_code.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)

except requests.exceptions.HTTPError as e:
    print(f"Error code: {e.response.status_code}")
