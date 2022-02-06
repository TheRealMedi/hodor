#!/usr/bin/python3
"""
Voting 1024 times my Holberton's id.
"""
import requests


php_dir = "http://158.69.76.135/level0.php"
vote = {
    "id": "3371",
    "holdthedor": "submit"
}

if __name__ == "__main__":
    for i in range(0, 1024):
        requests.post(php_dir, data=vote)
