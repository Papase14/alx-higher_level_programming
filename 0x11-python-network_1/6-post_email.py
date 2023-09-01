#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 3:
    print("Usage: ./6-post_email.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]
data = {"email": email}

try:
    response = requests.post(url, data=data)
    response.raise_for_status()
    print("Your email is:", response.text)

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
