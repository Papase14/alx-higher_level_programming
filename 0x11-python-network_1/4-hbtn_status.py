#!/usr/bin/python3
import requests

url = "https://alx-intranet.hbtn.io/status"

try:
    response = requests.get(url)
    response.raise_for_status()

    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
