#!/usr/bin/python3
"""Python script that takes in a URL
and an email, sends a POST request to
the passed URL with the email as a
parameter, and displays the body of
the response (decoded in utf-8)"""


if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    from sys import argv
    value = {'email': argv[2]}
    data = urllib.parse.urlencode(value).encode('ascii')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')
