#!/usr/bin/python3
from urllib import request


"""Get the status of intranet url"""

if __name__ == "__main__":

    url = "https://alx-intranet.hbtn.io/status"
    with request.urlopen(url) as response:
        data = response.read()
        print("Body response:")
        print(f"\t- type: {type(data)}")
        print(f"\t- content: {data}")
        print(f"\t- utf8 content: {data.decode('utf-8')}")
