"""
Concept: HTTP Requests
The `requests` library is the standard for making HTTP requests in Python. `requests.get(url)` fetches data.

Task: Make a GET request to 'https://httpbin.org/get'.
"""

import requests

def main():
    # FIX ME: Use requests.get to fetch "https://httpbin.org/get"
    # response = requests.get("https://httpbin.org/get")
    response = None
    
    if response is None:
        raise Exception("You didn't make the request!")
        
    if response.status_code != 200:
        raise Exception(f"Expected 200 OK, got {response.status_code}")
        
    print("Request successful!")

if __name__ == "__main__":
    main()
