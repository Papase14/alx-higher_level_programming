#!/usr/bin/python3
import requests
import sys

if len(sys.argv) == 1:
    q = ""
else:
    q = sys.argv[1]

url = "http://0.0.0.0:5000/search_user"
data = {"q": q}

try:
    response = requests.post(url, data=data)
    response.raise_for_status()
    try:
        result = response.json()
        if result:
            print(f"[{result['id']}] {result['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
