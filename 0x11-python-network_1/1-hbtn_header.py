#!/usr/bin/python3
import sys
import urllib.request

if len(sys.argv) != 2:
    print("Usage: ./1-hbtn_header.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        request_id = response.headers.get("X-Request-Id")
        if request_id:
            print(request_id)

except Exception as e:
    print(f"Error: {e}")
