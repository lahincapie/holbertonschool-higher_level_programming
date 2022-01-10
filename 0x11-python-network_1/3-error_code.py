#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and
displays the body of the response
(decoded in utf-8).
"""

if __name__ == "__main__":
    import urllib.error as err
    import urllib.request as request
    from sys import argv
    res = request.Request(argv[1])
    try:
        with request.urlopen(res) as req:
            print(req.read().decode('utf-8'))
    except err.HTTPError as e:
        print("Error code: {}".format(e.code))
