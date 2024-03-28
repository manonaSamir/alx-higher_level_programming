#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
import requests
import urllib.request


if __name__ == "__main__":
    request = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(request.text)))
    print("\t- content: {}".format(request.text))
