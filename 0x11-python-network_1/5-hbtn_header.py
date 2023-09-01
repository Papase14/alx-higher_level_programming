#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: ./5-hbtn_header.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)
    response.raise_for_status()
    request_id = response.headers.get("X-Request-Id")
    if request_id:
        print(request_id)

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
