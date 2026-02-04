"""
Concept: FastAPI Path Parameters

Path parameters let you capture values from the URL path itself. They're defined
using curly braces in the path and become function arguments.

Key concepts:
- Use `{param_name}` in the path to define a path parameter
- The function must have an argument with the same name
- Type hints enable automatic validation and conversion
- FastAPI returns 422 Unprocessable Entity for invalid types

Example:
    @app.get("/users/{user_id}")
    def get_user(user_id: int):
        return {"user_id": user_id}

    # GET /users/42 returns: {"user_id": 42}
    # GET /users/abc returns: 422 error (not a valid integer)

Path parameters are essential for RESTful APIs where you need to identify
specific resources (users, items, posts, etc.) by their ID.

Task: Define a route "/items/{item_id}" that:
      1. Accepts an integer path parameter called item_id
      2. Returns {"item_id": item_id} with the actual value
"""

from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


# TODO: Create a GET route for "/items/{item_id}"
# The function should accept item_id as an integer parameter
# Return a dictionary with the item_id: {"item_id": item_id}


# Test client for verification (don't modify this)
client = TestClient(app)


def main():
    # Test with item_id = 42
    response = client.get("/items/42")

    if response.status_code == 404:
        raise Exception(
            "Route not found! Define a route using @app.get('/items/{item_id}')"
        )

    if response.status_code == 422:
        raise Exception(
            "Validation error! Make sure item_id parameter has type hint 'int'"
        )

    data = response.json()

    if "item_id" not in data:
        raise Exception(f"Response missing 'item_id' key. Got: {data}")

    if data["item_id"] != 42:
        raise Exception(
            f"Expected item_id to be 42, got {data['item_id']}\n"
            "Make sure you're returning the actual parameter value!"
        )

    # Test with another value to ensure it's dynamic
    response2 = client.get("/items/123")
    if response2.json().get("item_id") != 123:
        raise Exception("The item_id should change based on the URL path!")

    print("FastAPI path parameters verified!")
    print(f"GET /items/42 returns: {data}")
    print(f"GET /items/123 returns: {response2.json()}")


if __name__ == "__main__":
    main()
