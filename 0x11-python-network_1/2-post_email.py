#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

if len(sys.argv) != 3:
    print("Usage: ./2-post_email.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]
data = urllib.parse.urlencode({'email': email}).encode('utf-8')

try:
    with urllib.request.urlopen(url, data=data) as response:
        response_content = response.read().decode('utf-8')
        print(response_content)

except Exception as e:
    print(f"Error: {e}")
