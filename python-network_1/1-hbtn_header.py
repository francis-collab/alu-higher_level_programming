#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays all headers
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    # Define headers
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "*/*",
    }

    # Create a request object
    request = urllib.request.Request(url, headers=headers)
    
    try:
        with urllib.request.urlopen(request) as response:
            # Print all headers
            for header, value in response.headers.items():
                print(f"{header}: {value}")
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
    except urllib.error.URLError as e:
        print("URL Error: {}".format(e.reason))

