"""
Concept: HTTP Requests with the requests Library

The `requests` library is Python's de facto standard for making HTTP requests.
It provides a simple, elegant API for interacting with web services.

Key concepts:
- `requests.get(url)` - Makes a GET request to fetch data from a URL
- `requests.post(url, data)` - Makes a POST request to send data
- The response object contains:
  - `status_code` - HTTP status (200 = OK, 404 = Not Found, etc.)
  - `text` - Response body as a string
  - `json()` - Parse response as JSON

Example:
    response = requests.get("https://api.example.com/data")
    if response.status_code == 200:
        data = response.json()

Task: Make a GET request to 'https://httpbin.org/get' and store the response.
      httpbin.org is a free service that echoes back information about your request.
"""

import requests


def main():
    # TODO: Use requests.get() to fetch data from "https://httpbin.org/get"
    # Store the result in the 'response' variable
    response = None

    # Verification
    if response is None:
        raise Exception("You need to make a request! Use requests.get(url)")

    if not hasattr(response, "status_code"):
        raise Exception("response should be a Response object from requests.get()")

    if response.status_code != 200:
        raise Exception(f"Expected status code 200 (OK), got {response.status_code}")

    # Verify we got valid JSON back
    data = response.json()
    if "url" not in data:
        raise Exception(
            "Response doesn't look right - are you hitting the correct URL?"
        )

    print("Request successful!")
    print(f"The server saw your request to: {data['url']}")


if __name__ == "__main__":
    main()
