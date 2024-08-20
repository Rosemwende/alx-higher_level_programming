#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status and displays the response body."""

from urllib import request

def fetch_status():
    """Fetches the status from the URL and prints the response details."""
    url = "https://alx-intranet.hbtn.io/status"
    with request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print(f"- type: {type(body)}")
        print(f"- content: {body}")
        print(f"- utf8 content: {body.decode('utf-8')}")

if __name__ == "__main__":
    fetch_status()
