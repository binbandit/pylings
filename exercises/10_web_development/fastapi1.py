"""
Concept: FastAPI Basics - Creating Routes

FastAPI is a modern, high-performance web framework for building APIs with Python.
It uses Python type hints to provide automatic validation and documentation.

Key concepts:
- Create an app with `app = FastAPI()`
- Define routes using decorators: `@app.get("/path")`, `@app.post("/path")`, etc.
- Route functions return data that FastAPI automatically converts to JSON
- The root path "/" is the base URL of your API

Example:
    from fastapi import FastAPI
    app = FastAPI()

    @app.get("/hello")
    def say_hello():
        return {"greeting": "Hello!"}

    # GET /hello returns: {"greeting": "Hello!"}

Task: Define a root route at "/" that returns {"message": "Hello World"}
      This is the classic first endpoint for any API!
"""

from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


# TODO: Create a GET route for the root path "/"
# The route should return a dictionary: {"message": "Hello World"}
# Hint: Use the @app.get("/") decorator above a function


# Test client for verification (don't modify this)
client = TestClient(app)


def main():
    response = client.get("/")

    if response.status_code == 404:
        raise Exception("Route not found! Define a route using @app.get('/') decorator")

    expected = {"message": "Hello World"}
    actual = response.json()

    if actual != expected:
        raise Exception(f"Wrong response!\n  Expected: {expected}\n  Got: {actual}")

    print("FastAPI basics verified!")
    print(f"Your API responds with: {actual}")


if __name__ == "__main__":
    main()
